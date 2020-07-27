import numpy as np
print(np.array([1,2,3,4,5,6]))
print(np.arange(1,7,1))

a = [1,2,3,4,0.1,0.8]
a1 = np.array(a) # 정수와 실수가 동시에
print(a1)

print(np.array(range(10))) # for range문과 동일
print(np.array(range(1,11,1)))


print(np.zeros(3)) # 0
print(np.ones(3)) # 1
print(np.zeros((3,4)))
print(np.ones((3,4)))
print(np.eye(5))

a = [1,2,3]
b = [2,3,4]
print(np.r_[a,b])
print(np.r_[[a],[b]])