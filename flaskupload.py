from flask import Flask, request

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB limit

@app.route('/upload', methods=['POST'])
def upload():
    # check if the POST request has a file part
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    # check if the file is a PDF
    if not file.filename.endswith('.pdf'):
        return 'File must be a PDF'

    # check if the file size is within the limit
    if len(file.read()) > app.config['MAX_CONTENT_LENGTH']:
        return 'File size exceeds the limit of 10MB'

    # save the file
    file.save(file.filename)

    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)
