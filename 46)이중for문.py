for i in range(3):# 0~2 i==0
    print("===={0}학년====".format(i+1))#0 +1 => 1
    for j in range(10):#0~11 j==0
        print("=={0}학년=={1}반==".format(i+1,j+1))
print("\n")

for i in range(1, 4, 1):
    print("===={0}학년====".format(i))
    for j in range(1, 11, 1):
        print("=={0}학년=={1}반==".format(i,j))
print("\n")

