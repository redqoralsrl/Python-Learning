#3)
su = 0
for i in range(1, 1000, 1):
    if i % 3 == 0 or i % 5 == 0:
        su = su + i
print(su)

#리스트표현식으로 구현
print([i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0]) # 1 ~ 999까지 3, 5의 배수 리스트
print(sum([i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0]))

#4)
name = "정예현,강민석,나혜린,권효정,김기주,김도연,나혜린,나혜린,박경민,박명규,박정훈,박지민,배유정,신재욱,이태경,임도영,하준봉"
name = list(name.split(","))
park, ei = 0, 0
for i in name:
    if i[0] == "박":
        park += 1
    elif i[0] == "이":
        ei += 1
print("박씨 : {0}, 이씨 : {1}".format(park,ei))
print()
park = 0
for i in name:
    if i == "나혜린":
        park += 1
print("나혜린 : {0}".format(park))
name = list(set(name))
print(name)
name.sort()
print(name)

#5)
num = int(input("10진정수입력:"))
print(bin(num))