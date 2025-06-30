print("안녕하세요")

file = open('README.md' ,encoding="UTF-8")
#print(type(file.readlines()))
for row in file.readlines() :
    print(row)
