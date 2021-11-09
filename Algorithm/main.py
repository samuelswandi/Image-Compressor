import matplotlib.pyplot as plt
import time
from compress import *

def main(file, percentage):
    Red, Green, Blue, oriImage = openImage(file)

    imageWidth = oriImage.width
    print(imageWidth)
    imageHeight = oriImage.height
    print(imageHeight)
    originalSize = imageWidth * imageHeight * 3

    compressedSize = percentage * originalSize
    singularCount = int(compressedSize//((1 + imageWidth + imageHeight)*3))
    print(singularCount)

    RedCompressed = compress(Red, singularCount)
    GreenCompressed = compress(Green, singularCount)
    BlueCompressed = compress(Blue, singularCount)

    imgRed = (Image.fromarray(RedCompressed, mode=None)).convert('L')
    imgGreen = (Image.fromarray(GreenCompressed, mode=None)).convert('L')
    imgBlue = (Image.fromarray(BlueCompressed, mode=None)).convert('L')

    compressedImage = Image.merge("RGB", (imgRed, imgGreen, imgBlue))

    #  Save Image
    filename = file.split(".")
    compressedImage.save(os.getcwd() + "//Result//" + filename[0] + f"_compressed_{str(percentage*100)[:2]}." + filename[1])

    return compressedImage


if __name__ == "__main__":
    start_time = time.time()
    img = main('lena.png', 0.2)
    plt.imshow(img)
    plt.axis('off')
    plt.show()
    print("--- %s seconds ---" % (time.time() - start_time))