import random
def valid_guess(guessed, correct_word):
    global M_word
    index = 0
    while index < len(correct_word):
        if guessed == correct_word:
            M_word = correct_word
            break
        index = correct_word.find(guessed, index)
        if index == -1:
            break
        M_word = M_word[:index] + guessed + M_word[index+1:]
        index += 1

list_lang = ['Html', 'css', 'javascript', 'binary', 'python', 'java', 'powershell', 'kotlin', 'rust', 'assembly', 'swift', 'perl',
             'ruby', 'scala', 'matlab', 'dart', 'lua', 'bash', 'shell', 'csharp', 'php']
C_word = random.choice(list_lang)
M_word = len(C_word) * '-'
print('This is a hangman game for programming languages!')
while True:
    print('the word right now is: ', M_word)
    guess = str(input("Please guess in single letter: ")).lower()
    valid_guess(guess, C_word)
    if C_word == M_word:
        break
print('You won! The word was %s!' % C_word)