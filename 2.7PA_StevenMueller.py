# Name: Steven Mueller
# Date: October 14, 2026
# Description: Ask the user to guess a predetermined number,
# count their attempts, and demonstrate while and for loops.

userName = input("What is your name? ")
studentId = input("What is your Student ID? ")

print(f"\nHello, {userName}! Student ID: {studentId}")

correctNumber = 5
guessCount = 0
userGuess = 0

# Keep asking until the user guesses the correct number.
while userGuess != correctNumber:
    userGuess = int(input("Please guess a number between 1 and 10: "))
    guessCount += 1

    if userGuess > correctNumber:
        print("You guessed too high.")
    elif userGuess < correctNumber:
        print("You guessed too low.")
    else:
        print(
            f"Congratulations, {userName}! "
            f"You guessed the number in {guessCount} tries!"
        )

# Display five increments of the correct guess using a while loop.
print("\nOutput from the 'while' loop:")

incrementAmount = 1

while incrementAmount <= 5:
    incrementedNumber = userGuess + incrementAmount
    print(
        f"{userGuess} incremented by {incrementAmount} "
        f"is {incrementedNumber}"
    )
    incrementAmount += 1

# Display the same five increments using a for loop.
print("\nOutput from the 'for' loop:")

for incrementAmount in range(1, 6):
    incrementedNumber = userGuess + incrementAmount
    print(
        f"{userGuess} incremented by {incrementAmount} "
        f"is {incrementedNumber}"
    )
