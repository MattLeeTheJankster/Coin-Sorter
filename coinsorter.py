userNum = input("Enter an amount of money in cents. ")

userNum = int(userNum)


q = int(userNum/25)
userNum = userNum - (q * 25)

d = int(userNum/10)
userNum = userNum - (d * 10)

n = int(userNum/5)
userNum = userNum - (n * 5)

p = int(userNum/1)
userNum = userNum - (p * 1)

output = str(userNum) + " is {} quarters, {} dimes, {} nickels, and {} pennys.".format(q, d ,n ,p)
print(output)