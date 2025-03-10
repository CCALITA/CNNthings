# -*- coding:utf-8 -*-
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.sans-serif"] = "Microsoft Yahei"
plt.rcParams["axes.unicode_minus"] = False
mnist = tf.keras.datasets.mnist
(train_x, train_y), (test_x, test_y) = mnist.load_data()
plt.figure(figsize=(10, 10))
plt.suptitle("MNIST测试集样本", size="20", c="r")
for i in range(16):
    num = np.random.randint(1, len(test_x))
    plt.subplot(4, 4, i + 1)
    plt.title(f"标签值：{test_y[num]}")
    plt.imshow(test_x[num])

plt.tight_layout(rect=[0, 0, 1, 0.9])
plt.show()
