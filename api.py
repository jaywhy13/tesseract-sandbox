import uuid
import os

from flask import Flask, request, flash, url_for
from flask import render_template, redirect, jsonify
from werkzeug import SharedDataMiddleware
import cv2
import pytesseract
from PIL import Image


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.add_url_rule('/preview/<image_id>', 'preview',
                 build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/uploads':  app.config['UPLOAD_FOLDER']
})
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


@app.route("/")
def home():
    return render_template('home.html')


def get_file_from_request(request):
    if "image" not in request.files:
        return None
    image = request.files["image"]
    return image if image.filename else None


def get_image_filename(image_id):
    matches = [
        file for file in os.listdir(UPLOAD_FOLDER)
        if image_id == os.path.splitext(file)[0]]
    return matches[0]


def get_image_path(image_id):
    return os.path.join(UPLOAD_FOLDER, get_image_filename(image_id))


def save_image(image):
    """ Saves the image and returns the ID
    """
    ext = os.path.splitext(image.filename)[1] or ".jpg"
    filename = "{}{}".format(str(uuid.uuid1()), ext)
    image.save(os.path.join(UPLOAD_FOLDER, filename))
    return os.path.splitext(filename)[0]

@app.route("/upload", methods=['POST'])
def upload():
    image = get_file_from_request(request)
    if not image:
        flash("Please upload an image", category="error")
        return redirect(url_for("home"))
    image_id = save_image(image)
    return redirect(url_for("preview", image_id=image_id))
