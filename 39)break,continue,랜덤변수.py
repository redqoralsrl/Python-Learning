#최소 공배수 구하기
num1 = int(input("정수1 입력 : "))
num2 = int(input("정수2 입력 : "))
a = 1
while True:
    if a % num1 == 0 and a % num2 == 0:
        break
    a = a + 1
print("최소 공배수",a)
#구구단 프로그램
import os
while True:
    i = 1
    num = int(input("몇단 출력해줄까?(0을 입력시 구구단 종료): "))
    if num == 0:
        break
    while i < 10:
        print("{0} * {1} = {2}".format(num, i, num*i))
        i = i + 1
    os.system("pause")
    os.system("cls")
#break : 반복 중 강제로 반복문을 빠져 나갈때 사용하는 명령어
#continue : 반복 중 반복문 내 continue의 아래 코드를 수행하지
#않고 조건식으로 올라가게 해준다

#반복 정리
'''
import os
    os.system("pause")
    os.system("cls")
'''
#랜덤변수
import random
print(random.randrange(11))#0~10사이의 수를 랜덤으로 출력
print(random.randrange(10,21))#10에서 20사이의 수를 랜덤으로 출력
NumList = [1,2,3,4,5,6,7,8,9,10]
print(random.choice(NumList))#자료구조형 자료형 내의 원소중 하나를 랜덤으로 선택
print(NumList)
random.shuffle(NumList)#자료 구조형 자료형 내의 원소들을 섞는 함수
print(NumList)