#1번
a = set([1,2,3,4,5,6])
b = set([4,5,6,7,8,9])
c = set([5,6,7,8,9,10])
l = tuple(a & b & c)
print(l)
U = tuple(a | b | c)
print(U)
D = tuple(a - b - c)
print(D)

#2번
a = [1,1,5,5,4,3,6,7,2,1,5,5,8,5]
a = list(set(a))
print(a)

#3번
d = set([1,2,3,4,5,6])
e = set([4,5,6,7,8,9])
f = set([5,6,7,8,9,10])
e.remove(4)
e.remove(5)
f.remove(5)
e.update([1,2])
print(d - e - f)