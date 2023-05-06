import openai
from configuration import OPENAI_API_KEY
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

def generate_response(prompt):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        # {"role": "user", "content": "Generate 2 exam questions about the following slides:"},
        {"role": "user", "content": intro + pdf_text + exam_text},
    ]

    # Make an API request to generate text completion
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1600,
        n=1,
    )  
    # Extract and print the generated joke
    output = response['choices'][0]['message']['content']
    return output


file_path = 'input.pdf'
pdf_text = extract_text_from_pdf(file_path)
# print(pdf_text)
intro = '''CONTENT OF LECTURE SLIDES:
'''
exam_text = '''

SAMPLE QUESTIONS: Based on slides that I provide in above, generate 3 exam questions on university level in the following format:
 Question:
    Which of the following is NOT a major type of parameter control in Evolutionary Algorithms?
    A. Deterministic
    B. Adaptive
    C. Self-adaptive
    D. Randomized

    Answer: D

Question:
    What is the main advantage of adaptive and self-adaptive parameter control in Evolutionary Algorithms?
    A. Increased user control
    B. Reduction in required computing resources
    C. Liberation from parameter tuning and delegating parameter setting to the evolutionary process
    D. Improved predictability of parameter values

    Answer: C
    
Generate 5 exam questions based on the provided CONTENT OF LECTURE SLIDES above in the format of the SAMPLE QUESTIONS:
5 QUESTIONS: 
'''
prompt = intro + pdf_text + exam_text
