from flask import Flask, render_template, request, redirect
from asciiTrans import asciiTran
import numpy
import cv2

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/ascii', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        res = asciiTran(cv2.imdecode(numpy.fromstring(
            request.files['file'].read(), numpy.uint8), cv2.IMREAD_UNCHANGED))
        return render_template('ascii.html', img_src=res.decode('utf-8'))
    elif request.method == 'GET':
        return render_template('ascii.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1')
