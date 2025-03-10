import numpy as np
x0 = np.ones(10)
x1 = np.array([64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03])
x2 = np.array([2, 3, 4, 2, 3, 4, 2, 4, 1, 3])
y = np.array([62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84]).reshape(10, 1)
X = np.column_stack((x0, x1, x2))
#W = np.linalg.inv(np.einsum('ji',X) @ X) @ (np.einsum('ji',X) @ y)
W = np.linalg.inv(X.T @ X) @ (X.T @ y)
print(f'{W.shape}\n{X}\n{y}\n{W}')
