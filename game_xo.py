# Game - game_xo.

print('''\n Game - XO \n''')
table = [['*', '*', '*'],
         ['*', '*', '*'],
         ['*', '*', '*']]
user_value = [0, 0]
for row in table:
    print(row)


def check_position_in_table(user_value):
    if table[user_value[0]][user_value[1]] == 'X' or table[user_value[0]][user_value[1]] == 'O':
        # print('This position have value! Please repeat.')
        return False
    else:
        # print('True')
        return True


def check_free_position(table):
    for row in table:
        for val in row:
            if val == str('*'):
                return True
            else:
                return False


def check_combination():
    # Check rows
    if (table[0][0] == 'X' and table[0][1] == 'X' and table[0][2] == 'X') \
            or (table[0][0] == 'O' and table[0][1] == 'O' and table[0][2] == 'O'):
        return True
    elif (table[1][0] == 'X' and table[1][1] == 'X' and table[1][2] == 'X') \
            or (table[1][0] == 'O' and table[1][1] == 'O' and table[1][2] == 'O'):
        return True
    elif (table[2][0] == 'X' and table[2][1] == 'X' and table[2][2] == 'X') \
            or (table[2][0] == 'O' and table[2][1] == 'O' and table[2][2] == 'O'):
        return True
    elif (table[1][0] == 'X' and table[1][1] == 'X' and table[1][2] == 'X') \
            or (table[1][0] == 'O' and table[1][1] == 'O' and table[1][2] == 'O'):
        return True
    # Check columns
    elif (table[0][0] == 'X' and table[1][0] == 'X' and table[2][0] == 'X') \
            or (table[0][0] == 'O' and table[1][0] == 'O' and table[2][0] == 'O'):
        return True
    elif (table[0][1] == 'X' and table[1][1] == 'X' and table[2][1] == 'X') \
            or (table[0][1] == 'O' and table[1][1] == 'O' and table[2][1] == 'O'):
        return True
    elif (table[0][2] == 'X' and table[1][2] == 'X' and table[2][2] == 'X') \
            or (table[0][2] == 'O' and table[1][2] == 'O' and table[2][2] == 'O'):
        return True
    # Check diagonals
    elif (table[0][0] == 'X' and table[1][1] == 'X' and table[2][2] == 'X') \
            or (table[0][0] == 'O' and table[1][1] == 'O' and table[2][2] == 'O'):
        return True
    elif (table[0][2] == 'X' and table[1][1] == 'X' and table[2][0] == 'X') \
            or (table[0][2] == 'O' and table[1][1] == 'O' and table[2][0] == 'O'):
        return True
    else:
        return False


answer = 0
while answer == 0:
    while True:
        if check_free_position(table):
            user_row = input('\nUser1: Enter row: ')
            if int(user_row) > 3 or int(user_row) <= 0:
                print('This row not exist. Please repeat.')
            else:
                user_value[0] = int(user_row) - 1
                break
            user_col = input('User1: Enter column: ')
            if int(user_col) > 3 or int(user_col) <= 0:
                print('This column not exist. Please repeat.')
            else:
                user_value[1] = int(user_col) - 1
                break
        else:
            answer = 3
        if check_position_in_table(user_value):
            # print(user_value)
            table[user_value[0]][user_value[1]] = 'X'
            print('\n')
            for row in table:
                print(row)
            if check_combination():
                answer = 1
        else:
            print('This position is busy. Enter other position.')
    while True:
        if check_free_position(table):
            user_row = input('\nUser2: Enter row: ')
            if int(user_row) > 3 or int(user_row) <= 0:
                print('This row not exist. Please repeat.')
            else:
                user_value[0] = int(user_row) - 1
                break
            user_col = input('User2: Enter column: ')
            if int(user_col) > 3 or int(user_col) <= 0:
                print('This column not exist. Please repeat.')
            else:
                user_value[1] = int(user_col) - 1
                break
        else:
            answer = 3
        if check_position_in_table(user_value):
            # print(user_value)
            table[user_value[0]][user_value[1]] = 'O'
            print('\n')
            for row in table:
                print(row)
            if check_combination():
                answer = 2
        else:
            print('This position is busy. Enter other position.')

if answer == 1:
    print('\nUser1(X) win!')
elif answer == 2:
    print('\nUser2(O) win!')
else:
    print('\nDraw!')