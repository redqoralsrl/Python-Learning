print("I eat %d cakes"%3)
print("I eat %s cakes"%"two")
print("I eat %f cakes"%3.5)
print("I eat %x cakes"%0xad)

num = 3
print("I eat %s cakes"%num)
print("%10s %5s"%("name","age"))

a = 3.14159265358979
print("%.3f"%a)
print("%.4f"%a)

#고급 포매팅을 사용해보자.
print("I have a {0}".format("Pen"))
print("I have a {0}, I have a Apple, Apple{1}".format("Pen","note"))
a = "good"
b = "bad"
print("I think {0}, you think {1}, now {0}".format(a,b))

print("Wow, {a} job! you look so {b}".format(a="good",b="nice"))
