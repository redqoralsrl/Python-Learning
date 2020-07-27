name = input("이름 입력 : ")
age = input("나이 입력 : ")
print("이름은 :",name,", 나이는 :",age,"입니다.")
print(type(age))
#int인 정수타입이 아닌 문자로 인식한다 그래서 아래와 같이해야 int다.
old = int(input("나이 입력 : "))
print(type(old))
#차이를 확실히 하려면 아래와 같이 보면 확실하게 이해된다.
firstname = input("성을 입력하세요 : ")
lastname = input("이름을 입력하세요 : ")
print("제 이름은 : ", firstname + lastname,"입니다.")
#str은 문자로 더해지지가 않고 차곡차곡 붙는다. 하지만 int경우 
#수는 더해진다.
num = input("숫자 하나 입력: ")
num1 = input("숫자 하나더 적어 : ")
print(num+num1)#2524로 나온다 즉 str이라는 증거다!
# int -> 정수 float -> 실수 str -> 문자 bool -> 참/거짓