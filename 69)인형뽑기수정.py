import os
import random
import time
doll = ["파이리","꼬부기","라이츄",1,1,1,1,1,1,1,1]
while True:
    input("""
    ========인형뽑기========
    Enter 누를 시 게임시작함
    """)
    print("인형목록")
    print(doll[:2])
    coin = int(input("""
    1판 - 1000원(1)
    5판 - 4000원(2)
    10판 - 8000원(3)
    종료 - (4)
    """))
    if coin == 4:
        print("다음에도 이용해주세요!")
        exit(0)
    if coin == 1:
        count = 1
    elif coin == 2:
        count = 5
    elif coin == 3:
        count = 10
    for i in range(1, count+1, 1):
        select = random.choice(doll)
        print("윙~~")
        time.sleep(2)
        print("철컹")
        time.sleep(2)
        if select == 1:
            print("꽝 ㅜㅜ")
        else:
            print(select,"가 잡혔다!")
        doll.remove(select)
        os.system("pause")
    os.system("cls")