# Password generator

import random
import string


while True:
    answer = input('\nNew password? ')
    if answer.upper() != 'Y':
        print('\nOk, goodbye!')
        break
    for value in range(3):
        animal = ['pig', 'kat', 'dog']
        animal = random.choice(animal)
        first_name = ['Max', 'Ivan', 'Alex']
        first_name = random.choice(first_name)
        last_name = ['Ivanov', 'Sidorov', 'Petrov']
        last_name = random.choice(last_name)
        numbers = random.randint(1, 100)
        special = random.choice(string.punctuation)
        special_two = random.choice(string.punctuation)
        passwd = animal + special_two + first_name + last_name + str(numbers) + special
        print('Passwords: ', passwd)