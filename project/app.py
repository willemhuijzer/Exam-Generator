from flask import Flask, render_template, request
from openai_api import generate_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def generate():
    text_input = request.form.get("text_input")
    response = generate_response(text_input)
    return render_template("result.html", response=response)


@app.route("/results", methods=["POST"])
def results():
    text = request.form["text"]
    questions = generate_questions(text)
    return render_template("results.html", questions=questions)


if __name__ == "__main__":
    app.run(debug=True)
