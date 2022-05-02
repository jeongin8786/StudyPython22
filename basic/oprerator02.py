#문자열 연산
from multiprocessing.dummy import current_process
from platform import python_branch


first ='Hello '
second = 'World!'

print(first + second) #문자열 연산 + (합치기)

print(first*3) # FIRST3번 반복
print(len(first)) #문자열 길이 확인

print(first[0]) #문자열 색인(0이 첫번째글자)
print(first[1])

print(first[-1])
print(first[-2]) #문자열 색인(거꾸로 숫자)

#문자열 자르기
current='2022-05-02 16:16:00'
print(current)
print('year=',current[:4])
print('month',current[5:7])
print('day=',current[8:10])
print('hour=',current[11:13])
print('min',current[14:16])
print('sec=', current[17:])

print('sec2=', current[-2:])