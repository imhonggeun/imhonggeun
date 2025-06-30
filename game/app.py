print("안녕하세요")

#파일생성 및 내용추가
#1.파일 생성 및 읽기 모드는 동시에 사용이 안됨
file = open('game\\text.txt', encoding='UTF-8', mode='w') #쓰기
file.write('안녕하세요') #글자 생성
file.close()# 쓰기 이후에 보기를 위해서 파일을 닫는다

file = open('game\\text.txt', encoding='UTF-8', mode='r') #읽기
print(file.readlines())
file.close() #메모리를 사용안하기위해서 필요하다

#파일 안에 내용 보기
#file = open('README.md' ,encoding="UTF-8")
#print(type(file.readlines()))
#for row in file.readlines() :
#    print(row)
