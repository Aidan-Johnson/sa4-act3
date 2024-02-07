number = 10

print("I'm thinking of a number...")
while True:
    guess = (input("What number am I thinking of? "))

    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess == 'q':
        print(f'The number was {number}!')
        break
    else:
        if int(guess) > number:
            print(f"Sorry! {guess} is higher than my number... PLEASE TRY AGAIN!!!1! IF YOU WISH TO EXIT TYPE q")
        else:
            print(f"Sorry! {guess} is lower than my number... PLEASE TRY AGAIN!!!1! IF YOU WISH TO EXIT TYPE q")
