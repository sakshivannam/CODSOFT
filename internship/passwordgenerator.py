import random
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&()_{}[]?\/.;'
length = int(input("Enter length:"))
password = ""

for a in range(length):
    password = password+random.choice(chars)
print("The Generated Password is",password)