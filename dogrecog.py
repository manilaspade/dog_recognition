from PIL import Image
import numpy as np

image = Image.open('pugs.jpg')
image = Image.open('sharpei.jpg')

imsize = np.array(image).shape[:-1]
# imx = imsize[1]/4
# imy = imsize[0]/3

k = 0
for i in range(imsize[1]/175):
    for j in range(imsize[0]/175):
        k+=1
        image_c = image.crop([imx*i, imy*j, imx*(i+1), imy*(j+1)])
        image_c.show()
        image_c.save('%d%d.png' %(i,j))

        cnn_dog('%d%d.png' %(i,j), k, categories_dog, func, verbose=True)
