# -*- coding:utf-8 -*-
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
x = tf.constant([64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03])
y = tf.constant([62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84])
n = len(x)
x_sum = tf.reduce_sum(x)
y_sum = tf.reduce_sum(y)
W = (n * tf.reduce_sum(tf.multiply(x, y)) - tf.reduce_sum(y_sum * x)) /\
    (n * tf.reduce_sum(tf.pow(x, 2)) - tf.pow(x_sum, 2))
b = (y_sum - W * x_sum) / n
print(f"W: {W}")
print(f"b: {b}")
