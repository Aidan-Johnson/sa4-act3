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
        print(f"Sorry! {guess} was not correct... PLEASE TRY AGAIN!!!1! IF YOU WISH TO EXIT TYPE q")
