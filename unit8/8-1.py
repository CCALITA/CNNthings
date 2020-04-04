# -*- coding:utf-8 -*-
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
x = tf.constant([64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03])
y = tf.constant([62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84])
xm = tf.reduce_mean(x)
ym = tf.reduce_mean(y)
W = tf.reduce_sum(tf.multiply(x-xm, y-ym)) / tf.reduce_sum(tf.pow(x-xm, 2))
b = ym - W * xm
print(f"W: {W}")
print(f"b: {b}")
