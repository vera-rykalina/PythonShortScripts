
#### Password Generator (Sequencial order) ####

'''
This python code outputs a password based on the prompted number of letters, numbers, and symbols sequencially. 
'''
# Load random library
import random

# Define characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# User input
print("Welcome to the PyPassword Generator!\n")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

# Set empty strings
string_1 = ""
string_2 = ""
string_3 = ""

# Generator for letters, numbers, and symbols
for number in range(1, nr_letters+1):
  letter=random.randint(0, len(letters)-1)
  string_1 += letters[letter]

for number in range(1, nr_numbers+1):
  digit=random.randint(0, len(numbers)-1)
  string_2 += numbers[digit]

for number in range(1, nr_numbers+1):
  symbol=random.randint(0, len(symbols)-1)
  string_3 += symbols[symbol]

print("Your password: " + string_1 + string_2 + string_3)

