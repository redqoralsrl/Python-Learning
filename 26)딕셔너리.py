Person = {"Name":"백민기","Number":"010-5879-3725"}
# 세미콜론 기준으로 왼쪽이 key값 오른쪽이 value값이다
print(Person) # 딕셔너리를 그냥 출력
print(Person["Number"]) # 딕셔너리안에 Number의 value값 출력
Person["Height"] = 190 # 새로운 딕셔너리 값 추가
print(Person)
print(Person["Height"]) # 키의 value 값 출력

del Person["Height"] # 딕셔너리 정보 중 한개 삭제
print(Person)

Person["Name"] = "강동원" # 딕셔너리안에 키값 Name의 정보를 수정
print(Person)
print(Person.keys()) # 딕셔너리의 키 값들만 출력
print(Person.values()) # 딕셔너리의 value 값들을 출력
KeyList = list(Person.keys()) # 딕셔너리의 키값들을 추출 후 KeyList에 리스트로 만듬
ValueList = list(Person.values()) # 딕셔너리의 value값들을 추출 후 ValueList에 리스트로 만듬
print(KeyList)
print(KeyList[1]) # 리스트로 만들었으니 인덱싱이 가능하다
print(ValueList)

print(Person["Name"]) # 둘 중 편한걸로 출력하면 된다
print(Person.get("Name"))

print("Name" in Person)
print("Birth" in Person)
print("Name" not in Person)
print("Birth" not in Person)

Person2 = {input("원하는 키값 : "):input("원하는 value값 : "),input("원하는 키값 : "):input("원하는 value값 : ")}
print(Person2)