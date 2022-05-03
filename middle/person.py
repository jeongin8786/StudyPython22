#사람객체를 위한 클래스 person
from typing_extensions import Self


class person:
    __name='' #이름속성
    age=0  #나이속성
    height = 100 #키
    weight = 30 #몸무게
#생성자 재정의
    def __init__(self)-> None:
    pass


    def walk(self, speed):
        print(f'{self.name}가 {speed}kn/h로 뛴다')
        return
  
p=person(성명건) #객체 생성
p.name = '성명건'
p.age=46
p.height=178
p.weight=70

p.walk(2)
p.run(10)

#print(type(p))
print(p)

print(f'{Self.__name} 탄생!!!')
#매직메서드 __str__ 사용 재정의
# def __str__(self) ->str:
#     value = f'''객체 : {self.__name\n
#     나이: {self.age}\n
#     키: {self.height}'''
#     return value
