📝 Flask App - Convert Slides to Practice Exam UI

This is a Flask web application that takes uploaded slide decks and converts them into a practice exam UI. The application uses OpenAI's GPT to generate questions based on the content of the slides.

📁 File Structure

All the main files are under the project folder.

- app.py : Runs the Flask code
- openai_api.py: Gets the GPT output
- resp_to_output.py: Chunks the API output to questions and options
template folder:
- index.html: The main page of the app
- results.html: The page where the questions are displayed
- questions.html: The page where the user can select the answers to the questions


🚀 How to Run the App

Clone the repository to your local machine
Install the dependencies by running pip install -r requirements.txt
Run the app using python app.py
Open your browser and go to http://localhost:5000
💡 How to Use the App

Upload your slide deck using the file input on the main page
Click the button you see to generate the questions
The app will display the questions on the "Results" page
Select your answers and submit
- as a sample use the input file give here "input.pdf". Mostly works!
The app will display your score on the "Questions" page
🔑 API Keys

This application requires an OpenAI API key. Please refer to the OpenAI documentation on how to obtain an API key.
- create a configuration.py file 
- add the key there with variable named as OPENAI_KEY
- ex: OPENAI_KEY = "asghh...."

📌 Note

This is a proof-of-concept application and is not intended for production use. It has not been extensively tested and may contain bugs or errors. Use at your own risk.
