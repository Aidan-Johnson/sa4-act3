number = 10
cap = 3
choice  = input("if you want unlimited guesses type U if not type L")
if choice == 'L':
        
    print("I'm thinking of a number...")
    while True:
        if cap == 0:
            print(f'The number was {number}!')
            break

        guess = (input("What number am I thinking of? "))

        if guess == number:
            print("Congratulations! You guessed the right number.")
            break
        
        elif guess == 'q':
            print(f'The number was {number}!')
            break
        
        else:
            if int(guess) > number:
                cap -= 1
                print(f"Sorry! {guess} is higher than my number... you have a remaining {cap} guesses left... IF YOU WISH TO EXIT TYPE q")
            else:
                cap -= 1
                print(f"Sorry! {guess} is lower than my number... you have a remaining {cap} guesses left... IF YOU WISH TO EXIT TYPE q")

if choice == 'U':
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
                print(f"Sorry! {guess} is higher than my number... you have a remaining {cap} guesses left... IF YOU WISH TO EXIT TYPE q")
            else:
                print(f"Sorry! {guess} is lower than my number... you have a remaining {cap} guesses left... IF YOU WISH TO EXIT TYPE q")
