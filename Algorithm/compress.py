import os
from svd import *
import numpy
from PIL import Image

def openImage(imagePath):
    cwd = os.getcwd()
    imOrig = Image.open(cwd + '\\Image\\' + imagePath)
    im = numpy.array(imOrig)

    aRed = im[:, :, 0]
    aGreen = im[:, :, 1]
    aBlue = im[:, :, 2]

    return [aRed, aGreen, aBlue, imOrig]

def compress(channelDataMatrix, k):
    sChannel, uChannel, vhChannel = svd(channelDataMatrix, k)
    sChannel = np.diag(sChannel)
    
    compressed = uChannel[:, :k] @ sChannel[0:k, :k] @ vhChannel[:k, :]
    return compressed