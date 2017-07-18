from flask import Flask, request
from flask import render_template

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/upload", methods=['POST'])
def upload():
    pass
