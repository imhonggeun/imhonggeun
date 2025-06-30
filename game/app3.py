f = open('game\\data3.csv', mode='r', encoding='UTF-8')
arr = f.readlines()

#내가 한것
'''
for row in arr:
    row = row.replace("\n","")
    row = row.replace(","," ")
    print(row)
'''

arr2 = [] #빈 리스트 생성
for row in arr:
    row = row.replace("\n", "")
    arr2.append( row.split(",") )
    #print(f'row를 확인해줘 {row}')
for row in arr2:
    행 = ""
    for v in row:
        행 += 'O' if v == 'O' else ' '
    print(f'행을 확인해줘 {행}')

