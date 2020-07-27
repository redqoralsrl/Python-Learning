#파일열기 open()
#파일사용 write() read()
#파일닫기 close()

#파일열기
#파일을 참조할 변수 = open("파일이름(경로포함)","파일열기모드")
#r - 읽기모드 - 파일을 읽어 낼 때 사용
#w - 쓰기모드 - 파일에 내용을 쓸 때 사용
#a - 추가모드 - 파일의 끝에 내용을 추가할 때 사용

#파일출력
#파일 자료형의 내장함수 writhe()를 사용한다
#파일변수.write(파일 내에 출력할 내용)

f = open("new.txt",'w')
f.write("파일출력")
f.close

#파일 입력이나 파일 출력은 동작하는 프로그램이 기준
#파일출력: 프로그램 -> 파일
#파일입력: 파일 -> 프로그램

f = open("C:\\Users\\백민기\\Desktop\\프로그래밍\\Python\\Python 정리\\day10-내가한거\\student.txt",'w')
for i in range(1,5,1):
    name = input("%d번째 학생이름 입력:"%i)
    data = "%d번째 : %s \n"%(i,name)
    f.write(data)
f.close

#with를 이용한 파일 출력(with가 끝나면 자동으로 close)

with open("C:\\Users\\백민기\\Desktop\\프로그래밍\\Python\\Python 정리\\day10-내가한거\\student1.txt",'w') as f:
    for x in range(1,5,1):
        name = input("%d번째 학생이름 입력:"%x)
        data = "%d번째 : %s \n"%(x,name)
        f.write(data)

#파일에 내용 추가
#파일을 쓰기모드(w)로 열면 기준에 있던 내용이 모두 삭제된다
#원래 있던 내용을 유지하고 새로운 내용을 추가하려면 추가모드(a)를
#사용해야한다

f = open("C:\\Users\\백민기\\Desktop\\프로그래밍\\Python\\Python 정리\\day10-내가한거\\student1.txt",'a')
f.write("\n오늘도 열심히 파이썬 합시다!!")
f.close()