import numpy as np
x = np.array([[20,20,20],[30,30,30],[40,40,40]])
print("Original array:")
print(x)
v = np.array([20,30,40])
print("Vector:")
print(v)
print(x / v[:,None])
