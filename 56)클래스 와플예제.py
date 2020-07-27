class Waffle:
    def __init__(self):
        self.taste = ""
    def SetTaste(self,taste):
        self.taste = taste
    def ShowTaste(self):
        print("{0}맛 와플을 만들었습니다.".format(self.taste))

Waffle1 = Waffle() # 오브젝트 -> (정보를 들고 잇지 않는 놈)
Waffle2 = Waffle() # 오브젝트
Waffle1.SetTaste("딸기") # 인스턴스화 -> (정보를 부여)
Waffle2.SetTaste("초코") # 인스턴스화 -> (정보를 부여)
Waffle1.ShowTaste() # 인스턴스
Waffle2.ShowTaste() # 인스턴스

##################
#하지만 만약 SetTaste에 맛을 넣지 않았다면 ?? 따로 설정을 추가로 해주면 좋다
class Waffle:
    def __init__(self):
        self.taste = ""
    def SetTaste(self,taste):
        self.taste = taste
    def ShowTaste(self):
        if self.taste == "":
            print("맛을 넣어주세요.")
        else:
            print("{0}맛 와플을 만들었습니다.".format(self.taste))
 # 중간에 Set 값을 안하면
Waffle3 = Waffle() # 오브젝트
Waffle3.ShowTaste() # 오브젝트(값이 없다....)
