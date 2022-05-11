# pip3 install googletrans==4.0.0-rc1 을 설치 해줘야한다. ; pip3 install googletrans 그냥 이렇게 설치하면 오류뜸...
# googletrans 라이브러리는 언어 감지, 언어 변역 기능 두가지 가짐.
from googletrans import Translator

# 번역기 생성
translator = Translator()

# 번역하고 싶은 문장
# sentence = "안녕하세요"
sentence = input('번역하고 싶은 문장을 입력하세요 : ')
dest = input('어떤 언어로 번역할까요? : ')

# 언어감지
detected = translator.detect(sentence)

# 번역한 결과 ; translate(번역할 문장, 번역목적지, src) 형태 ;; src는 optional
result = translator.translate(sentence, dest)

print("========번역 결과========")
print(detected.lang, ":", sentence)
print(result.dest, ":", result.text)
print("=========================")
