#1)
# 딕셔너리에 자신이 좋아하는 영어단어를 key에 넣고 그 단어의 뜻을 value에
# 넣은 dic이라는 딕셔너리 변수를 생성 후 find_word에 인자로 넘겨 주면 함수
# key를 이용하여 value를 찾는 find_word 함수를 만드시오
def find_word(dic):
    i = input("찾는 단어 입력: ")
    if i in dic:
        print(i,":",dic[i])
    else:
        print("해당 단어가 없습니다.")
dic = {"apple":"사과","banana":"바나나"}
find_word(dic)

#2)
import math
def FileSize(num):
    num = num.split()
    a = int(num[0])
    b = num[1].upper()
    if b == "T":
        b = 4
    elif b == "G":
        b = 3
    elif b == "M":
        b = 2
    elif b == "K":
        b = 1
    else:
        print("없습니다.")
        return
    total = round(a * math.pow(1024,b))
    total = format(total,",")
    print("출력 : {0}byte 입니다.".format(total))
num = input("입력 : ")
FileSize(num)

#3)
def LoginLoad(account,uid,upw):
    if uid in account:
        if account[uid] == upw:
            print("[{0}]님이 로그인하였습니다.".format(uid))
        else:
            print("비밀번호가 다릅니다.")
    else:
        print("아이디가 없습니다.")
import os
account = {}
while True:
    os.system("cls")
    print("==회원관리==")
    print("1.회원가입")
    print("2.로그인")
    print("3.종료")
    num = int(input("어떤 기능을 사용하시겠습니까? : "))
    if num == 1:
        print("==회원가입==")
        uid = input("아이디 : ")
        pwd = input("비번 : ")
        account[uid] = pwd
        os.system("pause")
        continue
    elif num == 2:
        print("==로그인==")
        uid = input("아이디 : ")
        pwd = input("비번 : ")
        LoginLoad(account,uid,pwd)
        os.system("pause")
        continue
    elif num == 3:
        print("==종료합니다==")
        break
    else:
        print("해당 기능이 없습니다.")
        os.system("pause")
        continue

#4)
def avg_score(**Train):
    a = Train.values()
    avg = sum(a) / len(a)
    print(avg)
avg_score(kor=98,eng=100,mat=87)

#5)
def My_Avg(*args):
    return sum(args)/len(args)
def My_Max(*args):
    args = list(args)
    args.sort()
    args.reverse()
    return args[0]
print("평균 : ",My_Avg(55,93,58,43))
print("최대값 : ",My_Max(55,93,58,43))

#6)
import random
def LottoRand():
    count = 0
    Lotto = []
    while len(Lotto) < 6:
        Lotto.append(random.randrange(1,11))
        Lotto = list(set(Lotto))
    me = []
    while len(me) < 6:
        me.append(int(input("입력: ")))
        me = list(set(me))
    for i in me:
        if i in Lotto:
            count = count + 1
    print(Lotto)
    print(me)
    print(count)
LottoRand()