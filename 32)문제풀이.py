#1번
num = int(input("숫자 입력 : "))
if num % 5 == 0:
    print("5의 배수입니다.")
else:
    print("5의 배수가 아닙니다.")
#2번
num1 = int(input("숫자입력 : "))
if num1 % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
#3번
num2 = int(input("숫자 입력 : "))
num3 = int(input("숫자 입력 : "))
if num2 % num3 == 0:
    print("{0}은(는) {1}의 배수입니다.".format(num2,num3))
else:
    print("관련 없습니다.")
#4번
num4 = int(input("숫자 입력 : "))
num5 = int(input("숫자 입력 : "))
if num4 >= num5:
    if num4 % 2 == 0:
        print("큰 수가 짝수입니다.")
    else:
        print("큰 수가 짝수가 아닙니다.")
if num4 < num5:
    if num5 % 2 == 0:
        print("큰 수가 짝수입니다.")
    else:
        print("큰 수가 짝수가 아닙니다.")
#5번
num6 = int(input("숫자 입력 : "))
num7 = int(input("숫자 입력 : "))
su = num6 + num7
if su % 2 == 0:
    if su % 3 == 0:
        print(su)
    else:
        print("아닙니다.")
else:
    print("아닙니다.")
#6번
num8 = int(input("숫자 입력 : "))
go = abs(num8)
print("입력한 {0}의 절대값은 {1}입니다.".format(num8,go))