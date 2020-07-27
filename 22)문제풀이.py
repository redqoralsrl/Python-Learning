#1번문제
movie = [input(),input(),input(),input(),input(),input()]
print(movie)
print(movie[0:4])
print(movie[0],movie[1])
print(movie[3:5])
eve = movie[0:2] + movie[2:4]
print(eve)
#2번문제
a = [3, 5, 2, 6, 1, 4]
a.sort()
a.reverse()
print(a)

b = [input(), input(), input(), input(), input()]
c = b
print(c)
#3번문제
a = [3, 5, 7, 1, 4]
to = sum(a) / len(a)
print(to)
a.append(7)
too = sum(a) / len(a)
print(too)