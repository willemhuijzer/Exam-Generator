from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from openai_api import generate_response
from resp_to_output import response_to_question_answer_pairs
from openai_api import *
from configuration import * # doe weg

app = Flask(__name__)


# set to True to simulate the response (skip the open ai API call)
DO_SIMULATE = True        
# set to True to store the prompt, output and response object
LOG_RESPONSE = False if DO_SIMULATE else True
# set to True to skip the pdf input and use the text input instead (to paste text)
USE_TEXT_ONLY = True    

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def generate():

    content_to_exam_on = 0 # dummy value for simulation

    if USE_TEXT_ONLY:
        content_to_exam_on = request.form.get("text_input", "")

    elif not DO_SIMULATE:
        if 'pdf_input' not in request.files:
            return 'No file part', 400
        
        # Get file from request 
        pdf_file = request.files['pdf_input']
        if pdf_file.filename == '':
            return 'No selected file', 400
    
        content_to_exam_on = extract_text_from_pdf(pdf_file)
        input_questions = request.form.get("text_input", "") # get the text from the text area    

    response = generate_response(content_to_exam_on, simulate_response=DO_SIMULATE, log_response=LOG_RESPONSE)
    exam_questions = response_to_question_answer_pairs(response)

    return render_template("questions.html", exam_questions=exam_questions)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/summarizer")
def summarizer():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
   