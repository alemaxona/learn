# Game - 'EnigmaInt'

from random import randint


def enigma_numbers():
    print('\nNew Game!')
    enigma_number = randint(0, 20)
    flag = 0
    while flag != 1:
        user_value = int(input('Enter number: '))
        if user_value == enigma_number:
            print('Great! Your number -', user_value, 'Enigma number -', enigma_number)
            flag = 1
        elif user_value > enigma_number:
            print('Your number > Enigma number! Please enter number again!')
        elif user_value < enigma_number:
                print('Your number < Enigma number!  Please enter number again!')


while True:
    answer = input('\nEnter game EnigmaInt? Y/N ')
    if answer == 'y' or answer == 'Y':
        enigma_numbers()
    else:
        print('Ok, Goodbye!')
        break