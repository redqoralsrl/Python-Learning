kg = "KG ITBank"
address = "부산광역시 수영구 민락동"
start = 10
end = 20
name = "백민기"
age = 25
Phone = "010-5879-3725"

print("☆ "*10+kg+" ☆"*10)
print("파이썬 강의 : {0}시 ~ {1}시".format(start,end))
print("본인 이름 : {0}\n주소 : {1}".format(name,address))
print("☆ "*10+kg+" ☆"*10)

kor = float(input("국어 점수를 입력 : "))
eng = float(input("영어 점수를 입력 : "))
mat = float(input("수학 점수를 입력 : "))
sum = kor + eng + mat
print("국어 점수 {0}점, 영어 점수 {1}점, 수학 점수 {2}점 입니다.".format(kor,eng,mat))
print("총 합점은 {0}점이며, 평균은 {1}점 입니다.".format((kor+eng+mat),sum/3))

a = int(input("1번째 수를 입력 : "))
b = int(input("2번째 수를 입력 : "))
print("{0}의 {1}제곱은 {2}이며, {0}을 {1}로 나누면 몫은 {3}이며 나머지는 {4}입니다.".format(a,b,a**b,a//b,a%b))

time = 3
count = int(input("가야할 지하철역 수를 입력 : "))
print("도착역까지 총 {0}분 걸립니다.".format(time*count))