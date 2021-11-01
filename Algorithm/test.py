from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = Image.open("algorithm/image.png")
np_img = np.array(img)

print(type(np_img))
plt.imshow(img)
plt.show()