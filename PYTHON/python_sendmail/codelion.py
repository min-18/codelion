# smtp란 서버에 요청을 보내고 서버가 다른 서버에 요청을 보내는 방식정도로 이해

# stmp 메일서버로 내용을 쉽게 보낼 수 있게 해주는 라이브러리
import smtplib
# MIME 형태를 띠는 이메일을 만들기 위한 방법 중 하나로 EmailMessage기능 활용
from email.message import EmailMessage
# 이미지의 확장자를 판단해주는 역할
import imghdr
# 정규표현식 사용위해
import re

def sendEmail(address): 
    # 이메일 주소의 유효성 검사하기 ; 정규표현식 활용
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    
    # if문 팁) bool함수; 안에 값이 있으면 Ture, 없으면 False
    
    # match 함수는 정규표현식, 검사할 형식을 재료를 필요로함.
    if bool(re.match(reg, address)):
        # 보낼 메시지 통 필요
        smtp.send_message(message)
        print('정상적으로 메일을 보냈습니다.')
    else:
        print('유효한 이메일 형식이 아닙니다.')

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465

# MIME형식으로 담을 통
message = EmailMessage()

# 그 통에 담길 이메일 본문내용
message.set_content('이메일 내용')

# header부분에 들어가는 내용은 대괄호형태로(딕셔너리) 정보를 넣어줌.; 제목, 수신인, 발신인
message['Subject'] = "제목부분 입니다"
message['From'] = 'doleme00@likelion.org'
message['To'] = 'doleme00@likelion.org'

# binary ; jpeg, png, exe, mp4 같이 이미지, 설치파일, 영상 파일등을 컴퓨터가 읽을 수 있는 언어로 변경한 것.

# 파일 열고 닫기
# image = open('likelion_logo.png', 'rb')
# image.read()
# image.close()

# 위 방법보다 안전하게 열고 닫는 방법 ; with 사용하기 ;; close할 필요 없음.
# 이미지 파일을 rb모드로 읽어서 image라는 변수에 담을게. 라는 의미
with open('likelion_logo.png', 'rb') as image:
    image_file = image.read()

image_type = imghdr.what('likelion_logo', image_file)
print(image_type)
# 이미지 첨부
message.add_attachment(image_file, maintype="image", subtype=image_type)

# smtp 서버에 연결하기 위해 서버주소와 포트번호 필요
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

# smtp의 login함수는 아이디와 비밀번호 필요
smtp.login('', '')

# sendEmail 함수 실행
sendEmail("doleme00@likelion.org")

smtp.quit()







