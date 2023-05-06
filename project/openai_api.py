import openai
from project.configuration import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_response(text_input):
    return "prompt: " + text_input + "\n\nResponse: " + "Test"

    response = openai.Completion.create(
        engine="davinci",
        prompt=text_input,
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.3,
        stop=["\n", " Human:", " AI:"]
    )
    return response.choices[0].text