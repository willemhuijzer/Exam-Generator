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
What is the purpose of text normalization?
A. To reduce the effectiveness of NLP models
B. To increase the number of input variables for NLP models
C. To reduce the dimensionality of the input for NLP models
D. To introduce more variations in the words used in the raw text

Answer: C

Question 2:
Which of the following is a component of text normalization?
A. Punctuation addition
B. Contractions reduction
C. Tokenization expansion
D. Stemming removal

Answer: B

Question 3:
What is the advantage of reducing the vocabulary size in NLP?
A. To make the language more difficult to understand
B. To make it easier to identify word variations
C. To minimize the number of features for NLP models
D. To increase the dimensionality of input for NLP models

Answer: C

Question 4:
What is the difference between stemming and lemmatization?
A. Stemming reduces words to their root form, while lemmatization reduces words to base words
B. Stemming and lemmatization are the same thing
C. Stemming reduces words to base words, while lemmatization reduces words to their root form
D. Stemming and lemmatization reduce words to synonyms

Answer: A

Question 5:
Which of the following is an example of a hypernymy relation?
A. Car is a kind of vehicle
B. An air bag is part of a car
C. A tomato is a type of vegetable
D. A book is related to an author

Answer: A

Question 6:
What is entropy in intrinsic evaluation measures of language models?
A. A measure of uncertainty
B. A measure of similarity
C. A measure of frequency
D. A measure of perplexity

Answer: A

Question 7:
Which of the following is a way to measure the performance of n-gram language models in predicting the probabilities of sentences?
A. Intrinsic evaluation measures
B. Extrinsic evaluation measures
C. Stemming-based evaluation measures
D. Tokenization-based evaluation measures

Answer: A

Question 8:
What is the purpose of WordNet in lexical semantics?
A. To solve word sense ambiguity
B. To remove offensive words
C. To provide a list of synonyms for each word
D. To classify relationships between words

Answer: D

Question 9:
What is the main advantage of dense word embeddings?
A. They have fewer parameters
B. They are better at capturing synonymy
C. They are easier to include as features in machine learning systems
D. All of the above

Answer: D

Question 10:
What is the objective function in Word2Vec?
A. To maximize the likelihood of the center word given the context words
B. To maximize the entropy of the center word
C. To minimize the sum of squared errors
D. To minimize the log likelihood of the context words given the center word

Answer: D
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