#1)
sum = 0
count = 1
num1 = int(input("숫자 입력: "))
while count <= num1:
    sum = sum + count
    count = count + 1
print(sum)
#2)
do = 1
while do <= 10:
    print("Hello, Python")
    do = do + 1
#3)
num2 = 1
sum = 0
while num2 != 0:
    num2 = int(input("정수 입력:"))
    sum = sum + num2
print(sum)
#4)
what = int(input("정수를 입력하세요 : "))
while what:
    print(what % 10, end="")
    what = what // 10
print("")
#5)
num1 = int(input("정수를 입력하세요 : "))
count = 0
while count < 4:
    count = count + 1
    print(num1 * count, end =" ")
print("")

