import random

print("Loja gjeje numrin\n")

guesses = 0
number = random.randint(0, 100)

while( guesses < 5 ):
    u_guess = int(input("Supozo nje numer nga 0 deri ne 100: "))

    if u_guess == number:
        print("Ju e gjetet numrin! Ju fituat!")
        break
    elif u_guess > number:
        print("Numri qe keni zgjedhur eshte shume i madh.")
        guesses = guesses + 1
    elif u_guess < number:
        print("Numri qe keni zgjedhur eshte shume i vogel.")
        guesses = guesses + 1
    else:
        print("Kemi nje error.")

if guesses == 5:
    print("Ju nuk e gjetet numrin! Ju e humbet lojen!")
    print("Numri eshte: " + str(number))