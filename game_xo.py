# Game - game_xo.


table = {0: ['1', '*', '*'], 1: ['2', '*', '*'], 2: ['3', '_', '*']}
user_str_col_list = {'str': 0, 'col': 0}
for key, value in table.items():
    print(value)
for key, value in user_str_col_list.items():
    print(value)
flag = 0
while flag == 0:
    #user_xo = input('Enter X or O: ')
    #if user_xo.upper() != 'X' r 'O':
        print('Enter X or O again!')
    user_str = input('\nEnter number row: ')
    user_str = int(user_str)
    if user_str == 0 or user_str > 3:
        print('Row with number -', user_str, 'do not exist! Please repeat.')
    else:
        print('Ok, you selected row -', user_str)
    user_col = input('\nEnter number column: ')
    user_col = int(user_col)
    if user_col == 0 or user_col > 3:
        print('Column with number -', user_col, 'do not exist! Please repeat.')
    else:
        print('Ok, you selected column -', user_col)
        flag = 1
print('\nRow -', user_str, end=', ')
print('Column -', user_col)
user_str -= 1
user_col -= 1
user_str_col_list['str'] = user_str
user_str_col_list['col'] = user_col
print('\nUser selected dict:', user_str_col_list)

for key, value in table.items():
    list_table = []
    if key == user_str_col_list['str']:
        #print(key)
        list_table = value
        print(list_table)
        for i in list_table:
            print(i)
            indx = list_table.index(i)
            print('\n',indx)
            if indx == user_str_col_list['col']:
                print(indx)
                list_table[indx] = 'X'
                print(list_table)


