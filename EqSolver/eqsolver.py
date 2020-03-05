import numpy as np
x=np.roots(input().split(' '))
if np.iscomplex(x[0]):print("no real solution")
else:print(x)