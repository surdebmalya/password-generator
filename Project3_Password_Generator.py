'''Password Generator:
    Write a programme, which generates a random password for the user.
    Ask the user how long they want their password to be, and how many 
    letters and numbers they want in their password. Have a mix of upper 
    and lowercase letters, as well as numbers and symbols. The password 
    should be a minimum of 6 characters long.'''

import random

print("\t :::  Welcome To Password Generator  :::")
print("\t      =============================\n")
print(" Rule: The password should be a minimum of 6 characters long.")
print(" ====\n\n")

n=int(input(" Enter the length of password: "))

while(n<6):
    print("\n PASSWORD LENGTH SHOULD BE GREATER OR EQUAL TO 6 !!!")
    print(" ===================================================\n")
    print(" Please input password length again")
    n=int(input("\n Enter the length of password: "))
print("\n")

no_letters=int(input(" Enter NUMBERs of LETTERS you want in your password: "))
no_numbers=int(input("\n Enter NUMBERs of NUMBERS you want in your password: "))
while(no_letters+no_numbers>n):
    print("\n WARNING: TOTAL NUMBER OF CHARACTER EXCEED THE LENGTH OF PASSWORD!!!")
    print(" =======\n")
    print(" Please try again\n\n")
    no_letters=int(input(" Enter NUMBERs of LETTERS you want in your password: "))
    no_numbers=int(input("\n Enter NUMBERs of NUMBERS you want in your password: "))
print("\n")
no_symbols=n-no_letters-no_numbers

virtual_l_of_letters=list(range(65,91))+list(range(97,123))
l_of_letters=[]
for i in range(len(virtual_l_of_letters)):
    l_of_letters=l_of_letters+[chr(virtual_l_of_letters[i])]

virtual_l_of_numbers=list(range(48,58))
l_of_numbers=[]
for i in range(len(virtual_l_of_numbers)):
    l_of_numbers=l_of_numbers+[chr(virtual_l_of_numbers[i])]

virtual_l_of_symbols=list(range(33,48))+list(range(58,65))+list(range(91,97))+list(range(123,127))
l_of_symbols=[]
for i in range(len(virtual_l_of_symbols)):
    l_of_symbols=l_of_symbols+[chr(virtual_l_of_symbols[i])]
    
set_of_letters=[]
for i in range(no_letters):
    set_of_letters=set_of_letters+[random.choice(l_of_letters)] 
    
set_of_numbers=[]
for i in range(no_numbers):
    set_of_numbers=set_of_numbers+[random.choice(l_of_numbers)]
    
set_of_symbols=[]
for i in range(no_symbols):
    set_of_symbols=set_of_symbols+[random.choice(l_of_symbols)]
    
final_set=set_of_letters+set_of_numbers+set_of_symbols
random.shuffle(final_set)

final_string=""
for i in range(n):
    final_string=final_string+final_set[i]

print(" Your Password Is Ready!!!\n")
print(" Password: "+final_string)
print(" ========\n")
print("\n\t ::: Thanks For Using :::\n\n")