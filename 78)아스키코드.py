#ASCII Code
#ord(글자) => ASCII코드로 변환
print(ord('A')) #65
print(ord('Z')) #90
print(ord('a')) #97
print(ord('z')) #122

#char(숫자) => 글자로 변환
print(chr(65))
print(chr(90))

for i in "Hello Python":
    print(ord(i),end = " ")