# time 모듈 : 시간에 관련된 모듈, time 함수를 이용해 시간을 잴 수 있다
import time

# 유닉스 타임 : 1970년 1월 1일 0시 0분
# time.time() : 유닉스 타임부터 현재까지 몇 초가 지났는가 리턴
# print(time.time())
print("안녕")
# time.sleep() : 일정한 시간을 두고 코드를 실행
# time.sleep(3)
# print("이것이 슬립이다.")
time.sleep(3)
print("이것이 슬립이다.")

##########################

import time
print(time.time())
time.sleep(3)

import time as t # time을 t로 할꺼야
print(t.localtime(t.time()))

##########################

# localtime : 연도, 월, 일, 시, 분, 초의 형태로 바꿔주는 함수
print(time.localtime(time.time()))

##########################

import time

print("\n==time 함수를 이용한 스톱워치==")
input("엔터를 누르고 3초를 마음속으로 세시오")
start = time.time() # 시작시간 저장

input("3초가 되면 다시 엔터를 누르세요")
end = time.time() # 끝나는 시간 저장

result = end - start

print("걸린시간 : %.2f"%result)
print("오차 : %.2f"%abs(result-3))
