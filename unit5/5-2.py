import numpy as np
x = np.array([64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03])
xm = x.mean()
y = np.array([62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84])
ym = y.mean()
xxm = x-xm
#w = np.einsum('i,i',xxm,y-ym)/np.einsum('i,i',xxm,xxm)
#w = np.dot(xxm,y-ym)/np.dot(xxm,xxm)
w = (xxm@(y-ym))/(xxm@xxm)
b = ym-w*xm
print(w, b)
