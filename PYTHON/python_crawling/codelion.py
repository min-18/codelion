# 함수는 반복되는 작업
# 모듈 ; 함수 또는 클래스들을 모아놓은 파일. 모듈은 내가 만들거나 남이 만든 걸 가져다 쓸 수 있다. 
# import로 모듈가져오기
import requests     # 요청하는 모듈
from bs4 import BeautifulSoup       # BeautifulSoup는 가져온 데이터를 의미있는 데이터로 변경하는 것을 도와줌.
from datetime import datetime       # 시간정보 불러오는 모듈

url = "https://finance.naver.com/sise/sise_market_sum.naver"

# requests.get(url) ; get요청을 보내는 함수 / return requests.response
response = requests.get(url)

# BeautifulSoup(데이터, 파싱방법) 형태 
# str타입인 response.text를 BeautifulSoup라는 통에 넣고 의미있는 데이터를 추출
soup = BeautifulSoup(response.text, 'html.parser')

# # 생성할 파일명, 쓰기목적 명시
# file = open('naver.html', 'w')
# file.write(response.text)
# # 파일 열었으면 닫아주는 것까지 마무리
# file.close()

# print(soup.title.string)
# print(soup.span)
# print(soup.find_all('span'))

# a태그의 클래스명이 tltle 인 부분 정보 담김. ; 리스트 형태로
results = soup.find_all('a', 'tltle')

# 아래코드처럼 select를 이용해 가져올 수도.
# results = soup.select('.tltle')

print(datetime.today().strftime("%Y년 %m월 %d일 코스피 시가총액 순위 \n"))

num = 1
# 반복문을 통해 리스트안에 있는 정보 하나씩 추출
for result in results:
    print(num, "위 : ", result.get_text())
    num += 1

