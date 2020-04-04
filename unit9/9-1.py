# -*- coding:utf-8 -*-
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
def rd():
    try:
        x1_test = float(input("输入面积, 20<=面积(实数)<=500 :"))
        x2_test = int(input("输入房间数, 1<=房间数(整数)<=10 :"))
        if x1_test < 20 or 500 < x1_test or x2_test < 1 or 500 < x2_test:
            raise OverflowError
    except ValueError:
        print("输入类型非法")
        return rd()
    except OverflowError:
        print("输入的值超越规定范围")
        return rd()
    return x1_test, x2_test
x1 = tf.constant(
    [137.97, 104.5, 100, 124.32, 79.2, 99, 124, 114, 106.69, 138.05, 53.75, 46.91, 68, 63.02, 81.26, 86.21])
x2 = tf.constant([3, 2, 2, 3, 1, 2, 3, 2, 2, 3, 1, 1, 1, 1, 2, 2], dtype=tf.float32)
y = tf.constant([145, 110, 93, 116, 65.32, 104, 118, 91, 62, 133, 51, 45, 78.5, 69.65, 75.69, 95.3])
x0 = tf.fill([16], 1.0)
Y = tf.expand_dims(y, -1)
X = tf.stack((x0, x1, x2), axis=1)
Xt = tf.transpose(X)
XtX_1 = tf.linalg.inv(tf.matmul(Xt, X))
XtX_1_Xt = tf.matmul(XtX_1, Xt)
W = tf.matmul(XtX_1_Xt, Y)
W = W.numpy()

x1_test, x2_test = rd()
y_pred = W[1] * x1_test + W[2] * x2_test + W[0]
print(f"预测价格: {y_pred[0]} 万元")
