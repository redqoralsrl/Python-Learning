import random
import time
import os
doll = ["피까츄","라이츄","파이리","꼬북이"]
while doll:
    input("""
    ========인형뽑기=======
    <Enter 누를 시 게임시작>
    """)
    print("인형목록")
    print(doll)
    crain = input("돈을 넣으세요")
    select = random.choice(doll)
    print("윙~")
    time.sleep(1)
    print("딸캉~")
    time.sleep(1)
    print("{0}이 뽑혔습니다.".format(select))
    doll.remove(select)
    os.system("pause")
    os.system("cls")
print("인형을모두뽑았네")