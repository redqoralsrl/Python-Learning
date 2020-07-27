class Animal:
    def __init__(self, weight, sound):
        self.weight = weight
        self.sound = sound
    def sleep(self):
        print("코 잔다.")
    def eat(self):
        print("먹는다.")
    def speak(self):
        print(self.sound)
    def show(self):
        print("동물 : %.2f"%self.weight)
class Cat(Animal):
    def eat(self):
        print("생선을 먹는다.")
    def show(self):
        print("고양이 : %.2f"%self.weight)
class Dog(Animal):
    def eat(self):
        print("뼈다귀를 먹는다.")
    def show(self):
        print("강아지 : %.2f"%self.weight)

Jinwoo = Animal(72.5,"드르렁")
Jinwoo.sleep()
Jinwoo.eat()
Jinwoo.speak()
Jinwoo.show
print()
Cat_M = Cat(10,"냐옹냐옹")
Cat_M.sleep()
Cat_M.speak()
Cat_M.eat()
Cat_M.show()