from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from openai_api import generate_response
from resp_to_output import response_to_question_answer_pairs
from openai_api import *
from configuration import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def generate():
    if 'pdf_input' not in request.files:
        return 'No file part', 400
    pdf_file = request.files['pdf_input']
    if pdf_file.filename == '':
        return 'No selected file', 400
    
    pdf_text = extract_text_from_pdf(pdf_file)
    response = generate_response(pdf_text, simulate_response=False)
    exam_questions = response_to_question_answer_pairs(response)

    return render_template("questions.html", exam_questions=exam_questions)


if __name__ == "__main__":
    app.run(debug=True)
   