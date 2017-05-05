import numpy as np
a = np.arange(18)
a = a.reshape(3, 3, 2)
print(a)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
