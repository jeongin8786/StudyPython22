#파일입출력

#mode - w 새로생성쓰기 a 추가쓰기 r읽기
f=open(r'C:/study/StudyPython22/temp.txt',mode='w', encoding='utf-8')

f.write('안녕하세요.')
f.write('저는 윤정인입니다.')
f.write('한국사람이죠.')

f.close() ##필수
print('파일생성완료')