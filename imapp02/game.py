import mariadb

conn_params= {
    "user" : "study",
    "password" : "study",
    "host" : "localhost",
    "database" : "edu"
}

# Establish a connection
#connection =conn , cursor =cur
conn= mariadb.connect(**conn_params)

cur= conn.cursor()

# sql = 'SELECT  `no`,  `title`,  `desc`, LEFT(`content`, 256),  `regDate`,  `modDate` FROM `edu`.`NOTICE` LIMIT 1;'

sql ='SELECT * FROM `edu`.`NOTICE` WHERE NO = 1' #변경
cur.execute(sql)
result = cur.fetchone() #fetchall = list , fetchone = tuple
col_name=cur.description

print(col_name[0])

name = ''
for row in col_name:
    name += row[0] + ("\t\t\t" if row[0] == 'regDate' else "\t")
print(name)
if result == None:
    print("데이터 없습니다.")
else:
    row=''
    #print('no\ttitle\tdesc\tcontent\tregDate\t\t\tmodDate')
    for col in result:
        #print(col)
        if col == 'None':
            row += ('없음\t')
        else:
            row += (f'{col}\t')
    print(row)
print(result)
#print(type(result))

cur.close()
conn.close()