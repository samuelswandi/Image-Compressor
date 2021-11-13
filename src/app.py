import base64
from flask import Flask, flash, request, redirect, url_for, render_template
from algorithm.main import *
import io
from PIL import Image

app = Flask(__name__)
app.secret_key = "secret key"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def uploadImage():
    imageFile = request.files['image-file']
    compressionRate = request.form['compressionRate']

    image  = Image.open(imageFile)
    data = io.BytesIO()
    image.save(data,"PNG")
    encodedImageBefore = base64.b64encode(data.getvalue())

    encodedImageAfter, cTime, pixelDiff = main(imageFile, int(compressionRate)/100)

    return render_template('result.html', imageBefore = encodedImageBefore.decode('utf-8'),imageAfter = encodedImageAfter.decode('utf-8'), pixelPercentage = pixelDiff, compressionTime = cTime)


if __name__ == '__main__':
    app.run(debug = True)