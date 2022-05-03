#입력 값을 변수에 저장하기 (매번 다른 값을 변수에 할당)
input()

#input 함수의 결과를 변수에 할당하기
x=input('문자열을 입력하세요: ')
print (x)

# #두 숫자의 합을 구하세요

# a=input('첫 번째 숫자를 입력하세요: ')
# b=input('두 번째 숫자를 입력하세요: ')

# print(a+b) #합이 아닌 'str' 나열

a= int(input('첫 번째 숫자를 입력하세요: ')) #int로 'STR'형을 정수로 변환
b= int(input('두 번째 숫자를 입력하세요: '))
print(a+b)
#입력 값을 변수 두 개에 저장하기
    #변수1, 변수2= input(), input()
    #변수1, 변수2= input().split('기준문자열')
    #변수1, 변수2 = input('문자열').split()
    #변수1, 변수2=input('문자열').split('기준문자열')