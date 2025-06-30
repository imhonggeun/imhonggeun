f = open('game\\data1.csv', mode='r', encoding='UTF-8')
# print(f)
arr = f.readlines() #리스트
print(arr) 

for i in range(1, len(arr)): 
    row =arr[i].replace("\n","") #뒤에 줄바꿈 변경(없애줘)
    arr2 = row.split(",") # 
    print(f'arr2 확인 {arr2}')
    print(f'{int(arr2[1])} * {int(arr2[2])} = {int(arr2[1]) * int(arr2[2])}')
f.close