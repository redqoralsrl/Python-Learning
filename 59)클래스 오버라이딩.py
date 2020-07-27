# 상속 받은 곳에서 오버라이딩이란 상속받은걸 수정해서 덧입히겠다 이다.
class Person:
    def __init__(self):
        self.name = input("이름 : ")
        self.age = int(input("나이 : "))
        self.gender = input("성별 : ")
    def ShowPersonInfo(self):
        print("이름 : ",self.name)
        print("나이 : ",self.age)
        print("성별 : ",self.gender)
    def Eat(self):
        print("밥을 먹습니다.")
class Student(Person):
    def __init__(self):
        Person.__init__(self)
        self.Class = int(input("학년 : "))
        self.StudentNumber = int(input("학번 : "))
        self.KorScore = int(input("국어점수 입력 : "))
        self.EngScore = int(input("영어점수 입력 : "))
        self.MatScore = int(input("수학점수 입력 : "))
        self.Total = self.KorScore + self.EngScore + self.MatScore
        self.Evg = self.Total / 3
        if self.Evg >= 90:
            self.Grade = 'A'
        elif self.Evg >= 80:
            self.Grade = 'B'
        elif self.Evg >= 70:
            self.Grade = 'C'
        elif self.Evg >= 60:
            self.Grade = 'D'
        else:
            self.Grade = 'F'
    def ShowStudentInfo(self):
        print("{0}학생의 정보{1}".format(self.name,self.StudentNumber))
        print("나이:{0} 성별:{1} 학년:{2}".format(self.age,self.gender,self.Class))
        print("합계:{0} 평균:{1} 등급:{2}".format(self.Total,round(self.Evg),self.Grade))
    def Eat(self): # 원래는 충돌이 나야 정상이지만 함수를 재정의 한다. 내용을 바꿔치기 하겠다고도 한다.
        print("그 성적에 밥이 넘어가냐?")

S1 = Student()
S1.ShowStudentInfo()
P1 = Person()
P1.Eat()
S1.Eat()