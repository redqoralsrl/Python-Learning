#if문제2
print("세 수(년, 월, 일)을 입력하시오 : ")
year = input("년: ")
month = input("월: ")
day = input("일: ")
total = year - month + day
if total == 0:
    print("대박")
else:
    print("그럭저럭")
#if문제3
station = int(input("정거장 수 : "))
time = 0
if station < 10:
    time = station * 2
else:
    time = station * 4
if time > 60:
    hour = time // 60
    minute = time % 60
    print("총 소요 시간은 {0}시간 {1}분입니다.".format(hour,minute))
else:
    print("총 소요 시간은 {0}분 입니다.".format(time))
