# Random Password generator
import random

# define the character you want to user
character ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*"

# take input from the user
len = int(input("Enter the length of the password:\n"))

# define pwd
pwd = ""

# use for loop to generate the password
for i in range(len):
    pwd += random.choice(character)
print(pwd)