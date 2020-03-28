# -*- coding:utf-8 -*-
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import boston_housing
from matplotlib.widgets import TextBox
mpl.rcParams['font.family']='Microsoft Yahei'
x, y = boston_housing.load_data(test_split=0)[0]
labels = np.array(['CRIM','ZN','INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO',
                   'B', 'LSTAT'])
fig = plt.figure(figsize=(13,13))
fig.suptitle(u"各个属性与房价的关系",y=1,size=14)
for i in range(0, labels.size):
    plt.subplot(4,4,i+1)
    plt.scatter(x[:,i],y,marker=r'$\heartsuit$',c='r')
    plt.xlabel(labels[i])
    plt.ylabel("price($1000's)")
    plt.title(f"{i+1}.{labels[i]}-Price")
plt.tight_layout()
def submit(text):
    i = eval(text)-1
    ax = plt.axes([0.1, 0.1, 0.85, 0.5])
    ax.scatter(x[:, i], y, marker=r'$\heartsuit$', c='r')
    ax.set_xlabel(labels[i])
    ax.set_ylabel("price($1000's)")
    ax.set_title(f"{i + 1}.{labels[i]}-Price")

fig = plt.figure(figsize=(7,7))
tBox = TextBox(plt.axes([0.16, 0.9, 0.7, 0.05]),u'请选择属性:')
tax = plt.axes([0.16, 0.6, 0.7, 0.3])
tax.set_xticks([])
tax.set_yticks([])
for i in range(0,labels.size):
    tax.text(0.01,.9-i/15, f'{i+1} -- {labels[i]}')

tBox.on_submit(submit)
plt.show()