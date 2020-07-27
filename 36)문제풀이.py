
#1)
kor = int(input("국어 점수 : "))
eng = int(input("영어 점수 : "))
mat = int(input("수학 점수 : "))
evg = (kor + eng + mat) / 3
if evg >= 90:
    print("A")
elif evg >= 80:
    print("B")
elif evg >= 70:
    print("C")
elif evg >= 60:
    print("D")
else:
    print("F")

#2)
Point = input("결과를 입력:")
A = Point.upper().count("A")
B = Point.upper().count("B")
print(A, B)
if A > B:
    print("우승자는 A입니다.")
elif B > A:
    print("우승자는 B입니다.")
else:
    print("무승부입니다.")

#3)
price = 0
print("====북촌 손만두 메뉴====\n\t새우만두 1개 : 1000원")
count = int(input("만두 몇개를 시키겠습니까?: "))
if count >= 100:
    price = (1000 * count) * 0.75
    cash = price * 0.9
elif count >= 10:
    price = (1000 * count) * 0.85
    cash = price * 0.9
else:
    price = 1000 * count
    cash = price * 0.9
print("가격 : {0}원, 현금결제가 : {1}원".format(int(price), int(cash)))

#4)
birth = input("생년월일 6자리 : ")
behind = int(input("주민번호 뒷자리 첫글자 : "))
if behind == 1:
    who = "남자"
    year = 1900 + int(birth[:2])
    old = 2018 - year + 1
elif behind == 2:
    who = "여자"
    year = 1900 + int(birth[:2])
    old = 2018 - year + 1
elif behind == 3:
    who = "남자"
    year = 2000 + int(birth[:2])
    old = 2018 - year + 1
elif behind == 4:
    who = "여자"
    year = 2000 + int(birth[:2])
    old = 2018 - year + 1
print("성별정보가 {0}이므로 {1}년생, {2}살입니다.".format(behind,year,old))

park = int(input("주차한 시간은 몇분인가요? : "))
time = park - 30
a = time % 10
b = time // 10
if park <= 30:
    price = 1000
elif park > 30:
    if time % 10 == 0:
        price = 1000 + 500 * b
    else:
        price = 1000 + 500 * b + 500
print(price)