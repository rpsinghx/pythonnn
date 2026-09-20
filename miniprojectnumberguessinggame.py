import random 
while True:
    secret_number = random.randint(1,100)
    attempts_left = 7
    attempts_used = 0
    guessed_correctly = False
    while attempts_left>0:
        raw_input = input("Enter your guess:")
        try:
            guess = int(raw_input)
        except:
            print("number entered not valid")

        if guess<1 or guess>100:
            print("out of range please enter a number between 1 and 100")
            continue
        attempts_left-=1
        attempts_used+=1

        if guess == secret_number:
            print(f"congratulations! you guessed the number in {attempts_used} attempts")
            guessed_correctly = True
            break
        elif guess < secret_number:
            print("Go High")
        else:
            print("Go Low")
    
    if not guessed_correctly:
        print(f"\nGame Over! You ran out of attempts. The secret number was {secret_number}.")
    
    play_again = input("\nPlay again? (yes/no):").strip().lower()
    if play_again !="yes":
        print("Goodbye! Thank you for playing.")
        break