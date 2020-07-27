#학생예제에다가 사람예제를 상속받아서 사용하기
class Person:
    def __init__(self):
        self.name = input("이름 : ")
        self.age = int(input("나이 : "))
        self.gender = input("성별 : ")
    def ShowPersonInfo(self):
        print("이름 : ",self.name)
        print("나이 : ",self.age)
        print("성별 : ",self.gender)
class Student(Person): # Sutdent가 Person을 상속 받았다. 자식 : Student 부모 : Person
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

        
S1 = Student()
S1.ShowStudentInfo()