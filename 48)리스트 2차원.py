apart = [[101,102,103,104],[201,202,203,204],[301,302,303,304]]
b = [1,2,3,4]
print(apart)
print(b)

for i in apart: # i -> y축에 대한 변수
    for j in i:# j -> x축에 대한 변수
        print(j,end=" ")
    print()

for a1,a2,a3,a4 in apart:
    print("{0} {1} {2} {3}".format(a1,a2,a3,a4))

yindex = 0
while yindex < len(apart):
    xindex = 0
    while xindex < len(apart[yindex]):
        print(apart[yindex][xindex],end = " ")
        xindex = xindex + 1
    print()
    yindex = yindex + 1