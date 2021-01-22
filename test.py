import time
import config
import pyperclip
import chromedriver_autoinstaller
import selenium
import re
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup


# 개인정보를 탐색할 블로거 명단 읽어오기
f = open('list.txt', mode='rt', encoding='utf-8')
blogger_list = f.read().splitlines()

# Selenium Driver 생성
chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

# 네이버 로그인
driver.get(url='https://www.naver.com/')
driver.find_element_by_xpath('//*[@id="account"]/a').click()
time.sleep(1)
pyperclip.copy(config.NAVER_ID)
driver.find_element_by_xpath('//*[@id="id"]').send_keys(Keys.COMMAND, 'v')
time.sleep(1)
pyperclip.copy(config.NAVER_PW)
driver.find_element_by_xpath('//*[@id="pw"]').send_keys(Keys.COMMAND, 'v')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="log.login"]').click()
time.sleep(2)

# xpath 검증 메소드
def has_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False

# 중고나라 게시물 검색
search_url = 'https://cafe.naver.com/joonggonara?iframe_url=/ArticleSearchList.nhn%3Fsearch.clubid=10050146%26search.searchBy=0%26search.query='
num = 0         # 게시물을 작성한 블로거
real_num = 0    # 게시물 안에 번호를 남긴 블로거

for blogger_id in blogger_list:
    driver.get(url=(search_url + blogger_id))
    driver.switch_to.frame('cafe_main') # iframe switching
    print(blogger_id)

    # xpath 유효성 체크
    if has_xpath('//*[@id="main-area"]/div[5]/table/tbody/tr/td/div'):
        intext = driver.find_element_by_xpath('//*[@id="main-area"]/div[5]/table/tbody/tr/td/div')
        # 등록된 게시물 여부 체크
        if intext.text == '등록된 게시글이 없습니다.':
            pass
            # print('{0} 블로거는 중고나라를 이용하지 않습니다.'.format(blogger_id))
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
                # print('{0} 블로거는 중고나라를 이용합니다.'.format(blogger_id))
                # print('작성한 글 개수: {0}개'.format(len(article_list)))
                num = num + 1

                # 실제 게시물 안에서 번호 탐색
                # 번호를 하나라도 발견하면 그 상태로 분기 종료
                for article_id in article_list:
                    # 폐쇄된 게시물인 경우 그냥 넘김
                    try:
                        article_addr = 'https://cafe.naver.com/ca-fe/ArticleRead.nhn?clubid=10050146&page=1&inCafeSearch=true&searchBy=0&includeAll=&exclude=&include=&exact=&searchdate=all&media=0&sortBy=date&articleid={0}&referrerAllArticles=true'.format(article_id)
                        driver.get(url=article_addr)
                        driver.switch_to.frame('cafe_main') # iframe switching
                        time.sleep(2)
                        bs = BeautifulSoup(driver.page_source, 'html.parser')

                        intext_tag = bs.select('.article_container')[0].get_text()
                        phone = re.compile('010\s*-{0,1}\s*\d{4}\s*-{0,1}\s*\d{4}').findall(intext_tag)

                        # 번호 발견
                        if len(phone) > 0:
                            print('들오긴 함')
                            for n in phone:
                                edit_n = re.sub('\s+', '-', n)
                                edit_n = re.sub('-', '', edit_n)
                                print('{0} 블로거의 전화번호: {1}'.format(blogger, edit_n))
                                real_num = real_num + 1
                                break
                            break
                    except:
                        break
            else:
                pass
                # print('{0} 블로거는 중고나라를 이용하지 않습니다.'.format(blogger_id))

    driver.implicitly_wait(3)
    
print('번호 추출 가능해보이는 사람: {0}명'.format(num))
print('실제로 번호가 적힌 사람: {0}명'.format(real_num))

driver.close()