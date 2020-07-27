#1)
class TV:
    def __init__(self):
        self.power = False #bool 타입 -> T, F
        self.ch = 5
        self.vl = 20
    def Power(self):
        self.power = not(self.power)
        self.Show() # 현재 TV상황 보여주는 메서드 호출
    #up, down 할때 self.Show() 넣어주세요
    def ChUp(self):
        self.ch += 1
        self.Show()
    def ChDown(self):
        if self.ch > 1:
            self.ch -= 1
        else:
            print("아래 채널이 없습니다.")
    def VlUp(self):
        self.vl += 1
        self.Show()
        self.Show()
    def VlDown(self):
        if vl >0:
            self.vl -= 1
        self.show(self)
    def Show(self):
        if self.power:
            print("========")
            print("ch : {0} vl : {1}".format(self.ch,self.vl))
        else:
            print("......")

LGTV = TV()
LGTV.Show()
LGTV.Power()
LGTV.ChDown()
LGTV.VlUp()
LGTV.Power()
LGTV.ChDown() #밑에서부터는 안되는 것을 볼 수 있다.
LGTV.VlUp()