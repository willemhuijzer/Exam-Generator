import regex as re
from pprint import pprint

def split_questions(response, question_identifier):

    #make regex pattern to search for the start of questions
    pattern = r'{}Question{}\s\d+:\n'.format(question_identifier, question_identifier)

    try:
        # Split response into a list of questions with regex
        return re.split(pattern, response)[1:]
    except IndexError:
        # If no questions are found, return empty list
        return []


def disect_question_options_answer(exam_question:str)->dict:
    """Splits question into question, options, and answer.
    
    Args:
        `exam_question` (str): Question from the GPT API.
    
    Returns:
        dict: Dictionary of question, options, and answer.
    """

    # identify question
    question = exam_question.split('\nA. ')[0].strip()

    # identify options
    options = "A. " + exam_question.split('A. ')[1].split('Answer: ')[0].strip()

    pattern = r'[A-Z]\.\s.+'
    options = re.findall(pattern, options)
    
    # identify answer
    answer = exam_question.split('Answer: ')[1].strip()

    return {'question': question, 'options': options, 'answer': answer}


def response_to_question_answer_pairs(response:str, question_identifier:str='')->list:
    """Splits response into a list of questions.    
    Args:
        response (str): Response from the GPT API.
    
    Returns:
        list: List of {'answer': <answer>, 'question': <question>, 'options': <options>}

    Expected format of response:
    %Question% <question number>:
    <question>
    Answer: <answer>

    Where '%' is the question identifier which is subject to change.
    """
    #cast response to string
    response = str(response)

    # Split response into a list of questions
    questions = split_questions(response, question_identifier)

    # If no questions are found, return empty list
    if not questions:
        return []

    # Disect questions into question, options, and answer
    exam = [disect_question_options_answer(question) for question in questions]

    pprint(exam)

    return exam

    # Split questions into a list of questions and answers
    list_of_pairs = [question.split('Answer: ') for question in questions]

    # Remove newline characters from evey element and return list of tuples
    return [(pair[0].strip(), pair[1].strip()) for pair in list_of_pairs]


if __name__ == '__main__':
    response = '''Based on the provided content from chapter slides and previous exam questions, here are three new exam questions:

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

    q_and_a_pair = response_to_question_answer_pairs(response)
    print(q_and_a_pair[0])
