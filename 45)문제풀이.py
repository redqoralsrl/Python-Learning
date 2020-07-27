#1)
num = int(input("정수입력 : "))
for i in range(num, 0, -1):
    print(i, end=" ")
print("")

#2)
for i in range(1, 5, 1):
    number = int(input("양의정수를 입력하시오 : "))
    if number == 0:
        print("0은 0입니다.")
    elif number < 0:
        print("잘못된 입력입니다.")
    else:
        if number % 2 == 0:
            print(number,"은 짝수입니다.")
        else:
            print(number,"은 홀수입니다.")

#3)
x = 1
money = 0
for i in range(1, 31, 1):
    money = money + x
    x = x * 2
print(money)

#4)
num1 = int(input("정수 입력: "))
check = True
for i in range(2, num1, 1):
    if num1 % i == 0:
        check = False
        break
if check == True:
    print("소수입니다.")
else:
    print("소수가 아닙니다.")

#5)
x = []
first = int(input("정수입력 : "))
second = int(input("정수입력 : "))
if first > second:
    tmp = first
    first = second
    second = tmp
for i in range(1, second+1, 1):
    if first % i == 0 and second % i == 0:
        print(i, end=" ")
        x.append(i)
print(max(x))