#번호 가중치를 준 로또프로그램
import numbers as rnd
import random
from turtle import window_height

numbers=weight = list(range(1, 46))
lottery = []
random.shuffle(weight)

lottery = random.choice(numbers,weights=weight, k=6)

print(lottery)
