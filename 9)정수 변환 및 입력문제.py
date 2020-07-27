#type을 변환시켜보자.
num1 = input("첫번째 정수 입력: ")
num2 = input("두번째 정수 입력: ")
print("합계는 : ",int(num1)+int(num2))
#이번엔 실수로 바꿔보자.
a = float(input("첫번째 실수를 입력 : "))
b = float(input("두번째 실수를 입력 : "))
print("합계는 ",a+b)
#round 함수는 실수를 원하는 자리까지 나오게 가능하게 만든다.
r = 3.14145293123
print(round(r,3))#세번째 자리까지나오니 4번째에서 반올림한다
result = round(3.6562)#이렇게 하면 정수로 반올림 하니 4가나온다
print(result)