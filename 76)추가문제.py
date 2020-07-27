#1)
su = 0
for i in range(1, 10001, 1):
    su = su + str(i).count("8")
print(su)
#2)
def median():
    num = int(input("입력할 숫자 갯수 : "))
    lis = []
    if num % 2 == 0:
        print('홀수개만 입력하라고 ㅡㅡ')
        exit(0)
    for i in range(1, num+1, 1):
        a = int(input("숫자 입력: "))
        lis.append(a)
    c = (len(lis)+1)//2 - 1
    lis.sort()
    print(lis[c])
median()