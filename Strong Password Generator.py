print("Welcome To Password Generator")
import random
letter=("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
number=("1234567890")
symbol=("!@#$%^&*()")
nr_letter=int(input("Type How many letter do you want?\n"))
nr_number=int(input("Type How many number do you want?\n"))
nr_symbol=int(input("Type How many symbol do you want?\n"))
Password_list=[]
for char in range(1,nr_letter+1):
    random_char=random.choice(letter)
    Password_list+=random_char
for char in range(1,nr_number+1):
    random_char=random.choice(number)
    Password_list+=random_char
for char in range(1,nr_symbol+1):
    random_char=random.choice(symbol)
    Password_list+=random_char
print(Password_list)

random.shuffle(Password_list)
Password=""
for char in Password_list:
    Password+=char
print(f"Your password is {Password}")


