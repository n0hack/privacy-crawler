import time
import pyperclip
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import chromedriver_autoinstaller


def hasxpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False


# Read Blogger ID
f = open('list.txt', mode='rt', encoding='utf-8')
blogger_list = f.read().splitlines() 
f.close()


chromedriver_autoinstaller.install()
URL = 'https://www.naver.com/'
driver = webdriver.Chrome()
driver.get(url=URL)

element = driver.find_element_by_xpath('//*[@id="account"]/a')
element.click()
time.sleep(1)

my_id = 'nohack-'
my_pw = 'wjswlehf2!N'
txt_id = driver.find_element_by_xpath('//*[@id="id"]')
txt_pw = driver.find_element_by_xpath('//*[@id="pw"]')
pyperclip.copy(my_id)
txt_id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)
pyperclip.copy(my_pw)
txt_pw.send_keys(Keys.CONTROL, 'v')
time.sleep(1)
element = driver.find_element_by_xpath('//*[@id="log.login"]')
element.click()
time.sleep(1)

# driver.get('https://cafe.naver.com/joonggonara')
# time.sleep(1)
# element = driver.find_element_by_xpath('//*[@id="topLayerQueryInput"]')
# element.send_keys(blogger_list[0])

# element = driver.find_element_by_xpath('//*[@id="cafe-search"]/form/button')
# element.click()

# time.sleep(1)

SEARCH_URL = 'https://cafe.naver.com/joonggonara?iframe_url=/ArticleSearchList.nhn%3Fsearch.clubid=10050146%26search.searchBy=0%26search.query='

test_url = SEARCH_URL + 'hyunju3685'
driver.get(url=test_url)
driver.switch_to.frame("cafe_main")

f = open('test2.html', mode='wt', encoding='utf-8')
f.write(driver.page_source)
f.close()



time.sleep(1)

test_url = SEARCH_URL + 'jenahj'
driver.get(url=test_url)
driver.switch_to.frame("cafe_main")

f = open('test1.html', mode='wt', encoding='utf-8')
f.write(driver.page_source)
f.close()

# 중고나라 이용 여부 체크
if hasxpath('//*[@id="main-area"]/div[5]/table/tbody/tr/td/div'):
    test_text = driver.find_element_by_xpath('//*[@id="main-area"]/div[5]/table/tbody/tr/td/div')
    if test_text.text == '등록된 게시글이 없습니다.':
        print('해당 블로거는 중고나라를 이용하지 않습니다.')
    else:
        pass


# if hasxpath('//*[@id="main-area"]/div[5]/table/tbody/tr/td/div'):
#     element = driver.find_element_by_xpath('//*[@id="main-area"]/div[5]/table/tbody/tr/td/div')
#     print(element.text)
# else:
#     print('없슴')

time.sleep(5)
driver.close()


















# # Close File
# f.close()


# URL = 'https://www.naver.com/'
# driver = webdriver.Chrome(executable_path='chromedriver')
# driver.get(url=URL)

# element = driver.find_element_by_xpath('//*[@id="account"]/a')
# element.click()
# time.sleep(1)

# my_id = 'nohack-'
# my_pw = 'wjswlehf2!N'
# txt_id = driver.find_element_by_xpath('//*[@id="id"]')
# txt_pw = driver.find_element_by_xpath('//*[@id="pw"]')
# pyperclip.copy(my_id)
# txt_id.send_keys(Keys.CONTROL, 'v')
# time.sleep(1)
# pyperclip.copy(my_pw)
# txt_pw.send_keys(Keys.CONTROL, 'v')
# time.sleep(1)
# element = driver.find_element_by_xpath('//*[@id="log.login"]')
# element.click()
# time.sleep(1)

# driver.get('https://cafe.naver.com/joonggonara')

# time.sleep(5)
# driver.close()