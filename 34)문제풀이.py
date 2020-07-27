#if문제4
a = int(input("A층 엘리베이터 현재 위치 : "))
b = int(input("B층 엘리베이터 현재 위치 : "))
me = int(input("층 입력 : "))
if abs(me-a) > abs(me-b):
    print("B 엘리베이터가 움직입니다.")
else:
    print("A 엘리베이터가 움직입니다.")
#if문제5
EngBook = {"money":"돈","key":"열쇠"}
word = input("영어 단어 입력 : ")
kor = input("영어 단어 뜻 입력 : ")
if word in EngBook:
    if EngBook[word] == kor:
        print("정답입니다.")
    else:
        print("뜻이 틀렸습니다.")
else:
    print("사전에 없습니다.")