import os
import numpy
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from algorithm.svd import *
from PIL import Image

def openImage(imagePath):
    cwd = os.getcwd()
    imOrig = Image.open(imagePath)
    im = numpy.array(imOrig)

    aRed = im[:, :, 0]
    aGreen = im[:, :, 1]
    aBlue = im[:, :, 2]

    return [aRed, aGreen, aBlue]

def openImageAlpha(imagePath):
    cwd = os.getcwd()
    imOrig = Image.open(imagePath)
    imOrig = imOrig.convert("RGBA")
    im = numpy.array(imOrig)
    # print(im.shape)

    aRed = im[:, :, 0]
    aGreen = im[:, :, 1]
    aBlue = im[:, :, 2]
    aAlpha = im[:, :, 3]

    return [imOrig, aRed, aGreen, aBlue, aAlpha]

def compress(channelDataMatrix, k):
    channelDataMatrix = channelDataMatrix.astype(np.float32)
    sChannel, uChannel, vhChannel = svd_test(channelDataMatrix, k)
    sChannel = np.diag(sChannel)
    
    compressed = uChannel[:, :k] @ sChannel[:k, :k] @ vhChannel[:k, :]
    return compressed

def compressedFileSize(file, percentage):
    cwd = os.getcwd()
    oriImage = Image.open(file)
    imageWidth = oriImage.width
    imageHeight = oriImage.height
    originalSize = imageWidth * imageHeight * 3

    compressedSize = percentage * originalSize
    return (imageWidth, imageHeight, compressedSize)

# def predictCompressTime(compressedSize):
#     compressedSize = compressedSize/1000000
#     X = [0.00786432, 0.047185920000000006, 0.08650752000000002, 0.12582912000000002, 0.16515072000000003, 0.20447232, 0.24379392, 0.28311552, 0.32243712, 0.36175872, 0.40108032, 0.44040192000000006, 0.47972352000000007, 0.5190451200000001, 0.5583667200000002, 0.5976883200000002, 0.6370099200000001, 0.6763315200000003, 0.7156531200000004, 0.7549747200000003]
#     y = [0.09598350524902344, 0.9020004272460938, 2.2789993286132812, 4.25800347328186, 7.046996355056763, 10.584001064300537, 15.091003894805908, 21.29899549484253, 25.659998893737793, 32.31500005722046, 39.7850022315979, 48.887956380844116, 59.374056577682495, 73.39800572395325, 79.09054970741272, 87.6819760799408, 102.432461977005, 122.51761865615845, 136.6737928390503, 148.09551453590393]

#     X = np.array(X)
#     X = X.reshape(-1, 1)
#     y = np.array(y)

#     poly = PolynomialFeatures(degree = 4)
#     x_poly = poly.fit_transform(X)
#     poly.fit(x_poly, y)
#     lin = LinearRegression()
#     lin.fit(x_poly, y)

#     return lin.predict(poly.fit_transform([[compressedSize]]))