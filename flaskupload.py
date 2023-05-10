import pdfplumber
import time
import os
from flask import Flask, request, render_template, flash, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}


app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB limit
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('loading.html')

# @app.route('/homepage')
# def homepage():
#     return render_template("index2.html")

@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    print(request.method)

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
           

            with pdfplumber.open(file_path) as pdf:
                # extract text from all pages of the PDF
                pages_text = [page.extract_text() for page in pdf.pages]
                # concatenate all pages' text into a single string
                text = '\n'.join(pages_text)
                print('hi',text)
            return render_template('index2.html', text=text)
        else:
            flash('Invalid file type (PDF only)')
            return redirect(request.url)
    return render_template("index2.html")
    

if __name__ == '__main__':
   app.run(debug=True, port=5000)
