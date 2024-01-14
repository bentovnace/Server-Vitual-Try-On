from flask import Flask, request, jsonify, abort, render_template, redirect, Response, send_file
from PIL import Image
import io
import base64
import numpy as np 
from flask_cors import CORS, cross_origin
from Remove_background import remove_background
import cv2
import time
import random
global outputfile
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET', 'POST'])
@cross_origin(origin='*')
def Home():
    return "Welcome to my Vitual Try On Application"


@app.route('/image_capture_remove_bg', methods=['GET', 'POST'])
@cross_origin(origin='*')
def Img_Capture_Remove_Bg():
    global name_img,outputfile

    if not request.json or 'image' not in request.json:
        abort(400)

    im_b64 = request.json['image']
    img_bytes = base64.b64decode(im_b64.encode('utf-8'))
    timestr = time.strftime("%Y%m%d_%H%M%S")
    print(timestr)
    name_img = str(random.randint(1, 10000)) + str(random.randint(1, 1000)) + "Day" + timestr + ".png"
    filename = "Image_Capture\\" + name_img
    with open(filename, 'wb') as f:
        f.write(img_bytes)
    inputfile =filename
    outputfile ="Remove_background\\"+name_img
    remove_background(inputfile, outputfile)
    image_file = outputfile
    with open(image_file, "rb") as f:
        im_bytes = f.read()        
    im_b64 = base64.b64encode(im_bytes).decode("utf8")

    return str(im_b64)







@app.route('/clothes_change_dowload', methods=['GET','POST'])
def Clothes_chage_img_send():
    global save
    image_file = save
    with open(image_file, "rb") as f:
        im_bytes = f.read()        
    im_b64 = base64.b64encode(im_bytes).decode("utf8")

    return str(im_b64)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='6868')

    # Call the base64_to_img function after the Flask app is run

