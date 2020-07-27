record = ["Enter uid1234 Muzi","Enter uid4567 Prodo","Leave uid1234"
,"Enter uid1234 Prodo","Change uid4567 Ryan"]

list_s = [i.split(" ") for i in record]
print(list_s)

#list_s = [['Enter', 'uid1234', 'Muzi'], ['Enter', 'uid4567', 'Prodo'],
#  ['Leave', 'uid1234'], ['Enter', 'uid1234', 'Prodo'], ['Change', 'uid4567', 'Ryan']]

#여기서 uid와 닉네임만 추출해서 딕셔너리로 만들려면

logs = {log[1]:log[2] for log in list_s if len(log)==3}
print(logs)