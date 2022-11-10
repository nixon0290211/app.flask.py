from PIL import Image
import numpy as np

im = np.array(Image.open('data/src/lena_square.png'))

im_R = im.copy()
im_R[:, :, (1, 2)] = 0


# 横に並べて結合（どれでもよい）
im_RGB = np.concatenate((im_R, im_G, im_B), axis=1)


pil_img_RGB = Image.fromarray(im_RGB)
pil_img_RGB.save('data/dst/lena_numpy_split_color.jpg')

import numpy as np

