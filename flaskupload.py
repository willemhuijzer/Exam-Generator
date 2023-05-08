import pdfplumber
from flask import Flask, request, render_template

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB limit

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # check if the POST request has a file part
    if 'file' not in request.files:
        return render_template('index2.html', text='No file part')

    file = request.files['file']

    # check if the file is a PDF
    if not file.filename.endswith('.pdf'):
        return render_template('index2.html', text='File must be a PDF')


    # check if the file size is within the limit
    if len(file.read()) > app.config['MAX_CONTENT_LENGTH']:
        return render_template('index2.html', text='File size exceeds the limit of 10MB')


    with pdfplumber.open(file) as pdf:
        # extract text from all pages of the PDF
        pages_text = [page.extract_text() for page in pdf.pages]
        # concatenate all pages' text into a single string
        text = '\n'.join(pages_text)

    return render_template('index2.html', text=text)


if __name__ == '__main__':
   app.run(debug=True,port=8080)
