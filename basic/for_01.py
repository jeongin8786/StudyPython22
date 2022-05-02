 #for문 학습
arr=[1,2,3,4,5]
result =0 

for x in range(1, 101):
    result = result + x

print('배열의 합=', result)

arr2=('me', 'my','friend','jane')

for item in arr2:
    print(f'{item:>10}')

 #한줄주석

 from ast import Continue
"""
다중문자열==여러줄주석
"""
 ##1~10까지 수에서 짝수 구분하기
for num in range(1,11):
    if(num%2) == 0:
        print(f'{num}은 짝수입니다.')
  else:
        print(f'{num}는 홀수입니다.') 

#for문 내에서 사용하는 continue, break

values = [1,3,4,5,7,9,11,13,15,17,19]


num=0
for item in values:
    num +=1 #num=num+1
    if (num % 2) ==0:
        continue 
        #break반복문 탈출
        
    else:
        print(f'{num}번 수는 {item}입니다.')

#ㄸ아니시발 왜안돼는데
