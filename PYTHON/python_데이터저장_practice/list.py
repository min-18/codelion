# 전체 리스트 안에 딕셔너리형태로 요소 넣기.

total_list = []

# 반복해서 질문 받기.
while True:
    question = input("질문을 입력하세요 : ")    #취미는? ->딕셔너리 안에 넣어야

    if question == "q":
        break
    else:
        # 리스트 안에 append해야 반복해서 질문 들어감. 딕셔너리형태로 append 할 수 있다는 걸 새로 배움.
        total_list.append({"질문" : question, "답변" : ""})

print(total_list)

# 이제 리스트에 담긴 질문들 보여주면서 답변 입력받아 저장.
for i in total_list:
    # 딕셔너리의 값 꺼낼 때 키를 제시하면 된다.
    print(i["질문"])
    answer = input("답변을 입력해주세요 : ")
    i["답변"] = answer

print(total_list)
