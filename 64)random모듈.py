# random 모듈
import random # random을 선언

print("1~10중에 랜덤값: ",random.randint(1,10))

print(random.randrange(10,21))#10에서 20사이의 수를 랜덤으로 출력

NumList = [1,2,3,4,5,6,7,8,9,10]
print(random.choice(NumList))#자료구조형 자료형 내의 원소중 하나를 랜덤으로 선택
print(NumList)
random.shuffle(NumList)#자료 구조형 자료형 내의 원소들을 섞는 함수
print(NumList)

##################

import random as r
import turtle as t

t.shape("turtle")

for i in range(10):
    distance = r.randint(10,20)
    angle = r.randint(1, 360)
    t.forward(distance)
    t.right(angle)
