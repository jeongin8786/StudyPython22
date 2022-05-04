#주소록 프로그램 v1.0

if __name__ =='__main__':
        print('--주소록 프로그램 v1,1--')
#주소록 시작
class contact:
    name = '';phone_num='';e_mail='';addr=''

    def __init__(self, name, phone_num, e_mail, addr) -> None:
        self.name=name
        self.phone_num = phone_num
        self.e_mail = e_mail
        self.addr = addr
#작성일: 2022-05-04
#작성자 : yun jeongin
#설명: 와 내일 논다 히히
import os
from unicodedata import name 
#연락처 클래스
    def __str__(self) -> str:
        str_val =  (f'이  름:{self.name}\n'
                    f'핸드폰: {self.phone_num}\n'
                    f'이메일: {self.e_mail}\n'
                    f'주  소:{self.addr}\n'
                    f'==============================')
        return str_val

    def run():
        1st_contact =[] #빈 리스트 생성
        # contact=Contact('홍길동','010-0000-0000','hgd@naver.com','서울')
        # print(contact)
        # set_contact():
        while True:
            sel_menu = get_manu()
            if sel_menu ==1:
                    clearconsole
                pass
            elif sel_menu =3:
                clearconsole()
                name=input('삭제할 이름 입력:>')
                del_contact(1stcontact,name)
                pass
            elif sel_menu =4:
                break
            
            else:
                clearconsole()
              

 #주소록 입력함수
  
    def set_contact()-> Contact:
        name, phone_num,  email,addr =\
            input('정보입력(이름,핸드폰, 이메일, 주소(구분자/))').split('/')
        contact = Contact(phone_num=phone_num,email=email,name=name, addr=addr)
        return contact

#주소록 전체 출력
    def get_contact(1sr_contact):
        for contact in 1st_contact:
            print(contact)
#주소록 삭제
    def del_contact(1st_contact, name):
        for i, contact in enumerate(1st_cotact):
            if contact.name ==name: 
                del contact

    def get_manu():
        str_menu = ('--주소록 프로그램 v1,1--\n'
                    '1. 연락처 추가\n'
                    '2. 연락처 출력\n'
                    '3. 연락처 삭제\n'
                    '4. 종료\n')
        print(str_menu)
        menu = input('메뉴입력 : ')
        return int (menu)

    def clearconsole():
        Command='clear'
        if os.name in ('nt','dos'): #mac, unix, linux 화면 클리어 명령어
            Command='cls'
            os. system(Command)
    if __name__ =='__main__':
        print('--주소록 프로그램 v1,1--') #windows, dos 화면 클리어 명령어
        run()