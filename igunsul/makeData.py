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

# 엠에스그리드 넘어가기
# sample = driver.find_element_by_class_name("menu03")
# driver.execute_script("arguments[0].click();", sample)

# 송암으로 다시 넘어가기
# driver.find_element_by_css_selector('#headerMyRoomTabWrap > div:nth-child(3)').click()


# 웹페이지의 소스코드를 파싱하기 위해 Beautiful Soup 라이브러리 호출
from bs4 import BeautifulSoup

driver.get("http://www.igunsul.net/myroom")
driver.find_element_by_css_selector('#headerMyRoomTabWrap > div:nth-child(3)').click()

# 반복문으로 반복작업 하기
# 아이디어 1 > table의 tr의 수를 세서 반복문의 횟수를 지정
table = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/table/tbody')
tr = table.find_elements_by_tag_name("tr")

# 반복문 사용해서 각 페이지 들어가고, 데이터 뽑아 오기(여기부터 진행 할것)
# 리스트가 된다면 DB로 올기는 것으로 (예정)

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
print(soup)

print('tr의 개수')
print(len(tr))
print('여기까지')

# 사업명 하나씩 꺼내오기
# title_list = soup.find_all('a','list2detailAnchor listColormyroom_list myroom_list')
# for title in title_list:
#     print(title.text.strip())
