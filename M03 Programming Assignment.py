# -*- coding: utf-8 -*-
"""
Armando Cedano
M03 Programming Assignment
This code is the answers to the 7.4 to 7.7 and 9.1, 9.2 of Things To Do questions.
"""

# 7.4
# Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".
things = ["mozzarella", "cinderella", "salmonella"]

# 7.5
# Capitalize the element in things that refers to a person and then print the list.
# Did it change the element in the list?
for i in range(len(things)):
    if 'ella' in things[i]:
        things[i] = things[i].capitalize()
print(things)
# Yes, it changed the element in the list.

# 7.6
# Make the cheesy element of things all uppercase and then print the list.
things[0] = things[0].upper()
print(things)

# 7.7
# Delete the disease element from things, collect your Nobel Prize, and print the list.
del things[2]
print(things)

# 9.1
# Define a function called good() that returns the following list: ['Harry', 'Ron', 'Hermione'].
def good():
    return ['Harry', 'Ron', 'Hermione']

print(good())

# 9.2
# Define a generator function called get_odds() that returns the odd numbers from range(10).
# Use a for loop to find and print the third value returned.
def get_odds():
    for number in range(1, 10, 2):
        yield number

count = 1
for odd in get_odds():
    if count == 3:
        print("Third odd number:", odd)
        break
    count += 1


