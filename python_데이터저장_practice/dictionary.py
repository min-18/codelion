# 딕셔너리로 질문:답변 입력받고 저장

total_dictionary = {}

while True:
    question = input("질문을 입력해주세요 : ")  
    if question == "q":
        break
    else:       # 딕셔너리에 질문 추가
        total_dictionary[question] = ""     # 질문은 키에, 값은 빈 형태로 일단 저장.

print(total_dictionary)

# 이제 답변을 넣을 차례
# 질문들을 하나씩 꺼내서(for반복문으로 딕셔너리 요소 하나씩) 답변 넣기.

for i in total_dictionary:
    print(i)
    answer = input("답변을 입력해주세요 : ")
    total_dictionary[i] = answer

print(total_dictionary)

