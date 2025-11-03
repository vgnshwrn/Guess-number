# 🎮 Secret Number Guessing Game
# The player has 5 attempts to guess the secret number

secret = 42
attempts = 5

while attempts > 0:
    guess = int(input("Guess the number (1-100): "))
    
    if guess == secret:
        print("🔥 Correct! You've guessed the number.")
        break
    elif guess > secret:
        print("📉 Too high!")
    else:
        print("📈 Too low!")
    
    attempts -= 1
    print(f"Attempts left: {attempts}")

if attempts == 0:
    print("💀 Game over! The secret number was", secret)
