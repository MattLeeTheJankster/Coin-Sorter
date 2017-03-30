userGuess = input("Enter an amount of money in cents. ")

userGuess = int(userGuess)


q = int(userGuess/25)
userGuess = userGuess -(q * 25)

d = int(userGuess/10)
userGuess = userGuess - (d * 10)

n = int(userGuess/5)
userGuess = userGuess - (n * 5)

p = int(userGuess/1)
userGuess = userGuess - (p * 1)

