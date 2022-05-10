import requests
import json

city = 'Seoul'
# api key ; 누가 이 api를 사용하는지 알 수 있는 고유값
apikey = '1e714b730d59169e2f82b006c61da546'
lang = 'kr'

# units=metric ; 화씨를 섭씨로 바꿔줌.
api = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric'

# api주소로 get요청을 보내 받은 정보가 담김.
result = requests.get(api)      
# print(result.text)      근데 str타입임.

# json타입으로 변경하고 싶을 때
data = json.loads(result.text)      # dic 타입으로 변경

print(data)
print(data['name'], '의 날씨정보입니다.')
print('오늘은', data['weather'][0]['main'])
print('현재 기온 : ', data['main']['temp'], "도")
print('체감 온도 : ', data['main']['feels_like'], "도")
print('최저 기온 : ', data['main']['temp_min'], "도")
print('최고 기온 : ', data['main']['temp_max'], "도")
print('풍속 : ', data['wind']['speed'], "m/s")

