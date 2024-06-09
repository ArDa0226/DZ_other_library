# -*- coding: UTF-8 -*-
import numpy as np

arr_3D = np.arange(12).reshape(2, 2, 3)
print(arr_3D.ndim)
print(arr_3D.shape)
print(arr_3D.size)

print(np.zeros(5))
print('Массив из 0\n', np.zeros((3,4)))

print(np.zeros((2, 3)))
print(np.full((2, 3), 4))

print(np.empty((3, 2)))
print('Массив 2х6\n', np.arange(1, 13).reshape(2, 6))
print('Массив 3х3\n', np.arange(1,10).reshape((3,3)))

def power(i, j):
    return i ** j

print(np.fromfunction(power, (3, 3)))
