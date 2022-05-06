#오라클 DB연동
import cx_Oracle as ora

def myconn():    
    #데이터 소스 네임 객체 생성 ("사용자 이름","비밀번호","호스트이름:포트/서비스이름")
    dsn = ora.makedsn('localhost', 1521, service_name='orcl')   
    #DB연결객체
    conn = ora.connect(user='SCOTT', password='tiger', dsn=dsn, encoding='utf-8')
    return conn

def test01(conn):
    cur = conn.cursor() #커서생성
    query='select * from emp'

    for row in cur.execute(query):
        print(row)

    cur.close() #커서 닫는다.
    conn.close()

def test02(conn):
    cur = conn.cursor() #커서생성
    query='select * from emp'
    cur.execute(query)
    for row in cur.execute(query):
        print(row)
    cur.close() #커서 닫는다.
    conn.close()
    

if __name__ == '__main__':
    print('---SQL조회 기본실행---')
    test01(myconn())
    print('---SQL조회 fetchone---')
    test02(myconn())
    