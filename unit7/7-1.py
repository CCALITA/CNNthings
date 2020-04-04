# -*- coding:utf-8 -*-
from PIL import Image
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = "Microsoft Yahei"
plt.rcParams["axes.unicode_minus"] = False
img = Image.open("lena.tiff")
img_r, img_g, img_b = img.split()
img_r_result = img_r.resize((50,50))
plt.figure()
plt.suptitle("图像基本操作", fontsize="22", c="b")
plt.subplot(221)
plt.axis("off")
plt.title("R-缩放", fontsize="14")
plt.imshow(img_r_result, cmap="gray")

img_g_result = img_g.transpose(Image.FLIP_LEFT_RIGHT)
img_g_result = img_g.transpose(Image.ROTATE_270)
plt.subplot(222)
plt.title("G-镜像+旋转", fontsize="14")
plt.imshow(img_g_result, cmap="gray")

img_b_result = img_b.crop((0, 0, 150, 150))
plt.subplot(223)
plt.axis("off")
plt.title("B-裁剪", fontsize="14")
plt.imshow(img_b_result, cmap="gray")

img_result = Image.merge("RGB", [img_r, img_g, img_b])
plt.subplot(224)
plt.axis("off")
plt.title(img_result.mode, fontsize="14")
plt.imshow(img_result)
img_result.save("test.png")

plt.tight_layout(rect=[0,0,1,0.9])
plt.show()
