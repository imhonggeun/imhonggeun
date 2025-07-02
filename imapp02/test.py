# import mariadb

# conn_params= {
#     "user" : "study",
#     "password" : "study",
#     #"host" : "localhost",
#     "host" : "192.168.0.23",#우리꺼
#     "database" : "edu"
# }

# # Establish a connection
# #connection =conn , cursor =cur
# conn= mariadb.connect(**conn_params)

# cur= conn.cursor()

# # sql = 'SELECT  `no`,  `title`,  `desc`, LEFT(`content`, 256),  `regDate`,  `modDate` FROM `edu`.`NOTICE` LIMIT 1;'

# sql ='SELECT * FROM NOTICE' #변경
# cur.execute(sql)
# result = cur.fetchone() #fetchall = list , fetchone = tuple
# col_name=cur.description

# #print(col_name[0])

# name = ''
# for row in col_name:
#     name += row[0] + ("\t\t\t" if row[0] == 'regDate' else "\t")
# print(name)
# if result == None:
#     print("데이터 없습니다.")
# else:
#     row=''
#     #print('no\ttitle\tdesc\tcontent\tregDate\t\t\tmodDate')
#     for col in result:
#         #print(col)
#         if col == 'None':
#             row += ('없음\t')
#         else:
#             row += (f'{col}\t')
#     print(row)
# #print(result)
# print(name)

# cur.close()
# conn.close()

import mariadb
def 마리아디비():
    conn_params = {
        "user" : "study",
        "password" : "study",
        "host" : "192.168.0.23",
        "database" : "edu",
        "port" : 3306
    }
    return mariadb.connect(**conn_params)

def 입력():
    conn = 마리아디비()
    cur = conn.cursor()

    title=input("제목을 입력하세요.")
    desc=input("설명을 입력")
    content=input("콘텐트 입력")

    sql = f"INSERT INTO NOTICE (`title`,`desc`,`content`) VALUE ('{title}','{desc}','{content}')"
    cur.execute(sql)
    conn.commit()

    cur.close()
    conn.close()

def 읽기():
    conn = 마리아디비()
    cur = conn.cursor()
    #숫자=int(input("숫자를 입력해주세요."))
    sql = 'SELECT  * FROM NOTICE'
    cur.execute(sql)
    result = cur.fetchall()

    col_name = cur.description
    for x in range(col_name):
        name = ""
        for row in col_name:
            name += row[0] + ("\t\t\t" if row[0] == 'regDate' else "\t")
        print(name)

        if result == None:
            print("데이터가 없습니다.")
        else:
            행 = ""
            #print('no\ttitle\tdesc\tcontent\tregDate\t\t\tmodDate')
            for col in result:        
                if col == None:
                    행 += "없다\t"
                else:
                    행 += f'{col}\t'
            print(행)
    
    cur.close
    conn.close
while True:
    모드 = input("CRUD 중 선택하세요 C:입력 R:읽기 U: D: 입니다.")
    if 모드 == 'C':
        입력()
    elif 모드 == 'R':
        읽기()
        
    else:break