#1)
import time
import random
count = 3
while True:
    print("구구단을 외자!",end=" ")
    time.sleep(2)
    print("구구단을 외자!")
    time.sleep(2)
    start = time.time()
    for i in range(1,4,1):
        a = random.randint(1,9)
        b = random.randint(1,9)
        print("{0} x {1}".format(a,b),end=" ")
        c = int(input(" = "))
        if c == (a*b):
            print('맞췃네')
        else:
            print('아쉽네')
    end = time.time()
    break
print("걸린시간: ",round(end - start))

#2)
import time
import random
count = 5
input("""
    게임을 시작하시려면 Enter키를 누르십시오
    """)
point = 0
start = time.time()
word = ["money", "hobby", "language", "do", "get"]
while count:
    a = random.choice(word)
    print("=========")
    print("점수 : {0}".format(point))
    print(a)
    c = input()
    if c == a:
        print("맞췃습니다.+1점")
        point += 1
        word.remove(a)
    else:
        print("틀렸습니다.")
    count -= 1
end = time.time()
print("총 걸린 시간 : {0}".format(round(end-start)))
print("점수 : ",point)

#3)
import random
import time
print("가위 바위 보 !! 게임")
input("""
Enter 누르면 시작
""")
me_point = 0
computer_point = 0
a = ["가위", "바위", "보"]
while True:
    b = random.choice(a)
    print("가위!")
    time.sleep(1.5)
    print("바위!")
    c = input("입력: ")
    print(b)
    if c == "가위":
        if b == "가위":
            print("무승부")
        elif b == "바위":
            print("졌어 ㅜㅜ")
            computer_point += 1
        elif b == "보":
            print("이겼다!")
            me_point += 1
    if c == "바위":
        if b == "바위":
            print("무승부")
        elif b == "보":
            print("졌어 ㅜㅜ")
            computer_point += 1
        elif b == "가위":
            print("이겼다!")
            me_point += 1
    if c == "보":
        if b == "보":
            print("무승부")
        elif b == "가위":
            print("졌어 ㅜㅜ")
            computer_point += 1
        elif b == "바위":
            print("이겼다!")
            me_point += 1
    if me_point==3 or computer_point == 3:
        break
if me_point > computer_point:
    print("내가이겼다!")
else:
    print("내가 졌다....")

#4)
import random
import os
while True:
    turn = 0
    guess = random.randint(1,100)
    while True:
        turn += 1
        print("====UpDown====")
        print("===={0}====".format(turn))
        print("1부터 100까지 고르시오.")
        num = int(input("정수를 입력하시오 : "))
        if num == guess:
            print("정답입니다.")
            break
        elif num > guess:
            print("Down")
        else:
            print("Up")
        os.system("pause")
        os.system("cls")
    print("맞혔습니다. {0}턴씩이나?".format(turn))
    now = input("종료 하시겠습니까? y/n :")
    if now == 'y':
        exit(0)
    else:
        continue
