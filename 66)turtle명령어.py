t.shape("classic") # 기본 classic 실제거북이모양 turtle 세모거북이 triangle

t.foward(100) # 거북이가 100픽셀 앞으로
t.backward(100) # 후진 100픽셀
t.left(90) # 거북이가 왼쪽 90도 만큼 회전
t.right(90) # 거북이가 오른쪽으로 90도 만큼 회전
t.circle(50) # 반지름 50짜리 원그림

t.speed(속도) # 거북이의 속도를 바꿈 1:가장느림 10:보통 0:가장빠름
t.pensize(굵기) # 펜의 굵기를 바꿈
t.color("색이름") # 펜의 색을 바꿈 red, black, green, white, pink, blue, yellow 등등
bgcolor("색이름") # 도형 내부를 칠할 색을 바꿈
begin_fill() # 도형 내부 색칠할 준비
end_fill() # 지금까지 그린 도형 색칠하기
showturtle() / st() # 거북이를 화면에서 표시함
hideturtle() / ht() # 거북이를 화면에서 가림
clear() # 거북이를 그대로 둔 채 화면을 지움
reset() # 화면을 지우고 거북이도 시작지점으로 돌림