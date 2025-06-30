#함수로 생성

f = open('game\\data1문제.csv', mode='r', encoding='UTF-8')
# print(f)
arr = f.readlines() #리스트
#print(arr) 

def 함수표():
    arr2 = []
    for i in range(0, len(arr)): # 리스트 길이만큼 숫자를 지정
        row = arr[i].replace("\n", "") # 리스트 안에서 \n를 지운다
        arr2.append(row.split(",")) # ,를 기준으로 빈칸도 공간으로 표시한다
    for row in arr2: 
        #print(f'row 뭐야{row}')
        행 = ""
        for v in row:
            #print(f"이건 뭐야 {v}")
            행 += '0' if v == 'O' else ' '
        print(행)
함수표()