"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Ondřej Kalvas
email: kalvasondrej@gmail.com
discord: Ondřej K.#0612
"""
import random
import inflect

p = inflect.engine()
number = []
tries = 0
list_of_used_numbers = []

def generate_number():
    for guessed_number in range(4):
        guessed_number = random.randrange(0, 9)
        number.append(guessed_number)
    if number[0] == 0:
        number.clear()
        generate_number()
    if len(number) > len(set(number)):
        number.clear()
        generate_number()

def game():
    global tries
    tries += 1
    bulls = 0
    cows = 0
    user_number = input(">>>")
    guess = []
    if user_number.isnumeric() and int(user_number) in range(1000, 10000):
        if user_number not in list_of_used_numbers:
            list_of_used_numbers.append(user_number)
            for i in range(4):
                guess.append(int(user_number[i]))
            if len(guess) <= len(set(guess)):
                for i in range (4):
                    for j in range (4):
                        if guess[i] == number[j]:
                            cows += 1
                for x in range(4):
                    if guess[x] == number[x]:
                        bulls += 1
                print(
                    bulls, p.plural("bull", bulls), ",",
                    cows, p.plural("cow", cows)
                )
                print("-" * 62)
                if bulls == 4:
                    print("Correct, you've guessed the right number in", tries, "guesses!")
                elif bulls != 4:
                    game()
            else:
                print("Your number contains duplicates.")
                print("-" * 62)
                game()
        else:
            print("You have already tried this number. Try another one.")
            print("-" * 62)
            game()
    else:
        print("It must be a four-digit number and must not start with a zero.")
        print("-" * 62)
        game()

print("I've generated a random 4 digit number for you.\n"
      "Let's play a bulls and cows game.")
print("-" * 62)
print("Enter a number:")
print("-" * 62)

generate_number()
game()