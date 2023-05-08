import openai
from configuration import *
import pdfplumber

openai.api_key = OPENAI_API_KEY

def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        num_pages = len(pdf.pages)
        text = ''
        for page_num in range(num_pages):
            page = pdf.pages[page_num]
            text += page.extract_text()
    return text

def generate_response(pdf_text, simulate_response=False):

    if simulate_response:
        return response_simulated
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": INTRO + pdf_text + EXAM_TEXT},
    ]

    # Make an API request to generate text completion
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1600,
        n=1,
    )  
    output = response['choices'][0]['message']['content']
    return output


response_simulated = '''Based on the provided content from chapter slides and previous exam questions, here are three new exam questions:

Question 1:
Which of the following is NOT a major type of parameter control in Evolutionary Algorithms?
A. Deterministic
B. Adaptive
C. Self-adaptive
D. Randomized

Answer: D

Question 2:
What is the main advantage of adaptive and self-adaptive parameter control in Evolutionary Algorithms?
A. Increased user control
B. Reduction in required computing resources
C. Liberation from parameter tuning and delegating parameter setting to the evolutionary process
D. Improved predictability of parameter values

Answer: C

Question 3:
In the context of varying mutation step size, which option assigns a personal σ to each individual and incorporates this σ into the chromosome?
A. Option 1
B. Option 2
C. Option 3
D. Option 4

Answer: C'''