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


@app.route("/upload", methods=['POST'])
def upload():
    pass
