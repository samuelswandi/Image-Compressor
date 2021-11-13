import matplotlib.pyplot as plt
import time
import numpy as np
import cv2
from compress import *

def main(file, percentage):

    imageWidth, imageHeight, compressedSize = compressedFileSize(file, percentage)
    singularCount = int(compressedSize//((1 + imageWidth + imageHeight)*3))

    try:
        oriImage, Red, Green, Blue, Alpha = openImageAlpha(file)
        RedCompressed = compress(Red, singularCount)
        GreenCompressed = compress(Green, singularCount)
        BlueCompressed = compress(Blue, singularCount)

        imgRed = (Image.fromarray(RedCompressed, mode=None)).convert('L')
        imgGreen = (Image.fromarray(GreenCompressed, mode=None)).convert('L')
        imgBlue = (Image.fromarray(BlueCompressed, mode=None)).convert('L')
        imgAlpha = (Image.fromarray(Alpha, mode=None)).convert('L')

        compressedImage = Image.merge("RGBA", (imgRed, imgGreen, imgBlue, imgAlpha))
        
        filename = file.split(".")
        compressedImage.save(os.getcwd() + "//Result//" + filename[0] + f"_compressed_{str(percentage*100)[:2]}." + filename[1])

    except OSError:
        compressedImage = Image.merge("RGB", (imgRed, imgGreen, imgBlue))

        filename = file.split(".")
        compressedImage.save(os.getcwd() + "//Result//" + filename[0] + f"_compressed_{str(percentage*100)[:2]}." + filename[1])

    oriImage = np.array(oriImage)
    oriImage = oriImage[:,:,:3]
    compressedImage = np.array(compressedImage)

    diff = cv2.absdiff(oriImage.astype(np.float32), compressedImage.astype(np.float32))
    pixelDiff = round((np.count_nonzero(diff)*100)/diff.size, 2)
    print(pixelDiff)

    # Save Image
    # filename = file.split(".")
    # compressedImage.save(os.getcwd() + "//Result//" + filename[0] + f"_compressed_{str(percentage*100)[:2]}." + filename[1])

    return compressedImage


if __name__ == "__main__":
    print(f"Estimated Compressed Time: {predictCompressTime(compressedFileSize('binjai.jpeg', 0.6)[2])}")
    start_time = time.time()
    img = main('binjai.jpeg', 0.6)
    plt.imshow(img)
    plt.axis('off')
    print("--- %s seconds ---" % (time.time() - start_time))
    plt.show()