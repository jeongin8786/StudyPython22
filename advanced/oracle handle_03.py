#DB 연동-  INSERT INTO
from __future__ import division
import cx_Oracle as ora

def myconn():
    dsn=ora.makedsn('localhost',1521, service_name='orcl')
    conn=ora.connect(user='scott',password='tiger',dsn=dsn, encoding='utf-8')
    return conn

def get_list(conn):
    cur=conn.cursor()
    for row in cur.execute('select * from divtbl'):
        print(row)

    cur.close()
    conn.close()

def set_list(conn, tup): #tup: 튜플
    cur=conn.cursor()
    query= "INSERT INTO divtbl VALUES(:1, :2)" #SQL Inject 보안문제 + 사용효율성
    cur.execute(query)
    conn.commit() #완전저장
    cur.close()
    conn.close()

if __name__ == '__main__':
    print('DIVTBL데이터 조회')
    get_list(myconn())
    print('DICTBL 신규 입력')
    division, names= input('(division, names) 입력 (구분자 \'\')>').split(' ')
    tup = (division,names)
    set_list(myconn(), tup)
    print('입력후 DIVTBL데이터 조회')
    get_list(myconn())