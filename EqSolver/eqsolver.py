# import numpy as np
# x=np.roots(input().split(' '))
# if np.iscomplex(x[0]):print("no real solution")
# else:print(x)

import tensorflow as tf
import os
import threading
os.environ['TF_CPP_LOG_LEVEL']='2'
# 这个op，作为一个node，添加到graph中
hello = tf.constant('122!')

# 启动TF进程（session）
sess = tf.compat.v1.Session()

# 运行op，并输出结果
print(sess.run(hello))