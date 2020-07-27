a = "Life is too short, You need Python"
b = a[0:4]
print(b)
print(a[3:-9])
print(a[:13])

address = "부산광역시 수영구 민락동"
si = address[:5]
goo = address[6:8]
dong = address[-3:]
print("시 : "+si+", 구 : "+goo+", 동 : "+dong)

say = "I love Pusan"
print(say[:7]+"B"+say[-4:])

money = "부산 112 2014 9018 01입금 = 10억원"
bank = money[:2]
Gejoua = money[3:-9]
Won = money[-4:]
print("은행 : "+bank+", 계좌번호 : "+Gejoua+", 금액 : "+Won)

a = "1 + 1 = 3"
b = "1011111101101 -> 23,137"
c = "파이썬은 저급언어이며 컴파일러방식이다."
d = "파이썬은 프로그래밍 언어 중 어려운 편에 속한다."
print("a = "+a[:8]+"2")
print("b = "+b[:17]+str(int(0b1011111101101)))
print("c = "+c[:5]+"고"+c[6:])
print("d = "+d[:16]+"쉬"+d[-9:])