class Calculator:
     #생성자 Calculator 객체 생성시 자동으로 호출되는 함수
    def __init__(self): #self 자기 자신을 가리키는 변수
        self.result = 0 #self.result Calculator가 가지는 멤버 변수
    def adder(self,num): #self는 무조건 들어가야된다. 즉 내가 들어가야된다.
        self.result += num
        return self.result
Cal1 = Calculator() #객체 생성하면서 result에 0값을 만든다.
print(Cal1.result)
Cal2 = Calculator()
print("Cal1 : ",Cal1.adder(3))
print("Cal2 : ",Cal2.adder(4))
print("Cal2 : ",Cal2.adder(3))
print("Cal2 : ",Cal2.adder(7))

'''
class 객체:
    def __init__(self): #self는 나 자신임
가 기본틀로 생각
'''

#사람을 만들고 싶다.
class Person:
    def __init__(self): #사람을 만들고
        self.name = input("이름 : ")
        self.age = int(input("나이 : "))
        self.gender = input("성별 : ")
    def ShowPersonInfo(self): #이제 출력을 만든다.
        print("이름 : ",self.name)
        print("나이 : ",self.age)
        print("성별 : ",self.gender)
P1 = Person() #P1에 클래스를 넣는다.
P2 = Person()
P1.ShowPersonInfo() #출력 만든 것을 사용
P2.ShowPersonInfo()

    