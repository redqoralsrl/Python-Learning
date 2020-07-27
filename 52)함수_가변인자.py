def Total(*args): # 튜플의 형태로 인자 값을 받아온다.
    sum = 0
    print(type(args))
    for i in args:
        sum = sum + i
    return sum
print(Total(1,2,3,4,5))
print(Total(10,20,30,40,50))

##########################

def calc(order, *args):#가변인자(*args)는 먼저 쓰면 오류난다 앞에 들어가서
    if order == "+":#뒤에 선언이 안된다. 그래서 가변인자는 마지막에 선언해야된다.
        sum = 0
        for i in args:
            sum = sum + i
        return sum
    elif order == "*":
        sum = 1
        for i in args:
            sum = sum * i
        return sum
print(calc("+",1,2,3,4,5))
print(calc("*",10,20,30,40,50))
