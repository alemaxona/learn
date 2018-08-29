# Game - 'enigma_int'


from random import randint


def enigma_int():
    print('\nNew Game - enigma_int!')
    enigma_number = randint(0, 20)
    flag = 0
    while flag != 1:
        user_value = int(input('Enter number: '))
        if user_value == enigma_number:
            print('Great! Your number -', user_value, 'Enigma number -', enigma_number,'.')
            flag = 1
        elif user_value > enigma_number:
            print('Your number > Enigma number! Please enter number again!')
        elif user_value < enigma_number:
                print('Your number < Enigma number!  Please enter number again!')


while True:
    answer = input('\nStart new game? Y/N ')
    if answer == 'y' or answer == 'Y':
        enigma_int()
    else:
        print('Ok, Goodbye!')
        break