#1번문제
a = [10, 22, 33, 44, 50]
a[1:4] = [20, 30, 40]
print(a)
del a[2]
print(a)
#2번문제
b = [21, 9, 12, 17, 9, 3, 27, 32, 1]
b[-2] = 19
b[2:4] = [22, 7]
print(b)
second_list = sum(b[1::2])
first_list = sum(b[::2])
print("짝수번째 합은 {0}이고 홀수번째 합은 {1}".format(second_list,first_list))
#3번문제
c = [5, 9, 1, 2, 10, 15]
print(max(c))
print(min(c))