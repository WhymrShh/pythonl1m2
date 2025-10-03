import random

characters = "+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

number = int(input("Parolanın uzunluğunu giriniz: "))

password = ""

for i in range(number):
    character = random.choice(characters)
    password += character

print("Parola:", password)

