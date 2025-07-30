
import random
print("Welcome to the Password Generator")
while True:
    a=input("Enter the password Length:")
    if a.isdigit():
        length=int(a)
        if length >0:
            break
        else:
            print("please enter a number greater than 0")
    else:
        print("invalid input")
letters='abcdefghijklmnopqrstuvwxyz'
numbers='0123456789'
symbols='!@#$%^&*()+_-='
all_characters = letters+numbers+symbols
password= ' '
for i in range(length):
    password += random.choice(all_characters)
print("Generated password",password)
