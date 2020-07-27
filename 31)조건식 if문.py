#in, not in
Value = ('a','b','c')
if 'a' in Value:
    print("튜플 내에 a가 존재합니다.")
if 'd' in Value:
    print("튜플 내에 d가 존재합니다.")
if 'a' not in Value:
    print("튜플 내에 a가 존재하지 않습니다.")
if 'd' not in Value:
    print("튜플 내에 d가 존재하지 않습니다.")

print("="*30)
b = {1:'a',2:'b',3:'c'}
if 1 in b:
    print("1은 딕셔너리 안에 존재합니다.")
if 'a' in b:
    print("a는 딕셔너리 안에 존재합니다.")#value로 검색은 안된다.
if 'a' in b.values():
    print("a는 딕셔너리 안에 존재합니다.")

print("="*30)
print("3의 배수 판별기")
num = int(input("숫자를 입력 : "))
if num % 3 != 0:
    pass
else:
    print("3의 배수 입니다.")