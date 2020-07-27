#기본사용
num = 1
while num <= 3:
    print("num = ",num)
    num = num + 1

#조건문while의 사용
print("어제 드라마 봤어?\n두번 봐라!")
count = 2
while count: #count가 0 되면 실행 안함
    print("재방송을 시청합니다.")
    count = count - 1
print("두번 다 봤어!!")

#예제1
print("열 번 찍어 안 넘어가는 나무가 없다.")
hit = 0
while hit < 10:
    hit = hit + 1
    print("나무를 {0}번 찍었습니다.".format(hit))
print("나무가 넘어갔습니다.")
#정수입력 프로그램 os 사용하기
import os
#system, exit함수 사용하기위해 외부 라이브러리 파일을 가져오는 코드
num = 0
while True:
    print("=======메뉴========")
    print("1. 정수입력\n2. 입력된 정수 출력\n3. 종료")
    choose = int(input("메뉴 선택: "))
    if choose == 1:
        num = int(input("정수입력: "))
    elif choose == 2:
        print("입력된 정수 : ",num)
    else:
        exit(0) #종료되는 방법
    os.system("pause") #프로그램을 잠시 멈춰주는 역할
    os.system("cls") #화면에 출력된 문자를 지워주는 역할

#입력된 정수들의 합과 그 평균을 구하고 0이되면 프로그램을 종료
count = 0
sum = 0
num = 1
while num != 0:
    count = count + 1
    num = int(input("정수입력: "))
    sum = num + sum
count = count - 1
evg = sum / count
print("총합 {0}이며 평균 {1}입니다.".format(sum, round(evg)))

#몬스터 사냥
MonsterHp = 1000
turn = 0
import os
while MonsterHp > 0:
    turn = turn + 1
    print("========={0}턴============".format(turn))
    print("어떤 기술을 사용하시겠습니까?")
    print("1: 기본공격 \t 2: 스킬공격")
    choose = int(input("선택 : "))
    if choose == 1:
        print("몬스터에게 300 데미지를 입혔습니다.")
        MonsterHp = MonsterHp - 300
    elif choose == 2:
        print("몬스터에게 500 데미지를 입혔습니다.")
        MonsterHp = MonsterHp - 500
    print("몬스터 체력 {0}".format(MonsterHp))
    os.system("pause")
    os.system("cls")
print("몬스터가 죽었습니다.")
print("축하드립니다~~")