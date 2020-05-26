import random

def valid():
    typeOfGuess = type(guess)
    if typeOfGuess != int:
        print("that is an invalid guess")
      
    


name = input("what is your name?")
number = random.randint(1,100)
winner = False
attempts = 1
record = 0
while True:
    attempts = 1
    str(name)
    str(attempts)
    print("let's play a guess a number game ok " + name + "?")
    print("guess a number from 1 to, 100")
    for attempts in range(7):
        guess_ = input("guess a number ")
        guess = int(guess_)
        # valid(guess)
        if guess < number:
            print("guess greater ")
        if guess > number:
            print("guess less ")
        if guess == number:
            print("you got my number!!!")
            newRecord = attempts
            if record > newRecord:
                record = newRecord
                winner = True
                print(record)
                break

if winner == False:
    print("sorry you lost")
    
