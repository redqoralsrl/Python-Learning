money = int(input("밥 뭐먹을까? 얼마있어?: "))
if money >= 50000:
    print("소고기 먹자")
else:
    if money >= 30000:
        print("돼지고기 먹자")
    else:
        if money >= 10000:
            print("돈까스 먹자!")
        else:
            print("요즘 알바 시급이 얼마지?")
money = int(input("밥 뭐먹을까? 얼마있어?: "))
if money >= 50000:
    print("소고기 먹자")
elif money >= 30000:
    print("돼지고기 먹자")
elif money >= 10000:
    print("돈까스 먹자")
else:
    print("요즘 알바 시급이 얼마지?")