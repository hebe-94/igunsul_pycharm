# 셀레니움 불러오기

from selenium import webdriver
from time import sleep
# 크롬 웹 드라이버 경로 설정

driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')

# 크롬을 통해 로그인화면 접속
driver.get('https://igunsul.net')


# 아이디와 비밀번호 입력 (0.3초 간격으로)
sleep(0.5)
driver.find_element_by_name('id').send_keys('songam')

sleep(0.5)
driver.find_element_by_name('pw').send_keys('qwer1234!@')

# XPath를 이용해 로그인 시도 및 데이터 화면 이동
sample = driver.find_element_by_css_selector('#login_btn')
driver.execute_script("arguments[0].click();", sample)

sample = driver.find_element_by_class_name("menu03")
driver.execute_script("arguments[0].click();", sample)

driver.find_element_by_css_selector('#headerMyRoomTabWrap > div:nth-child(3)').click()


#웹페이지의 소스코드를 파싱하기 위해 Beautiful Soup 라이브러리 호출
from bs4 import BeautifulSoup

driver.get("http://www.igunsul.net/myroom")
driver.find_element_by_css_selector('#headerMyRoomTabWrap > div:nth-child(3)').click()
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

# 사업명 하나씩 꺼내오기
title_list = soup.find_all('list2detailAnchor listColormyroom_list myroom_list')
for title in title_list:
    print(title.text)
