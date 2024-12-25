def q_print(question):
    print(question)

def a_print(answers):
    for answer in answers:
        print(answer)

question1 = {
    'question' : 'what is capital of brazil?',
    'answers' : ['A. santiago', 'B. brasilia', 'C. São Paulo', 'D. Rio de janeiro'],
}
question2= {
    'question' : "which part of digestive system won't absorb water?",
    'answers' : ['A. small intestine ', 'B. large intestine', 'C. esophagus', 'D. mouth'],
}
question3= {
    'question' : 'who writes The miserable book?',
    'answers' : ['A. Victor Hugo', 'B. Charles Dickens', 'C. William Shakespeare', 'D.  Jack Higgins']
}
question4= {
    'question' : 'which Empire is largest in History?',
    'answers' : ['A. British Empire', 'B. Mongol Empire', 'C. Persian Empire', 'D. Abbasid Empire']
}
question5= {
    'question' : 'choose the answer of: 144 / 3(2 + 2 * 3)',
    'answers' : ['A. 4', 'B. 6', 'C. 384', 'D. 128']
}

questions = [question1, question2, question3, question4, question5]
key = ['B', 'C', 'A', 'A', 'B']
correct_counter = 0
for i in range(0, 5):
    q_print(questions[i]['question'])
    a_print(questions[i]['answers'])
    client_answer = str(input('pls inter your answer choice: '))
    if client_answer.lower() == key[i].lower():
        correct_counter += 1
print('you correctly answered %i question!' % (correct_counter))