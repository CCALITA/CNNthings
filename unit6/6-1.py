# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
D = {'area': np.array([137.97, 104.5, 100., 124.32, 79.2, 99., 124., 114., 106.69, 138.05, 53.75, 46.91, 68., 63.02, 81.26,
              86.21]),
     'price': np.array([145., 110., 93., 116., 65.32, 104., 118., 91., 62., 133., 51., 45., 78.5, 69.65, 75.69, 95.3]),
     }
ft = {'family': 'Microsoft Yahei',
      'size': 14, }
plt.scatter('area', 'price', c='r', data=D)
plt.xlabel("面积(平方米)", fontdict=ft)
plt.ylabel("价格(万元)", fontdict=ft)
plt.title("商品房销售记录", fontdict=ft, size=16, c='b')
plt.show()
