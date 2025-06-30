#1번 파일생성 및 글쓰기
'''
파일명 = input('파일이름을 입력하세요')
신규파일 = open(f'game\\{파일명}', encoding='UTF-8', mode='w')
글 = input("내용 입력하세요.")
신규파일.write(글)
신규파일.close()
'''

#2번 def 함수로 생성 및 글쓰기 나누기
def 메모장생성():
    파일명 = input('파일이름을 입력하세요')
    return open(f'game\\{파일명}', encoding='UTF-8', mode='w')

#메모장글쓰기 반복문 3번으로 변경
'''
def 메모장글쓰기(파일):
    글 = input("내용 입력하세요.")
    파일.write(글)
    파일.close()
''' 
#3번 반복문 추가 while 
def 메모장글쓰기(파일):
    while True:
        글 = input("내용 입력하세요.")
        if 글 == '':
            글='\n'
        elif 글 =='exit()':
            break
        파일.write(글)
    파일.close()

def 메모장읽기():
    파일명 = input('읽을 파일을 입력하세요')
    입력받은파일 = open(f'game\\{파일명}', encoding='UTF-8', mode='r')
    #print(입력받은파일.readlines())
    입력받은파일.readlines()
    return 입력받은파일.close()

def 메모장글추가():
    파일명 = input('글추가할 파일을 입력하세요')
    글추가파일 = open(f'game\\{파일명}', encoding='UTF-8', mode='a')
    글추가파일.write(input("추가할 내용을 입력하세요"))
    글추가파일.close()
    return 


메모장글쓰기(메모장생성()) #마지막
메모장글추가()
메모장읽기()
