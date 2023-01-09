import numpy as np
import torch

A = [1,2,3,4,5]
B = np.array([0, 1, 2, 3, 4, 5])

print(B)
print(B.dtype)
print(type(B))
print(type(B[0]))

a = torch.arange(1, 13).reshape(3,4)
print(a)
print(a[2:1])
print(a[2:0])
print(a[2:-1])
print(a[2:-2])

print(a[1:2])
