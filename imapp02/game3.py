import mariadb
import os

def 마리아디비():
    conn_params = {
        "user" : os.getenv('MARIADB_USER'),
        "password" : os.getenv('MARIADB_PASSWORD'),
        "host" : os.getenv('MARIADB_HOST'),
        "database" : os.getenv('MARIADB_DATABASE'),
        "port" : int(os.getenv('MARIADB_PORT'))
    }
    # conn_params = {
    #     "user" : os.getenv('MARIADB_USER'),
    #     "password" : os.getenv('MARIADB_PASSWORD'),
    #     #"host" : "localhost",
    #     #"host" : "192.168.0.23",#우리꺼
    #     "host" : os.getenv('MARIADB_HOST'),#학원
    #     "database" : os.getenv('MARIADB_DATABASE'),
    #     "port" : os.getenv('MARIADB_PORT')
    # }
    return mariadb.connect(**conn_params)


def 입력():
    conn = 마리아디비()
    cur = conn.cursor()

    title = input("제목을 입력하세요.")
    desc = input("설명을 입력하세요.")

    sql = f"INSERT INTO NOTICE (`title`, `desc`) VALUE ('{title}', '{desc}')"
    cur.execute(sql)
    conn.commit()

    cur.close()
    conn.close()

def 읽기():
    conn = 마리아디비()
    cur = conn.cursor()
    
    sql = 'SELECT  * FROM `edu`.`NOTICE`'
    cur.execute(sql)
    result = cur.fetchall()
    
    if result == None:
        print("데이터가 없습니다.")
    else:
        for row in result:
            행 = ""
            for col in row:
                if col == None:
                    행 += "\t"
                else:
                    행 += f'{col} '
            print(행)

def 선택적읽기():
    conn = 마리아디비()
    cur = conn.cursor()
    
    no = input("숫자를 입력하세요")
    sql = f'SELECT  * FROM `edu`.`NOTICE` where NO={no}'
    
    cur.execute(sql)
    result = cur.fetchone()
    
    if result == None:
        print("데이터가 없습니다.")
    else:
        #for row in result:
        행 = ""
        for row in result:
            if row == None:
                행 += "\t"
            else:
                행 += f'{row} '
        print(행)

    # conn = 마리아디비()
    # cur = conn.cursor()
    # no = int(input("불러올 입력값을 가지고 오세요"))
    # sql = f'SELECT * FROM NOTICE where NO ={no}'
    # cur.execute(sql)
    # result = cur.fetchone() #fetchall = list , fetchone = tuple
    # col_name=cur.description
    # #print(col_name[0])
    
    # name = ''
    # for row in col_name:
    #     name += row[0] + ("\t\t\t" if row[0] == 'regDate' else "\t")
    # #print(name)
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
    # print(result)

def 삭제():
    conn = 마리아디비()
    cur = conn.cursor()

    no = int(input("삭제할 번호를 적어주세요"))
    sql = f"DELETE FROM notice WHERE  no={no};"
    
    cur.execute(sql)
    conn.commit()

    cur.close()
    conn.close()

def 수정():
    conn = 마리아디비()
    cur = conn.cursor()

    no = int(input("변경할 번호를 적어주세요"))
    title = input("타이틀에 수정할 내용작성해주세요")
    desc = input("설명에 수정할 내용작성해주세요")
    content =input("내용에 수정할 내용작성해주세요")
    # sql = f"UPDATE NOTICE SET `title`='{title}',`desc`='{desc}',`content`='{content}'  WHERE no={no}"
    
    txt = ""
    if title != "": # 작성 됐을 때
       txt = f"`title`='{title}'" #txt 라는 변수에 타이틀 내용을 작성
    if desc != "": # 작성이 됐을 때
        txt += f", `desc`='{desc}'" if txt != "" else f"`desc`='{desc}'" #
    if content != "":
        txt += f", `content` = '{content}'" if txt != "" else f"content = '{content}'"

    if txt != "":
        sql = f"UPDATE NOTICE SET {txt} WHERE  no = {no}"
        cur.execute(sql)
        conn.commit()

    
    cur.execute(sql)
    conn.commit()

    cur.close()
    conn.close()

while True:
    모드 = input("CRUD 중에 선택하세요")
    if 모드 == 'C':
        입력()
    elif 모드 == 'R':
        타입 = input("전체 또는 선택 이라는 단어를 입력해주세요")
        if 타입 == '전체':
            읽기()
        elif 타입 =='선택':
            선택적읽기()
    elif 모드 == 'U':
        수정()
    elif 모드 == 'D':
        삭제()
    else :
        break