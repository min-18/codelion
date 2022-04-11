# 프로젝트 
# 메뉴후보 추가하고 빼고 해서 최종 후보 결정 후 그중에서 랜덤 선택하는 프로그램.
import random
import time

menu = []
# 리스트를 집합으로
set_menu = set(menu)

# 리스트보다 집합이 유리한 이유는 순서가 필요없고 중복을 고려할 수 있기 때문. 
# 거기에 더해 제거할 때도 사용자가 리스트 안에 없는 값을 입력했을 때 발생할 수 있는 오류를 방지할 수 있다.
while True:
    add_option = input("어떤 메뉴를 추가할까요? : ")

    if add_option == "q":
        print("현재 메뉴 = ", set_menu)
        break
    else:
        set_menu = set_menu | set([add_option])
        print("현재 메뉴 = ", set_menu)
        # menu.append(add_option)

while True:
    del_option = input("어떤 메뉴를 삭제할까요? : ")

    if del_option == "q":
        print("최종 후보 = ", set_menu)
        break
    else:
        set_menu = set_menu - set([del_option])
        print("현재 메뉴 = ", set_menu)

# 반복되는 부분은 반복문으로! ; 이 부분을 함수로 처리할까도 고민했으나 단순해서 그냥 반복문이 더 좋을 거라 판단.
# 숫자감소시키기
# range(시작, 끝, 얼만큼 변화시킬지;감소시키려면 증가폭 음수로.)
for i in range(5,0,-1):
    print(i)
    time.sleep(1)

# set에서는 random.choice를 쓸 수가 없다. 그래서 list로 형태를 바꿔서 하자.
final_menu = random.choice(list(set_menu))
print(final_menu)