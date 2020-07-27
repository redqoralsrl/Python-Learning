
#1)
num = 1
data = []
while num !=0:
    num = int(input("정수입력 : "))
    if num == 0:
        break
    else:
        data.append(num)
for i in data:
    print(i, end=" ")
print(sum(data))

#2)
movie = {"물":"인간1","불":"인간2","흙":"인간3","공기":"인간4"}
for i in movie.keys():
    print(i, end=" ")
print("")
for i in movie.items():
    print(i)
for i in movie.keys():
    print(i, end=" ")
print("")
for i in movie.values():
    print(i, end=" ")
print("")
for i in movie:
    print(i,movie[i])