import matplotlib.pyplot as plt
import time
import numpy as np
from compress import *

def main(file, percentage):
    Red, Green, Blue, oriImage = openImage(file)

    imageWidth, imageHeight, compressedSize = compressedFileSize(file, percentage)
    singularCount = int(compressedSize//((1 + imageWidth + imageHeight)*3))

    RedCompressed = compress(Red, singularCount)
    GreenCompressed = compress(Green, singularCount)
    BlueCompressed = compress(Blue, singularCount)

    imgRed = (Image.fromarray(RedCompressed, mode=None)).convert('L')
    imgGreen = (Image.fromarray(GreenCompressed, mode=None)).convert('L')
    imgBlue = (Image.fromarray(BlueCompressed, mode=None)).convert('L')

    compressedImage = Image.merge("RGB", (imgRed, imgGreen, imgBlue))

    # Save Image
    filename = file.split(".")
    compressedImage.save(os.getcwd() + "//Result//" + filename[0] + f"_compressed_{str(percentage*100)[:2]}." + filename[1])

    return compressedImage


if __name__ == "__main__":
    print(f"Estimated Compressed Time: {predictCompressTime(compressedFileSize('image.png', 0.5)[2])}")
    start_time = time.time()
    img = main('image.png', 0.5)
    plt.imshow(img)
    plt.axis('off')
    print("--- %s seconds ---" % (time.time() - start_time))
    plt.show()