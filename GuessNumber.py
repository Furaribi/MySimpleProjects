import random
def get_number(num):
    while True:
        try:
            return int(input(num))
        except ValueError:
            print('Please inter a valid number!')
print('Welcome! Choose the range of number. ')
f_number = get_number("First Number: ")
s_number = get_number("Second Number: ")
random_number = random.randint(f_number, s_number+1)
client_guess = None
counter = 0
while client_guess != random_number:
    counter += 1
    try:
        client_guess = int(input("Guess the number: "))
    except ValueError:
        print("Please inter a valid number!")
    if client_guess > random_number:
        print("you'r guess is bigger than answer.")
    if client_guess < random_number:
        print("you'r guess is smaller than answer.")
print("Yay! you won! The answer was %i and took you %i time to guess the number!" % (random_number, counter))