#백민기 25 1.0 1.0
#박소희 21 0.8 0.8
#이선영 28 1.0 1.0
#정유진 20 1.0 1.0
first_per = [input("이름입력 : "), int(input("나이입력 : ")), float(input("왼쪽눈 시력: ")), float(input("오른쪽눈 시력: "))]
second_per = [input("이름입력 : "), int(input("나이입력 : ")), float(input("왼쪽눈 시력: ")), float(input("오른쪽눈 시력: "))]
third_per = [input("이름입력 : "), int(input("나이입력 : ")), float(input("왼쪽눈 시력: ")), float(input("오른쪽눈 시력: "))]
forth_per = [input("이름입력 : "), int(input("나이입력 : ")), float(input("왼쪽눈 시력: ")), float(input("오른쪽눈 시력: "))]
old_avg = (first_per[1] + second_per[1] + third_per[1] + forth_per[1]) / 4
left_eye = (first_per[2] + second_per[2] + third_per[2] + forth_per[2]) / 4
right_eye =  (first_per[3] + second_per[3] + third_per[3] + forth_per[3]) / 4
print(old_avg)
print(first_per)
print(second_per)
print(third_per)
print(forth_per)
print("평균나이는 {0} 왼쪽 시력 평균은 {1} 오른쪽 시력 평균은 {2}".format(old_avg,left_eye,right_eye))