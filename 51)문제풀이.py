
#1)
# 1-1)
# 정수 하나를 전달받아 1부터 입력 받은 수 까지의 누적 합계를 구하는 함수를 구하시오
# (매개변수(입력값)는 있고 반환값(출력값)이 없는 함수)
def SumTotal(num):
    sum = 0
    for i in range(1, num+1, 1):
        sum += i
    return sum
num = int(input("입력 : "))
print("{0}~{1}의 총합은 {2}".format(1,num,SumTotal(num)))

# 1-2)
# 정수 하나를 전달 받아 해당 정수가 3의 배수인지 출력해주는  함수를 만드시오
# (매개변수(입력값)는 있고 반환값(출력값)이 없는 함수)
def ThreeWhat(num):
    if num % 3 == 0:
        return "3의 배수입니다."
    else:
        return "3의 배수가 아닙니다."
num = int(input("입력 : "))
print("{0}은 {1}".format(num,ThreeWhat(num)))

# 1-3)
# 두 수를 입력 받아 더 큰 수를 return 하는 함수를 만드시오
# (매개변수(입력값)는 있고 반환값(출력값)이 있는 함수)
def WhatBest(num,num1):
    if num > num1:
        return num
    else:
        return num1
num = int(input("입력 : "))
num1 = int(input("입력 : "))
print("입력한 {0},{1}중 최대값은 {2}입니다.".format(num,num1,WhatBest(num,num1)))

# 1-4)
# 정수 하나를 입력 받아 절대값을 구하는 함수를 만드시오
# (매개변수(입력값)와 반환값(출력값)이 없는 함수)
def Madeabs(num):
    if num < 0:
        num = - num # 단 abs는 함수이므로 함수를 만드는 건데 함수를 쓰면 왜 만드는 건지 모른다
        return num
    else:
        return num
num = int(input("입력 : "))
print("입력한 {0}의 절대값은 {1}입니다.".format(num,Madeabs(num)))

#2)
# 자신의 이름 전체를 영어로 입력 받고 '성'과 '이름'을 바꾸는 함수를 만들어
# 해당 함수를 통해 바뀐 영문 이름을 출력하시오
def SplitName(name):
    name = name.split()
    print("성은 {0}이고 이름은 {1}입니다.".format(name[0],name[1]))
name = input("이름을 입력")
SplitName(name)

#3)
# numlist 리스트에 정수를 5개 입력 받고 5보다 큰 수만 result 리스트에
# 추가하는 함수를 만드시오
def FiveOnly(numlist):
    result = []
    for i in numlist:
        if i > 5:
            result.append(i)
    return result
numlist=[]
for i in range(1,6,1):
    numlist.append(int(input("입력 : ")))
print("5보다 큰 수는 {0}".format(FiveOnly(numlist)))

#4)
# 숫자를 입력 받고 그 수를 거꾸로 반환하는 함수를 만드시오
# 반환형이 없고 정수형 변수 x를 매개변수로 하는 Reverse 함수 선언
# While문을 이용하여 입력 받은 숫자를 거꾸로 뒤집어서 출력하는 함수
# 선언 %와 // 연산자 사용
def Reverse(num):
    total = 0
    while True:#234
        total = total + num % 10
        num = num // 10
        if num == 0:
            break
        total = total * 10
    return total
num = int(input("입력 : "))
print("{0}을 뒤집으면 {1}입니다.".format(num,Reverse(num)))

#5)
# 두 수를 입력 받아 그 두 수로 사칙연산을 하는 함수 네 개를 만드시오
# sum, sub, mul, divi 함수를 선언하고 while 반복문과 if를 이용하여
# 한번 실행 후 다시 다른 수를 입력 받을 수 있도록 만드시오
def sum(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def divi(a,b):
    return a / b
import os
while True:
    print("="*8,"계산기","="*8)
    a = int(input("입력 1: "))
    b = int(input("입력 2: "))
    c = int(input("계산할 방식을 선택 \n1.더하기\n2.뺄셈\n3.곱하기\n4.나누기\n0.종료: "))
    if c == 1:
        print("{0}+{1}={2}".format(a,b,sum(a,b)))
    elif c == 2:
        print("{0}-{1}={2}".format(a,b,sub(a,b)))
    elif c == 3:
        print("{0}*{1}={2}".format(a,b,mul(a,b)))
    elif c == 4:
        print("{0}/{1}={2}".format(a,b,divi(a,b)))
    elif c == 0:
        break
    else:
        print("잘못된 선택입니다.")
    os.system("pause")
    os.system("cls")