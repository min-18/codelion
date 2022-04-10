# 집합 set
# 순서가 없다는 점, 중복요소가 없다는 점이 리스트와의 차이점이다.
# 고등학교 때 배운 집합이랑 똑같다. 교집합, 합집합, 차집합 연산도 그대로 사용.

menu1 = ["탕수육", "짜장면", "짬뽕", "마라탕.."]
menu2 = ["돈가스", "초밥", "텐동", "탕수육"]

# 리스트에서 집합으로 변환한다.
set_menu1 = set(menu1)
set_menu2 = set(menu2)

# 교집합
print(set_menu1 & set_menu2)
# 합집합
print(set_menu1 | set_menu2)
# 차집합
print(set_menu1 - set_menu2)




