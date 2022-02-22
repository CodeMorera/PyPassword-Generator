#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 


random_letters = random.sample(letters, nr_letters)
print(random_letters)

nr_symbols = int(input(f"How many symbols would you like?\n"))
random_symbols = random.sample(symbols, nr_symbols)
print(random_symbols)


nr_numbers = int(input(f"How many numbers would you like?\n"))
random_numbers = random.sample(numbers, nr_numbers)
print(random_numbers)

pass_gen=[*random_letters,*random_symbols,*random_numbers]

char_acters=nr_numbers+nr_symbols+nr_letters
scrambled_pass=random.sample(pass_gen,char_acters)
new_pass="".join(scrambled_pass)
print(f"Your new password is {new_pass}")
