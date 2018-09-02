# Game - EnigmaStr.


import random


def enigmastr(answer, user_value, chose):
    index = 0
    while index < len(chose):
        if user_value == chose[index]:
            answer[index] = user_value
        index += 1


while True:
    user_answer = input('\n\nStart new game? Y/N ')
    if user_answer.upper() == 'Y':
        enigma_string = ['green', 'book', 'Hockey', 'Sun', 'Python', 'World', 'Administrator']
        chose = random.choice(enigma_string)
        length_word = len(chose)
        answer = [i for i in range(0, length_word)]
        for i in answer:
            answer[i] = '?'
        health = 10
        flag = 0
        health_symbol = u'\u2764'
        print('\nComputer chose a word for', length_word, 'letters.\n\n', answer, '\n\nYour health:', health_symbol * health)
        while health > 0:
            user_value = input('\nEnter word or 1 letter: ')
            if len(user_value) == len(chose):
                if user_value == chose:
                    print('\nGreat, You guessed! It\'s -', chose,'!', 'Your health:', health_symbol * health)
                    flag = 1
                    break
                else:
                    health -= 1
                    print('This word is not right! Please repeat. Your health:', health_symbol * health)
            elif user_value in chose:
                enigmastr(answer, user_value, chose)
                print(answer)
                if '?' not in answer:
                    flag = 1
                    break
            else:
                if len(user_value) > len(chose):
                    health -= 1
                    print('Length word < length secret word! Please repeat. Your health:', health_symbol * health)
                else:
                    health -= 1
                    print('This letter is not in secret word. Your health:', health_symbol * health)
        if flag == 1:
            print('\nGreat, You win! It\'s -', chose,'!', 'Your health:', health_symbol * health)
        else:
            print('You lose! Your health -', health, health_symbol)
    else:
        print('\nOk, goodbye!')
        break