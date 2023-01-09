'''
    * 텐서(tensor)
        - 배열(array)이나 행렬(matrix)과 매우 유사한 특수한 자료구조
'''
# list로부터 tensor 생성하기
import torch
import numpy as np

data = [[1,2], [3,4]]
x_data = torch.tensor(data)
print(x_data)

# numpy array로부터 tensor 생성하기    -> copy본 생성
np_array = np.array(data)
x_np_1 = torch.tensor(np_array)
print(x_np_1)

x_np_2 = torch.as_tensor(np_array)  # -> view를 만듦
print(x_np_2)

x_np_3 = torch.as_tensor(np_array)  # -> view를 만듦
print(x_np_3)

x_np_1[0,0] = 5 # copy본 수정
print(x_np_1)

# original 확인
print(np_array)
# 변하지 않음 -> np_1는 말 그대로 copy가 된 것

# 나머지 확인
print(x_np_2)
print(x_np_3)
# 2,3는 copy본이 수정됨에 따라 변하지 않고 원본을 따라감

x_np_4 = torch.from_numpy(np_array)
print(x_np_4)

print("---------------------------------------------------")
np_again = x_np_1.numpy()
print(np_again, type(np_again))

print("---------------------------------------------------")
a = torch.ones(2,3) #1로만 채움
print(a)

b = torch.zeros(2,3)    #0으로만 채움
print(b)

c = torch.full((2,3), 2)    #,뒤의 숫자로만 채움
print(c)

d = torch.empty(2,3)    #초기화가 안된 경우 여러 값이 나올 수 있음
print(d)

print("------------------------------------")
e = torch.arange(10)
print(e)

f = torch.rand(2,2) # 0과 1 사이의 숫자를 균등하게 생성
print(f)

g = torch.randn(2,2)    # -값도 포함
print(g)

print("========================================")
a = torch.arange(1, 13).reshape(3,4)
print(a)

#indexing
print(a[1])
print(a[0, -1])

#slicing --- (?)
print(a[1:-1])
print(a[0:-1])
print(a[0:0])
print(a[0:1])
print(a[:2, 2:])    # 첫번째행, 두번째행까지의 모든 행과 세번째 이후의 모든 열
print(a[2:-1])

x = torch.tensor([[1,2], [3,4]], dtype=torch.float32)
y = torch.tensor([[5,6], [7,8]], dtype=torch.float32)
# print(x)
# print(y)
# print("===========----------------=================------------------")
# print("x+y : ", x+y)
# print("x-y : ", x-y)
# print("x*y : ", x*y)
# print("x/y : ", x/y)
print("x@y : ", x@y)
print('='*30)
print(torch.add(x,y))
print(torch.subtract(x,y))
print(torch.multiply(x,y))
print(torch.divide(x,y))
print(torch.matmul(x,y))

