import time

a = "내가 그린 목이긴 기린그림은 잘 그린 기린 그림이고"
b = "니가 그린 그린기린그림은 못 그린 기린그림이다"

input("문장을 따라 적으시오 Enter 누를 시 게임 시작")
start = time.time()

print(a)
a1 = input()
print(b)
b1 = input()
end = time.time()
result = end - start

if a == a1 and b == b1:
    print("소요시간은 {0}초 입니다.".format(round(result)))
else:
    print("틀렸습니다. 다시 도전하세요.")