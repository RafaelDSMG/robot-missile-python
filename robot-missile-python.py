import random

print("ROBOT MISSILE")
code = chr (65+random.randint(1,26))

for attempt in range(4):
    guess = input("Guess a letter (A-Z)   ").upper()


    if guess == code: 
        print("TICK....FZZZZZ...CLICK.")
        print("YOU DID IT!!")
        break
    elif guess < code : 
        print(f"LATER than {guess}")
    elif guess > code :
        print(f"EARLIER than {guess}")
else:
        print("BOOOOOOOOOM!")
        print(f"YOU BLEW IT. the correct code was : {guess}")
