jumsu = [95, 50, 60, ["perfect","zero"]]
print(jumsu)
print(jumsu[0])
print(jumsu[0] + jumsu[2])
print(jumsu[3])
print(jumsu[3][1])
print(jumsu[3][1][2])

#'a'문자와 1.2를 인덱싱하시오
a = [1, 2,["Python",['c','b'],[1.2, "itbank", 5.55],5]]
print(a[2][2][1][3])
print(a[2][2][0])

x = [1, 2, 3, 4, 5]
print(x[0:2])
y = "12345"
y = x[:2]
z = x[2:]
print(y)
print(z)

date = [2018, 2019, 2020]
print(str(date[1]) + " Year")

num = [1, 2, 3]
print(num[2])
num[2] = 4
print(num[2])
print(num)

loop = [1,2,3,4,5,6,7,8,9]
loop1 = loop[1::2]
print(loop[::2])
print(loop[::3])
print(loop1)

ex = [1, 2, 3]
print(ex[1:2])
print(ex[1])
ex[1:2] = [4, 5]
print(ex)
ex[:2] = ['d', 'e']
print(ex)