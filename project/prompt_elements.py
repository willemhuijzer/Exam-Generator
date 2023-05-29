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