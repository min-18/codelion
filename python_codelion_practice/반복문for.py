import random

menu = ["된찌", "김치볶음밥", "라면", "김밥", "국수", "돈가스"]

# range로 반복 범위를 설정할 수 있음.
# 1~10미만, 즉 9번까지 반복
# random.choice 함수를 반복문 안에 넣어줘야 새롭게 뽑는 과정을 반복
for i in range(1,10):
    print(i, random.choice(menu))

# 리스트 안의 요소를 순서대로 하나씩 끄집어내서 반복문 돌릴 수 있음.
num = 1
for i in menu:
    print(f"{num}번 메뉴 :",i)
    num += 1

# 이렇게 코드를 작성할 수도 있지만 범위가 커졌을 때 직접 세기 힘들다는 점, 만약 리스트 요소가 바꼈을 때 매번 바꿔줘야한다는 점때문에 리스트요소를 끄집어내는 방법이 더 좋은 것 같다.
# 아래코드는 비추
for i in range(6):
    print(menu[i])


# 딕셔너리 값도 순서대로 끄집어내서 반복문 돌릴 수 있음.
# .items()함수를 이용하면 키:값 모두 꺼낼 수 있음./ 그냥 딕셔너리만 쓰면 키만 내보낸다.
menu_list = {"김치볶음밥" : 5000, "새우볶음밥" : 6000, "돈가스" : 9000}
for i in menu_list.items():
    print(i)

# 키만 불러낼 수도
for i in menu_list.keys():
    print(i)
# 값만 불러낼 수도
for i in menu_list.values():
    print(i)

# 키와 값을 따로 불러내고 싶을 때.
for x,y in menu_list.items():
    print(x)
    print(y) 

# 한줄 for문
customer = [1,2,3,4,5]
customer = ["A-" + str(i+100) for i in customer]
print(customer)