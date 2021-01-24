import re
import os
import time
import pyperclip
import chromedriver_autoinstaller
from PyQt5 import QtCore, QtWidgets
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


class Thread(QtCore.QThread):
    label_changed = QtCore.pyqtSignal(str)
    progress_changed = QtCore.pyqtSignal(int)
    list_changed = QtCore.pyqtSignal(int, list)
    list_reset = QtCore.pyqtSignal()
    num_of_row_changed = QtCore.pyqtSignal(int)

    def __init__(self, parent, window):
        super().__init__(parent)
        self.window = window

    # xpath 유효성 검증 메소드
    def has_xpath(self, xpath, driver):
        try:
            driver.find_element_by_xpath(xpath)
            return True
        except:
            return False

    # Dummy Flush
    def flush(self):
        pass
    
    def run(self):
        # 개인정보를 탐색할 블로거 명단 읽어오기
        f = open(self.window.fname[0], mode='rt', encoding='utf-8')
        self.window.blogger_list = f.read().splitlines()

        # 카운트 관련 변수
        num_of_row      = 0 # Table Row
        num_of_blogger  = len(self.window.blogger_list)

        # 준비 Label과 Process 변경
        self.label_changed.emit('수집 중')
        self.progress_changed.emit(0)
        self.list_reset.emit()

        # Selenium Driver 생성
        chromedriver_autoinstaller.install(cwd=True)
        time.sleep(1)
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('--app=http://www.google.com')
        driver = webdriver.Chrome(chrome_options=options)

        # 네이버 로그인
        driver.get(url='https://www.naver.com/')
        driver.find_element_by_xpath('//*[@id="account"]/a').click()
        time.sleep(1)
        pyperclip.copy(self.window.user_info[0])
        driver.find_element_by_xpath('//*[@id="id"]').send_keys(Keys.CONTROL, 'v')
        time.sleep(1)
        pyperclip.copy(self.window.user_info[1])
        driver.find_element_by_xpath('//*[@id="pw"]').send_keys(Keys.CONTROL, 'v')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="log.login"]').click()
        time.sleep(2)

        # 중고나라 게시물 검색
        search_url = 'https://cafe.naver.com/joonggonara?iframe_url=/ArticleSearchList.nhn%3Fsearch.clubid=10050146%26search.searchBy=0%26search.query='

        for blogger_id in self.window.blogger_list:
            driver.get(url=(search_url + blogger_id))
            driver.switch_to.frame('cafe_main') # iframe switching
            blogger_phone = ''

            # xpath 유효성 검증
            if self.has_xpath('//*[@id="main-area"]/div[5]/table/tbody/tr/td/div', driver):
                intext = driver.find_element_by_xpath('//*[@id="main-area"]/div[5]/table/tbody/tr/td/div')
                # 등록된 게시물 여부 체크
                if intext.text == '등록된 게시글이 없습니다.':
                    pass
                else:
                    bs = BeautifulSoup(driver.page_source, 'html.parser')
                    # 블로거가 게시물을 작성했는지 체크
                    article_tags = bs.select('#main-area > div.article-board.result-board.m-tcol-c > table > tbody > tr')
                    article_list = []
                    for article in article_tags:
                        # 답글의 경우 불필요하므로 except에서 거름
                        try:
                            article_id = article.get_text().split()[0]
                            # 블로그가 작성한 글 여부
                            if blogger_id in article.select('a.m-tcol-c')[0]['onclick']:
                                article_list.append(article_id)
                            else:
                                pass
                        except:
                            pass
                    if len(article_list) > 0:
                        # 실제 게시물 안에서 번호 탐색
                        # 번호를 하나라도 발견하면 그 상태로 분기 종료
                        for article_id in article_list:
                            # 폐쇄된 게시물인 경우 그냥 넘김
                            try:
                                article_addr = 'https://cafe.naver.com/ca-fe/ArticleRead.nhn?clubid=10050146&page=1&inCafeSearch=true&searchBy=0&includeAll=&exclude=&include=&exact=&searchdate=all&media=0&sortBy=date&articleid={0}&referrerAllArticles=true'.format(article_id)
                                driver.get(url=article_addr)
                                driver.switch_to.frame('cafe_main') # iframe switching
                                time.sleep(1)
                                bs = BeautifulSoup(driver.page_source, 'html.parser')
                                intext_tag = bs.select('.article_container')[0].get_text()
                                phone = re.compile(r'(?:010|01o|o10|o1o|0l0|0lo|ol0|olo)\s*-{0,1}\s*\d{4}\s*-{0,1}\s*\d{4}').findall(intext_tag)

                                # 번호 발견
                                if len(phone) > 0:
                                    for n in phone:
                                        n = re.sub('\s', '', n)
                                        n = re.sub('-', '', n)
                                        n = re.sub('l', '1', n)
                                        n = re.sub('o', '0', n)
                                        n = n[:3] + '-' + n[3:7] + '-' + n[7:]
                                        blogger_phone = n
                                        break
                                    break
                            except:
                                pass

            # # 테이블 뷰에 데이터 추가
            self.list_changed.emit(num_of_row, [blogger_id, blogger_id + '@naver.com', blogger_phone])
            num_of_row = num_of_row + 1
            # Progress 진행
            self.progress_changed.emit(int((num_of_row/num_of_blogger)*100))

        # 완료 레이블 변경
        self.label_changed.emit('수집 완료')
        self.num_of_row_changed.emit(num_of_row)

        # Selenium Close
        driver.close()
        os.system('taskkill /f /im chromedriver.exe')