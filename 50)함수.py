def Multi(num):
    num = num * 2 + 1
    return num #Multisum 에 보내서 계산을 하고 다른 곳에 활용할때 num에 넣어준다. 안하면 None으로 나온다.
                #계속해서 값을 사용하려고 고정하는 것
num1 = 10
num2 = 20
num3 = 30
print(num1 * 2 + 1)
print(num2 * 2 + 1)
print(num3 * 2 + 1)
print(Multi(num1)) #번거롭게 반복하는 일을 줄이는데 쓰인다.
print(Multi(num2))
print(Multi(num3))

def MultiSum(num):
    num = num * 2 + 1 #위에 return 값을 안하고 그냥 출력만 하라면 출력을 해준다.
    print(num)
MultiSum(num1)
MultiSum(num2)
MultiSum(num3)

def MultiSum():
    num = int(input("정수입력 : ")) #사용자에게 입력받으려고 할때 사용법
    num = num * 2 + 1
    print(num)
MultiSum()

def EvenCheck(Num):
    if Num % 2 == 0:
        return True
    else:
        return False
if EvenCheck(11) == True:
    print("짝수")
else:
    print("홀수")


def EvenCheck(Num):
    if Num % 2 == 0:
        print("짝수")
    else:
        print("홀수")
EvenCheck(11)
EvenCheck(10)

import math #내장함수 선언하겠다
print(pow(2,3)) #시스템 내장함수

#나중에 궁금하면 파이썬 거북이 모듈을 구글링에 쳐서 해보기