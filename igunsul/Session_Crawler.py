import requests
from bs4 import BeautifulSoup as bs

Member_Data = {
    'status': 'login',
    'url2': 'common',
    'url': '',
    'login_page_value': '1',
    'go_page': '',
    'id': 'songam',
    'pw': 'qwer1234!@'
}

# 하나의 세션 객체를 생성해 일시적 유지
with requests.Session() as s:
    requests = s.post('https://www.igunsul.net/login/login_process', data=Member_Data)


# 나의방[엠에스그리드] 접근 URL
requests = s.get('http://igunsul.net/myroom?value="&freeze=&page_num=1&list_num=500&align=5&myroom_folder_eum=yes&folder_num=2&myroom_folder_info=&folder_seq=')
print('myroom 내용')

requests.encoding = 'euc-kr'
soup = bs(requests.text, 'html.parser')

result = soup.findAll('a', {"class": "list2detailAnchor listColormyroom_list myroom_list"})



# 반복문 개수 결정(반복문 시작)
print(len(result))

print(result)




# 반복문 시작해서 다시 한번더 링크 변경
requests = s.get('http://igunsul.net/'+result[0].get('href'))
requests.encoding = 'euc-kr'
soup = bs(requests.text, 'html.parser')



# 공고명 : <title>
#
result = soup.findAll('li')
# 120 종목
# 121 기초금액
# 123 투찰율
# 124 투찰 마강일
print(requests.text)

print('result값 확인')

# print(result[0].get('href'))



