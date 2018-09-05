# Game - 'enigma_str'. Double letters do not check.


import random


def enigma_str():
    print('''\nNew Game - enigma_str. You have 10 health!
The computer chose a word. Guess this word!''')
    enigma_string = ['green']#, 'book', 'Hockey', 'Sun', 'Python', 'World', 'Administrator']
    chose = random.choice(enigma_string)
    length_word = len(chose)
    print('\nComputer chose a word for', length_word, 'letters.')
    answer = [i for i in range(0, length_word)]
    for i in answer:
        answer[i] = '_'
    health = 10
    while health != 0:
        user_value = input('\nEnter word or letters: ')
        print(user_value)
        if user_value == chose:
            print('\nGreat, You guessed! It\'s -', chose,'!', 'Your health -', health,'.')
            break
        else:
            # count_letter = chose.count(user_value)
            for value in user_value:
                if value in chose:
                    # print('\nThis word have', count_letter, 'letters -', value, '!')
                    indx = chose.index(value)
                    answer[indx] = value
                    print(answer)
                    n = '_'
                    if n not in answer:
                        print('\nGreat, You guessed! It\'s -', chose, '!', 'Your health -', health,'.')
                        health = 0
                else:
                    health -= 1
                    print('This letter or word does not right. Your health -', health,'.')
                    if health == 0:
                        print('Game stop! You need a health...')


while True:
    user_answer = input('\n\nStart new game? Y/N ')
    if user_answer.upper() == 'Y':
        enigma_str()
    else:
        print('\nOk, goodbye!')
        break