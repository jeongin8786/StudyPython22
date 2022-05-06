#오라클 DB연동
import cx_Oracle as ora

#데이터 소스 네임 객체 생성 ("사용자 이름","비밀번호","호스트이름:포트/서비스이름")
dsn = ora.makedsn('localhost', 1521, service_name='orcl')
#DB연결객체
conn = ora.connect(user='SCOTT', password='tiger', dsn=dsn, encoding='utf-8')

cur = conn.cursor() #커서생성
query='select * from MEMBERTBL'

for row in cur.execute(query):
    print(row)

cur.close()
conn.close()
