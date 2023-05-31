import openai
from configuration import *
import pdfplumber
from prompt_elements import *
import time, os

openai.api_key = OPENAI_API_KEY

NUM_OF_QUESTIONS = 10

def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        num_pages = len(pdf.pages)
        text = ''
        for page_num in range(num_pages):
            page = pdf.pages[page_num]
            text += page.extract_text()
    return text

def generate_response(content_to_exam_on, content_nature='slides', simulate_response=False, log_response=False):
    """Generates a response based on the provided text.

    Args:
        `content_to_exam_on` (str): Text to generate a response from.\n
        `content_nature` (str, optional): Description of the content the users whats to be examed on. Defaults to 'slides'.\n
        `simulate_response` (bool, optional): Whether to simulate the response. Defaults to False.\n
        `log_response` (bool, optional): Whether the openai response should be logged as a textfile.\n
        
    Returns:
        str: Response from the GPT API.
    """

    if simulate_response:
        return SIMULATED_RESPONSE
    
    #find current time
    time_of_api_call = time.strftime("%y|%m|%d-%H:%M:%S")
    
    # Generate prompt
    prompt = prompt_preface(content_nature=content_nature) \
                + content_to_exam_on \
                + prompt_instruction(
                    num_of_questions=NUM_OF_QUESTIONS,
                    example_questions=EXAMPLE_QUESTIONS,
                    content_nature=content_nature,
                    difficulty_level='university')

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]

    # Make an API request to generate text completion
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1600,
        n=1,
    )  
    output = response['choices'][0]['message']['content']

    if log_response:
        #create a folder for this response
        log_path = f"project/response_logger/{time_of_api_call}"
        os.mkdir(log_path)
        # store the prompt
        with open(f"{log_path}/prompt.txt", "w") as file_object:
            file_object.write(prompt)
        # store the output
        with open(f"{log_path}/output.txt", "w") as file_object:
            file_object.write(output)
        # store the whole response object 
        with open(f"{log_path}/response_full.txt", "w") as file_object:
            file_object.write(str(response))
    
    return output
