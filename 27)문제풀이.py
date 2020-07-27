mart = {"다이제" : 1000, "메로나" : 500, "코카콜라" : 700, "츄파츕스" : 500}
#1번문제
menu = tuple(mart.keys())
print(menu)
#2번문제
price = sum(mart.values())
print(price)
#3번문제
object1 = input("제품 이름을 입력 : ")
mart[object1] = int(input("가격을 입력 : "))
print(mart)
object2 = input("제품 이름을 입력 : ")
mart[object2] = int(input("가격을 입력 : "))
print(mart)