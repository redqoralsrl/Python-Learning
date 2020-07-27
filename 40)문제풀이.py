#break,continue 문제

#1
x = 0
sum = 0
while True:
    x = x + 1
    if x % 3 == 0 and x % 5 == 0:
        sum = sum + x
    elif x % 3 == 0:
        continue
    else:
        sum = sum + x
    if x == 1000:
        break
print(sum)

#2
import os
money = int(input("돈을 넣으세요 : "))
while True:
    print("="*8+"자판기"+"="*8)
    print("콜라 : 1200원\n사이다 : 1200원")
    print("조지아 : 1000원\n컨피던스 : 600원")
    print("종료")
    drink = {"콜라":1200,"사이다":1200,"조지아":1000,"컨피던스":600}
    pick = input("음료를 선택하세요 : ")
    if pick in drink and (money - drink[pick]) > 0:
        money = money - drink[pick]
        print("잔돈 : ", money)
    elif pick == "종료":
        exit(0)
    else:
        print("잘못된 입력이거나 돈이 없습니다.")
    os.system("pause")
    os.system("cls")

#3
import random
wordlist = ["itbank", "hello", "dog", "boy"]
while wordlist != []:
    print(wordlist)
    quiz = random.choice(wordlist)
    print(quiz[0][0])
    word = input("단어를 입력 : ")
    if word in wordlist:
        print("정답입니다.")
        wordlist.remove(word)
    else:
        print("오답입니다.")
print("모두 맞혔습니다!")