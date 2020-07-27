#1)
import random
A = 100
B = 100
rou = 0
print("A의 점수는 100, B의 점수는 100")
how = int(input("주사위를 몇 번 던지겠습니까? : "))
while how:
    rou = rou + 1
    how = how - 1
    a = random.randrange(1,7)
    b = random.randrange(1,7)
    print("A의 주사위 : ",a)
    print("B의 주사위 : ",b)
    print(rou,"Round) ",a,b)
    if a > b:
        B = B - a
    elif a < b:
        A = A - b
    else:
        continue
print("A의 점수는 {0}, B의 점수는 {1}".format(A,B))

#2)
import random
play = 9
lot, sam, lot_point, sam_point, turn = 0, 0, 0, 0, 0
while play:
    play = play - 1
    turn = turn + 1
    lot = random.randrange(0,3)
    sam = random.randrange(0,3)
    print("{0}회) 롯데{1} : 삼성{2}".format(turn,lot,sam))
    lot_point = lot_point + lot
    sam_point = sam_point + sam
    if turn == 9 and lot_point == sam_point:
        play = 3
    elif turn > 9:
        if lot_point > sam_point or lot_point < sam_point:
            break
if lot_point > sam_point:
    print("롯데{0} : 삼성{1} 로 롯데가 이겼습니다.".format(lot_point,sam_point))
elif lot_point < sam_point:
    print("롯데{0} : 삼성{1} 로 삼성이 이겼습니다.".format(lot_point,sam_point))
else:
    print("무승부")

#3)
num = int(input("대결횟수: "))
turn = 0
data = {}
while num:
    num = num - 1
    turn = turn + 1
    how = int(input("{0}회차 학교 수 : ".format(turn)))
    while how:
        how = how - 1
        school = input("대학입력 : ")
        data[school] = int(input("술 주량 : "))
        print(school, data[school])
    a = list(data.keys())
    b = list(data.values())
    c = b.index(max(b))
    print(turn,"회차 승리 학교는 ",a[c])
    data.clear()
    a.clear()
    b.clear()
