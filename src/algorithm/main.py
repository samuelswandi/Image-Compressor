import matplotlib.pyplot as plt
import time
import numpy as np
from algorithm.compress import *
import io
import base64
import cv2

def main(file, percentage):

    imageWidth, imageHeight, compressedSize = compressedFileSize(file, percentage)
    singularCount = int(compressedSize//((1 + imageWidth + imageHeight)*3))
    start_time = time.time()

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

    except OSError:
        compressedImage = Image.merge("RGB", (imgRed, imgGreen, imgBlue))

    oriImage = np.array(oriImage)
    oriImage = oriImage[:,:,:3]
    compressedImage1 = np.array(compressedImage)

    diff = cv2.absdiff(oriImage.astype(np.float32), compressedImage1.astype(np.float32))
    pixelDiff = round((np.count_nonzero(diff)*100)/diff.size, 2)

    cTime = (time.time() - start_time)

    buffered = io.BytesIO()
    compressedImage.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue())

    return [img_str, cTime, pixelDiff]
