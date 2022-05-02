#문자열 포맷팅
a="I'm so happy"
print({0}.format(2))
#문자열 포맷팅 방법
print('{0},{1},{2}', format('하나',2,'삼',4))

--##이위로 하다가 맘...ㅎㅎ

#소수점 표현
PI = 3.14159268
print('{0:0.2f',format(PI))
print(f'{PI:0.3f}')

full_name = 'Hugo MG SUNG'
sp_names = full_name.split() #문자열을 '' 잘라서 리스트로
print(sp_names)
print(sp_names[0])

greeting = 'Hello, World'
words =greeting. split(',') #문자열을 ,로 잘라서 리스트로
print(words)

