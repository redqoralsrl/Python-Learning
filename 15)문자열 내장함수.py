#count = 문자열의 개수
Str = "Hello Python"
print(Str.count('o'))
print(Str.count('l'))
#find = 해당 문자의 인덱스 번호 반환
print(Str.find('l'))#제일 처음 만나는 번호를 띄워준다
print(Str.find('P'))
print(Str.find('a'))#없으면 -1로 리턴된다
#join = 문자열 안에 원하는 문자를 넣어준다
a = ","
print(a.join("abcd"))
#upper = 문자열을 전체 대문자로 변환
print(Str.upper())
#lower = 문자열을 전체 소문자로 변환
print(Str.lower())
#lstrip = 문자열의 왼쪽 공백을 제거
a = "   Hello   "
print(a.lstrip())
#rstrip = 문자열의 오른쪽 공백을 제거
print(a.rstrip())
#strip = 문자열의 양쪽 공백 제거
print(a.strip())
#replace = 특정 문자열을 교체
Say = "I love Pusan"
print(Say.replace("P","B"))
#split = 문자열을 나누는 함수
print(Say.split())
Say = "I lo:ve Pusan"
print(Say.split(':'))#콜론 기준으로 나눈다
FilePath = "C:/Users/Administrator/Desktop"
print(FilePath.split('/'))
#startswitch = 시작 문자열 확인
#endswitch = 마지막 문자열 확인
Say = "Life is too short"
print(Say.startswith("Life"))
print(Say.endswith("short"))
print(Say.endswith("Short"))
#capitalize = 첫번째 알파벳을 대문자로 변환
a = "food"
print(a.capitalize())
#center = 문자열 중앙 정렬
#ljust = 문자열 왼쪽 정렬
#rjust = 문자열 오른족 정렬
a = "백민기"
print(a.center(10),"Hello")
print(a.ljust(10),"Hello")
print(a.rjust(10),"Hello")

#isdigit = 함수는 문자열이 숫자인지 아닌지를 True,False로 리턴한다
#isalpha = 함수는 문자열이 문자인지 아닌지를 True,False로 리턴한다
a1 = '111'
a2 = '백민기'
a3 = 'Hi'
print(a1.isdigit())
print(a1.isalpha())
print(a2.isdigit())
print(a2.isalpha())
print(a3.isdigit())
print(a3.isalpha())

import math
print(math.gcd(12,18)) #최대공약수

#최소공배수 = a*b // gcd(a,b)최대공약수로 나눈다
