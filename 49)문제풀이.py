top = []
mid = []
count = 0
for i in range(1, 65, 1):
    count = count + 1
    mid.append(i)
    if count == 8:
        count = 0
        top.append(mid)
        mid = []
print(top)