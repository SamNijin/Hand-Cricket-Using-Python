"""
This python script is made to determine
whether the total sum of the user number
and the system number is odd or even.
"""

# importing random function for picking up random values
import random as rd

'''
Getting input from user for both odd or even and the values from 0 to 10
Making compiler to generate random data according to the values
user_choice -> to store odd or even value from user it can be the first letter of odd and even like O or E
                or it can be like odd or even then converting it to lower case to simply the the ambiguity
                also overriding the use_choice variable with the first letter from the input                
user_number -> to store the values from 0 to 10 from the user
sys_number -> to store random generated numbers from 0 to 10
'''

user_choice = input('Enter "O" Odd and "E" for Even -> ').lower()
user_choice = user_choice[:1]
print(user_choice)
user_number = int(input('Enter values from 0 to 10 -> '))
sys_number = rd.choice(range(11))

# Adding the user value and the system value and storing in total variable
total = user_number + sys_number

'''
find whether the input is odd or even

requires the total variable as argument
returns True if the value is even
return False if the value is odd
'''


def is_even(value):
    if value % 2 == 0:
        return True
    else:
        return False


'''
Find the result

requires total variable as argument
calling theis_even function 
if the value is even if so,
    check for the user input and if it is e
        display user won the toss
    if not
        display system won the toss
else
    check for the user input and if it is o
        display user won te toss
    if no
        display system won the toss
'''


def result(value):
    if is_even(value=total):
        print('*** The Result is even ***')
        if user_choice == 'e':
            print('Total is {}\nComputer Choice is {}'.format(value, sys_number))
            print('user won the toss')
        elif user_choice == 'o':
            print('Total is {}\nComputer Choice is {}'.format(value, sys_number))
            print('system won the toss')
    else:
        print('*** The Result is even ***')
        if user_choice == 'o':
            print('Total is {}\nComputer Choice is {}'.format(value, sys_number))
            print('user won the toss')
        elif user_choice == 'e':
            print('Total is {}\nComputer Choice is {}'.format(value, sys_number))
            print('system won the toss')


# invoking the result function
result(value=total)
