from flask import Flask, render_template, request
from openai_api import generate_response
from resp_to_output import response_to_question_answer_pairs

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def generate():
    text_input = request.form.get("text_input")
    response = generate_response(text_input)
    exam_questions = response_to_question_answer_pairs(response)

    return render_template("result.html", exam_questions=exam_questions)


@app.route("/results", methods=["POST"])
def results():
    text = request.form["text"]
    questions = generate_questions(text)
    return render_template("results.html", questions=questions)


if __name__ == "__main__":
    app.run(debug=True)
            