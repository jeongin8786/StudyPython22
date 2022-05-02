#문자열
from cgi import print_arguments
from platform import python_branch


bruce_ecke1 = 'life is shert.\n you need python.'
print(bruce_ecke1)

multi_line = '''life is short
and i need python
and i need c#, too.
'''
print(multi_line)

#리스트(배열)
b=[1,2,3,4]

print(b)

b.append(5) #리스트 맨 마지막 추가
print(b)

b.insert(3.10) #원하는 인덴스에 추가
print(b)

b.sort()#오름차순 정렬
print(b)

b.reverse#내림차순 정렬
print(b)

b.remove(10) #원소삭제
print(b)

print(type(b))

##튜블
c=(1,2,3,4)
print(c)
#c.append(5) #error 튜플에서는 값 추가불가
print(c[2])

##딕셔너리 KEY :value쌍의 집합
spiderman={
    'name' : '피터파커',
    'age' : 18,
    'weapon' : '웹슈터',
    'memverofAvengers' : True
}
    print(spiderman)
    print(spiderman['name'])
    print(spiderman['memverofavengers')
    