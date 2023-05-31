SLIDES_PREFACE = '''CONTENT OF LECTURE SLIDES:
'''
SUMMARY_PREFACE = '''SUMMARY OF LECTURES:
'''
EXAMPLE_QUESTIONS = '''Question 1:
EA parameters are rigid (values constant during a run).
A. True
B. False

Answer: B

Question 2:
What is the main advantage of adaptive and self-adaptive parameter control in Evolutionary Algorithms?
A. Increased user control
B. Reduction in required computing resources
C. Liberation from parameter tuning and delegating parameter setting to the evolutionary process
D. Improved predictability of parameter values

Answer: C
'''

SIMULATED_RESPONSE = '''
Question 1:
What is Natural Language Processing (NLP)?
A. The branch of computer science concerned with giving computers the ability to understand images and videos.
B. The branch of artificial intelligence concerned with giving computers the ability to perform complex mathematical computations.
C. The branch of computer science concerned with giving computers the ability to understand text and spoken words in much the same way human beings can.
D. The branch of computer science concerned with developing algorithms that can learn from data.

Answer: C

Question 2:
What are the different technologies combined in NLP?
A. Computational linguistics, machine learning, and deep learning models.
B. Robotics, computer vision, and natural language modeling.
C. Computer graphics, computer vision, and machine learning models.
D. None of the above.

Answer: A

Question 3:
What is meant by the compositional property of natural language?
A. The choice of words to describe someone is quite arbitrary.
B. The meaning of a whole expression is a function of the meaning of its parts and the manner in which they are put together.
C. New words are created all the time.
D. None of the above.

Answer: B

Question 4:
What is meant by the displaced property of natural language?
A. The ability to talk about things that are not here or do not exist.
B. The choice of words to describe someone is quite arbitrary.
C. New words are created all the time.
D. None of the above.

Answer: A

Question 5:
What is meant by the ambiguity property of natural language?
A. Certain words can mean a lot of things.
B. The choice of words to describe someone is quite arbitrary.
C. New words are created all the time.
D. None of the above.

Answer: A

Question 6:
What is Zipf's law?
A. The rank-frequency distribution of words is an inverse relation.
B. The frequency of a word is directly proportional to the rank of that word.
C. All words follow a normal distribution.
D. None of the above.

Answer: A

Question 7:
Why is handling variation in language difficult for NLP?
A. Because one form can have different meanings.
B. Because the same meaning can be expressed with different forms.
C. Because different types of language use require different models.
D. All of the above.

Answer: C

Question 8:
What is the context-dependence property of natural language?
A. The correct interpretation is context-dependent and often requires world knowledge.
B. The frequency of a word is directly proportional to the rank of that word.
C. All words follow a normal distribution.
D. None of the above.

Answer: A

Question 9:
What is one issue with natural language being often spoken and grounded?
A. It is too easy for computers to understand spoken language.
B. It requires a lot of computing resources to understand spoken language.
C. It is difficult to represent spoken language in a computational system.
D. None of the above.

Answer: C

Question 10:
What technologies enable computers to process human language in the form of text and voice data?
A. Computational linguistics, machine learning, and deep learning models.
B. Robotics, computer vision, and natural language modeling.
C. Computer graphics, computer vision, and machine learning models.
D. None of the above.

Answer: A
'''

def prompt_preface(content_nature:str='slides'):
    if content_nature == 'slides':
        return SLIDES_PREFACE
    elif content_nature == 'summary':
        return SUMMARY_PREFACE
    else:
        raise ValueError(f'content_nature must be either slides or summary. "{content_nature}" is not a valid value yet.')


def prompt_instruction(num_of_questions:int=5, example_questions:str='', content_nature:str='slides', difficulty_level:str='university'):
    content = "CONTENT OF THE LECTURE SLIDES" if content_nature == 'slides' else "SUMMARY OF THE LECTURES"
    return f'''

SAMPLE QUESTIONS: Based on the {content_nature} that I provide in above, generate {num_of_questions} multiple choice exam questions on {difficulty_level} level in the following format:

{example_questions}


Generate {num_of_questions} exam questions based on the provided {content} above in the format of the SAMPLE QUESTIONS:
{num_of_questions} QUESTIONS: 
'''

# '''Which of the following is not a strategy parameter in EA?
# a) mutation rate
# b) crossover operator
# c) selection mechanism
# d) population color

# EA parameters are rigid (values constant during a run).
# a) True
# b) False

# Which of the following statements is false?
# a) EA has many strategy parameters.
# b) Good parameter values facilitate good performance.
# c) Optimal parameter values may vary during a run.
# d) EA parameters are not rigid.

# Which of the following statements are true regarding varying mutation step size?
# a) The constant σ can be replaced by a function σ(t) updated after every n steps by the 1/5 success rule.
# b) The constant σ can be replaced by a function σ (t) = 1 - 0.9 × Tt, where t is the current generation number.
# c) A personal σ can be assigned to each individual and incorporated into the chromosome.
# d) A personal σ can be assigned to each variable in each individual and incorporated into the chromosome.

# '''
# #c