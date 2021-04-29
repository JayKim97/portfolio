from flask import Flask, render_template, request, redirect, url_for
from asciiTrans import asciiTran
from recipeFinder import createRandom, recipeData
from base64 import b64encode
import numpy
import cv2
import os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/ascii', methods=['GET', 'POST'])
def ascii_page():
    if request.method == 'POST':
        res, ori_img = asciiTran(cv2.imdecode(numpy.fromstring(
            request.files['file-3[]'].read(), numpy.uint8), cv2.IMREAD_UNCHANGED))

        return render_template('ascii.html', img_src=res.decode('utf-8'), img_ori=ori_img.decode('utf-8'))
    elif request.method == 'GET':
        return render_template('ascii.html')


@app.route('/recipefinder', methods=['GET', 'POST'])
def recipe_page():
    if request.method == "POST":
        curIngs = request.form['ings']
        file = os.path.join(
            app.root_path, 'static/recipeFinder', "recipeData.txt")
        possibleRec, uing, oldrec = recipeData(file, curIngs)
        return render_template('recipeFinder.html',  newIngs=uing, recipes=oldrec, newrecipes=possibleRec)

    elif request.method == 'GET':
        file = os.path.join(
            app.root_path, 'static/recipeFinder', "ingredients.txt")
        file2 = os.path.join(
            app.root_path, 'static/recipeFinder', "recipeData.txt")
        current, possibleRec = createRandom(file, file2)
        return render_template('recipeFinder.html', curIngs=current, recipes=possibleRec)


if __name__ == '__main__':
    app.run(host='127.0.0.1')
