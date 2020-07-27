time = int(input("현재 시간 : "))
if time >= 14:
    print("집에 가자~")
else:
    print("공부합시다 ㅜㅜ")

print("="*30)
age = int(input("당신의 나이를 입력하세요 : "))
if age > 19:
    print("당신은 성인",end="")
else:
    print("당신은 미성년자",end="")
print("입니다.")

print("="*30)
print("오늘도 지각이다... 대중교통을 탈까? 택시를 탈까?")
money = input("택시 탈 돈을 가지고 있는가? [y/n] :")
if money == 'n':
    print("어쩔 수 없지 대중교통이다\n 지하철, 버스 중 뭘 타지?")
    time = input("출근 시간인가? [y/n] : ")
    if time == 'y':
        print("지하철 타야겠다!")
    else :
        print("버스타야겠다!")
else:
    print("인생 모있나 택시로 Flex해보리기")

print("="*30)
se = input("당신의 성별은 [남/여]?: ")
age = int(input("당신의 나이는 ?: "))
if se == "남" and age >=19:
    print("입영대상자 입니다.")
if se == "여" or age < 19:
    print("입영대상자가 아닙니다.")