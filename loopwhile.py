import random
secret_number = random.randint(1,10)
guess = 0
attempts = 0
print("I am thinking of a number between 1 to 10!")
while guess !=  secret_number:
    guess = int(input("Take a guess: "))
    attempts += 1
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too High! Try again.")
    else:
         print(f"You got it! It took you {attempts} tries to find the secret nubmer{secret_number}!") 