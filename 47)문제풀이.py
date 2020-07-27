#1)
apart = [[101,102,103,104],[201,202,203,204],[301,302,303,304]]
floor = 0
for i in range(0,3,1):
    floor = floor + 1
    for j in range(0,4,1):
        print("{0}호 부착완료".format(apart[i][j]))
    print("{0}층에 모두 부착완료".format(floor))
print()

#2)
num = int(input("입력 : "))
for i in range(1, num+1, 1):
    for j in range(1, i+1, 1):
        print("*",end="")
    print()

#3)
num = int(input("입력 : "))
for i in range(1, num+1, 1):
    for j in range(num-i, 0, -1):
        print(" ",end="")
    for k in range(1, i+1, 1):
        print("*",end="")
    print()

#4)
num = int(input("입력 : "))
for i in range(num, 0, -1):
    for j in range(num-i, 0, -1):
        print(" ",end="")
    for k in range(1, i+1, 1):
        print("*",end="")
    print()

#5)
num = int(input("입력 : "))
for i in range(1, num+1, 1):
    for j in range(num-i, 0, -1):
        print(" ",end="")
    for k in range(1, i*2, 1):
        print("*",end="")
    print()

#6)
num = int(input("입력 : "))
for i in range(num, 0, -1):
    for k in range(num-i, 0, -1):
        print(" ",end="")
    for j in range(2*i-1, 0, -1):
        print("*",end="")
    print()

#7)
num = int(input("입력 : "))
for i in range(num, 0, -1):
    for k in range(num-i, 0, -1):
        print(" ",end="")
    for j in range(2*i-1, 0, -1):
        print(i,end="")
    print()