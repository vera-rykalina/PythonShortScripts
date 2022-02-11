#### Password Generator (randomized order) ####
'''
This code outputs a password based on the prompted number of letter, numbers, and symbols in a random order. 
'''
# Load random library
import random

# Define characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Define user input
print("Welcome to the Password Generator!\n")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

# Generator for letters, numbers, and symbols
total_char_number = nr_letters + nr_numbers + nr_symbols
total_char_list = letters + numbers + symbols

password = ""
for number in range(1, total_char_number + 1):
  char=random.randint(0, len(total_char_list)-1)
  password += total_char_list[char]
print("A password has been generated for you: " + password)
