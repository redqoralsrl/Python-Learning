This_year = int(input("올해의 년도를 입력 : "))
Birth_year = int(input("태어난 년도를 입력 : "))
age = This_year - Birth_year + 1
print("당신의 나이는 ",age,"세 입니다.")

Max_Weight = 600
Object1 = float(input("첫번째 물건의 무게 : "))
Object2 = float(input("두번째 물건의 무게 : "))
Current_Weight = Max_Weight - (Object1 + Object2)
print("현재 엘리베이터 허용 무게는 ",Current_Weight,"kg 입니다.")

Current_Height = int(input("현재 키를 입력하세요 : "))
Man_StandardWeight = (Current_Height - 100) * 0.9
print("당신의 표준 체중은 ",Man_StandardWeight,"(kg) 입니다.")