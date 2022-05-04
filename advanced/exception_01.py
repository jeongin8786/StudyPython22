#예외처리1 - 예외발생
def multi(a,b):
    res = a*b
    return res

def divide(a,b):
    res=0
  
    try:
        res=a/b
    except Exception as e:
        print(f'예외발생 {e}')
    return res
value=7
print('곱셈/나눗셈')

try:
    print(divide(6,0))
   
    
except ZeroDivisionError as e:
    #print(e)
    print('b에다가 0쫌 넣지마세요!! 이 바보야!@!')

print(multi(6,6))
print('종료')