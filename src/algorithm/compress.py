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

    print(im.shape)
    aRed = im[:, :, 0]
    aGreen = im[:, :, 1]
    aBlue = im[:, :, 2]

    return [aRed, aGreen, aBlue]

def openImageAlpha(imagePath):
    cwd = os.getcwd()
    imOrig = Image.open(imagePath)
    imOrig = imOrig.convert("RGBA")
    im = numpy.array(imOrig)
    print(im.shape)

    aRed = im[:, :, 0]
    aGreen = im[:, :, 1]
    aBlue = im[:, :, 2]
    aAlpha = im[:, :, 3]

    return [imOrig, aRed, aGreen, aBlue, aAlpha]

def compress(channelDataMatrix, k):
    channelDataMatrix = channelDataMatrix.astype(np.float32)
    sChannel, uChannel, vhChannel = svdPowerIteration(channelDataMatrix, k)
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