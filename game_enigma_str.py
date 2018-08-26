# Game - 'EnigmaStr'

import random



def enigmastr():
    print('\nNew Game. You have 10 health!')
    print('The computer chose a word of 4 letters. Guess this word!')
    enigma_string = ['mari', 'kate', 'alex', 'mama']
    chose = random.choice(enigma_string)
    flag = 0
    while flag == 0:
        health = 10
        answer = ['_', '_', '_', '_']
        user_value = input('Enter word or letters: ')
        if user_value == chose:
            print('Great! Your version -', user_value, '.', 'The Computer chose - ', chose, '.', 'Your health -', health, '!', 'Best!')
            flag = 1
        else:
            if user_value[0] == chose[0]:
                answer[0] = user_value[0]
            if len(user_value) > 1 and user_value[1] == chose[1]:
                answer[1] = user_value[1]
            if len(user_value) > 2 and user_value[2] == chose[2]:
                answer[2] = user_value[2]
            if len(user_value) > 3 and user_value[3] == chose[3]:
                answer[3] = user_value[3]
            print(str(answer))

enigmastr()