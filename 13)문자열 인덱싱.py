#문자열 인덱싱은 왼쪽부터 0부터 오른쪽으로 간다.
#오른쪽부터는 -1부터 시작한다 그리고 제일 왼쪽은 0으로 끝난다.
index = "Welcome to Python!"
print(index[0])
print(index[11])
print(index[-1])
print(index[-14])
length = len(index)#index의 길이를 알 수 있는 명령어
print(length)
print(index[length-1])#0부터 시작하므로 하나를 빼야한다.
#변수[원하는 알파벳위치 순서]를 적어야한다.

c = "abcdefghijklmnopqrstuvwxyz"
d = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#"Life is too"
#"Python"을 만드시오
print("\""+d[11]+c[8]+c[5]+c[4]+" "+c[8]+c[-8]+" "+c[-7]+c[-12]+c[-12]+"\"")
print("\""+d[-11]+c[-2]+c[-7]+c[7]+c[-12]+c[13]+"\"")