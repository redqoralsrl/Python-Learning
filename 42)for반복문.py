#
count = [0,1,2,3]
for num in count:
    print("num = ",num)
#
count = [1,2,3,4]
print("숫자세기")
for i in count:
    print(i, end=" ")
print("")
count.reverse()
for i in count:
    print(i, end=" ")
print("")
#
jumsu = (90, 60, 88, 58, 70, 100)
number = 1
for i in jumsu:
    if i >= 80:
        print("{0}번째 학생 : 합격".format(number))
    else:
        print("{0}번째 학생 : 불합격".format(number))
    number = number + 1
#
people = {"송새봄" : 29, "송여름" : 16, "송가을" : 32,"송겨울" : 5}
minor = []
adult = []
for i in people:
    if people[i] < 20:
        print(i,"님",people[i],"살 ==> 미성년자")
        minor.append(i)
    else:
        print(i,"님",people[i],"살 ==> 성인")
        adult.append(i)
print("미성년자 : ",minor)
print("성인 : ",adult)
#
Value = [(1,2),(3,4),(5,6)]
for (a,b) in Value:
    print("{0} + {1} = {2}".format(a,b,a+b))
#
film = {"작품상":"택시운전사","우수상":"아이캔스피크",
"남우주연상":"송강호","여우주연상":"나문희"}
for x in film.keys():
    print(x)
for x in film.values():
    print(x)
for x in film.items():
    print(x)
for x,y in film.items():
    print(x,":",y)