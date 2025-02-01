secret = "Dog".lower()

secret_length = len(secret)
underscore = "_ " * secret_length


guess_count = 0

print("Welcome to the word guessing game!")
print(f"Your hint is: {underscore}")
print()
while True: 
    guess = input("What is your guess? :").lower()
    guess_count += 1

    if len(guess) != secret_length:
        print(f"Your guess must be {secret_length} letters long. Try again.")
        continue
    
    if guess == secret:
        print("Congratulations! You guessed it!")

        if guess_count == 1:
            print(f"It took you {guess_count} guess.")
        else: 
            print(f"It took you {guess_count} guesses.")
        break
    
    hint = ""
    for i in range(secret_length):
        if guess[i] == secret[i]:
            hint += guess[i].upper()
        elif guess[i] in secret:
            hint += guess[i].lower()
        else:
            hint += "_"

    print(f"Your hint is: {hint}")

print("Game over.")
        
    
