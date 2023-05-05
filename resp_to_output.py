import regex as re

def chunk_questions(response:str, question_identifier:str='')->list:
    """Splits response into a list of questions.    
    Args:
        response (str): Response from the GPT API.
    
    Returns:
        list: List of questions and answers.

    Expected format of response:
    %Question% <question number>:
    <question>
    Answer: <answer>

    Where '%' is the question identifier which is subject to change.
    """

    #make regex pattern to search for the start of questions
    pattern = r'{}Question{}\s\d+:\n'.format(question_identifier, question_identifier)

    # Split response into a list of questions with regex
    questions = re.split(pattern, response)[1:]

    # Split questions into a list of questions and answers
    list_of_pairs = [question.split('Answer: ') for question in questions]

    # Remove newline characters from evey element and return list of tuples
    return [(pair[0].strip(), pair[1].strip()) for pair in list_of_pairs]


if __name__ == '__main__':
    response = '''Based on the provided content from chapter slides and previous exam questions, here are three new exam questions:

    %Question% 1:
    Which of the following is NOT a major type of parameter control in Evolutionary Algorithms?
    A. Deterministic
    B. Adaptive
    C. Self-adaptive
    D. Randomized

    Answer: D

    %Question% 2:
    What is the main advantage of adaptive and self-adaptive parameter control in Evolutionary Algorithms?
    A. Increased user control
    B. Reduction in required computing resources
    C. Liberation from parameter tuning and delegating parameter setting to the evolutionary process
    D. Improved predictability of parameter values

    Answer: C

    %Question% 3:
    In the context of varying mutation step size, which option assigns a personal σ to each individual and incorporates this σ into the chromosome?
    A. Option 1
    B. Option 2
    C. Option 3
    D. Option 4

    Answer: C'''

    q_and_a_pair = chunk_questions(response)
    print(q_and_a_pair[0])
