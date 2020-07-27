s1 = set([1,2,3]) # 집합을 만든다
print(s1)
s2 = set("Hello") # 집합은 순서가 없고 중복을 허용하지 않음
print(s2)
s3 = set(["Hello","Phython"])
print(s3)
# 순서가 없기 때문에 인덱싱은 안된다 슬라이싱도 불가
s3 = list(s3)
print(s3[0]) # 하지만 순서가 마구 바뀌기 때문에 값은 할때마다 바뀐다

a1 = set([1,2,3,4,5,6])
a2 = set([4,5,6,7,8,9])
#교집합 - > 두 개의 집합이 동시에 들고있는 값
print(a1 & a2)
print(a1.intersection(a2))
#합집합 - > 두 집합이 들고있는 중복없는 모든 값
print(a1 | a2) # | - > 파이프
#차집합 - > 교집합을 뺀 나머지 정보
print(a1 - a2)
print(a2 - a1)
#add - > 집합에 요소 추가
a1.add(10)
print(a1)
#update - > 집합에 복수의 값을 추가
a1.update([11,12,13])
print(a1)
#remove - > 요소 삭제
a1.remove(5)
print(a1)