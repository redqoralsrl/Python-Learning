import math #수학관련 함수 모듈
print(math.pi) #원주율
print(math.e) #자연상수 e
print(math.factorial(10)) #팩토리얼 (10x9x8x7x6x5x4x3x2x1)
print(math.pow(2,3)) #제곱 (**)
print(math.sqrt(16)) #제곱근 (루트씌우는거)
print(math.gcd(10,12)) #최대공약수

#from 모듈 import 함수명 : 모듈 중 일부 함수만 가져옵니다.
from math import pow
print(pow(2,3))

from math import pow, factorial, sqrt
print(factorial(10))
print(sqrt(16))


import os
import inspect #모듈이 저장되어 있는 실제경로가 어딘지 알아내봅시다
print(inspect.getfile(os))
print(inspect.getfile(inspect))