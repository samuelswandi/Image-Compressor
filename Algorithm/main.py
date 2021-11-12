import matplotlib.pyplot as plt
import time
import numpy as np
from compress import *

def main(file, percentage):

    imageWidth, imageHeight, compressedSize = compressedFileSize(file, percentage)
    singularCount = int(compressedSize//((1 + imageWidth + imageHeight)*3))

    try:
        Red, Green, Blue, Alpha = openImageAlpha(file)
        RedCompressed = compress(Red, singularCount)
        GreenCompressed = compress(Green, singularCount)
        BlueCompressed = compress(Blue, singularCount)
        # AlphaCompressed = Alpha
        # AlphaCompressed = compress(Alpha, singularCount)

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
        # Red, Green, Blue = openImage(file)


    # AlphaCompressed = compress(Alpha, singularCount)
    # imgAlpha = (Image.fromarray(AlphaCompressed, mode=None)).convert('L')

    # try:
    #     compressedImage = Image.merge("RGBA", (imgRed, imgGreen, imgBlue, imgAlpha))
    # except OSError:
    #     compressedImage = Image.merge("RGB", (imgRed, imgGreen, imgBlue))

    # Save Image
    # filename = file.split(".")
    # compressedImage.save(os.getcwd() + "//Result//" + filename[0] + f"_compressed_{str(percentage*100)[:2]}." + filename[1])

    return compressedImage


if __name__ == "__main__":
    print(f"Estimated Compressed Time: {predictCompressTime(compressedFileSize('lena.png', 0.6)[2])}")
    start_time = time.time()
    img = main('lena.png', 0.6)
    plt.imshow(img)
    plt.axis('off')
    print("--- %s seconds ---" % (time.time() - start_time))
    plt.show()