a = ","
print(a.join("abcd")) # a,b,c,d

b = "find"
print(b.upper()) # FIND

c = "FIND"
print(c.lower()) # find

d = "   Hello   "
print(d.lstrip()) # 왼쪽공백제거Hello
print(d.rstrip()) #     Hello오른쪽공백제거
print(d.strip()) # 양쪽공백제거

say = "I love Pusan"
print(say.replace("P","B")) # 특정 문자 교체

e = "nice shoot"
print(e.capitalize()) # 문자 첫글자를 대문자로 교체

f = "백민기"
print(f.center(10),"Hello") # 문자열 중앙정렬
print(f.ljust(10),"Hello") # 문자열 왼쪽정렬
print(f.rjust(10),"Hello") # 문자열 오른쪽정렬

a = [1, 2, 3, 4, 5] # 리스트 선언
print(sum(a)) # 안에 리스트 다 더하기
print(max(a)) # 최대 값 추출
print(min(a)) # 최소 값 추출
print(sum(a[:3])) # 처음부터 지정된 곳까지 더해라
print(sum(a[::2])) # 2씩증가하면서 더해라

del a[3] # 4 지우기
print(a)
a[:2] = [6,7] # 0자리부터 2자리까지 지우고 6, 7값 저장
print(a)
a[1] = 8 # 1자리에 8로 변경
print(a)

print(len(a)) # 리스트 안에 값을 개수로 바꿔준다

x = [1, 2, 3]
x.append(4) # 리스트에 추가
print(x)
x.append([5,6]) # 리스트에 또 다른 리스트 만들기
print(x)
#[1,2,3,4,[5,6]]이 출력된다. 5를 추출하려면
print(x[4][0])

y = [4, 6, 2, 9] # 정렬해준다
y.sort()
print(y)

z = ['a', 'c', 'b']
z.reverse() # b c a 로 뒤집어 지지만 만약 역순정렬은 정렬한뒤 뒤집는다
print(z)
t = ['a', 'c', 'b']
t.sort()
t.reverse() # c b a 로 잘 뒤집어진다
print(t)

u = [1, 2, 3]
u.insert(0, 4) # 리스트에 삽입하는 거지만 왼쪽은 위치 오른쪽은 값을 적는 단점이 있다
print(u)
u.insert(5, 4)
print(u)

n = [1, 2, 3]
n.remove(2) # 삭제하는 것이다
print(n)

e = [1, 2, 3]
e.pop() # 제일 뒤를 끄집어낸다 혹은 삭제
print(e)
e.pop(1) # 1번 자리에 수를 끄집어낸다 혹은 삭제
print(e)

w = [1, 2, 3]
w.extend([4,5]) # 여러개를 추가할때 효율적이다
print(w)
