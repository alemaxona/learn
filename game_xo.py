# Game - game_xo.

print('''\n Game - XO''')


def check_position_in_table(user_value):
    if table[user_value[0]][user_value[1]] == 'X' or table[user_value[0]][user_value[1]] == 'O':
        # print('This position have value! Please repeat.')
        return False
    else:
        # print('True')
        return True


def check_user_value(value):
    if value == '0' or value == '1' or value == '2' or value == '3':
        if int(value) < 3 or int(value) > 0:
            if int(value) != 0:
                return True
            else:
                print('This value does not exist')
                return False
        else:
            print('This value does not exist')
            return False
    else:
        print('This value does not exist')
        return False

def check_free_position(table):
    i = '*'
    if i == table[0][0] or i == table[0][1] or i == table[0][2]\
        or i == table[1][0] or i == table[1][1] or i == table[1][2]\
        or i == table[2][0] or i == table[2][1] or i == table[2][2]:
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


while True:
    user_answer = input('\n\nStart new game? Y/N ')
    if user_answer.upper() == 'Y':
        print('\n')
        table = [['*', '*', '*'],
                 ['*', '*', '*'],
                 ['*', '*', '*']]
        user_value = [0, 0]
        for row in table:
            print(row)
        result = 0
        while result == 0:
            flag_user2 = 0
            flag_user1 = 0
            # User1
            while flag_user1 == 0:
                if check_free_position(table):
                    user_row = input('\nUser1: Enter row: ')
                    user_col = input('User1: Enter column: ')
                    if check_user_value(user_row) and check_user_value(user_col):
                        user_value[0] = int(user_row) - 1
                        user_value[1] = int(user_col) - 1
                        flag_user1 = 1
                        if check_position_in_table(user_value):
                            table[user_value[0]][user_value[1]] = 'X'
                            print('\n')
                            for row in table:
                                print(row)
                            if check_combination():
                                result = 1
                                flag_user2 = 1
                                break
                        else:
                            print('This position is busy. Enter other position.')
                            flag_user1 = 0
                    else:
                        flag_user1 = 0
                else:
                    result = 3
                    break
                # User2
            while flag_user2 == 0:
                if check_free_position(table):
                    user_row = input('\nUser2: Enter row: ')
                    user_col = input('User2: Enter column: ')
                    if check_user_value(user_row) and check_user_value(user_col):
                        user_value[0] = int(user_row) - 1
                        user_value[1] = int(user_col) - 1
                        flag_user2 = 1
                        if check_position_in_table(user_value):
                            table[user_value[0]][user_value[1]] = 'O'
                            print('\n')
                            for row in table:
                                print(row)
                            if check_combination():
                                result = 2
                                break
                        else:
                            print('This position is busy. Enter other position.')
                            flag_user2 = 0
                    else:
                        flag_user2 = 0
                else:
                    result = 3
                    break
        if result == 1:
            print('\nUser1(X) win!')
        elif result == 2:
            print('\nUser2(O) win!')
        else:
            print('\nDraw!')
    elif user_answer.upper() != 'N':
        print('Please enter "Y" or "N"!')
    else:
        print('Buy!')
        break