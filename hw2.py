#Home work++ for video2
answer_score = 0
score = 0
attempts = 3
print("""\n
		It\'s 3 questions!\n 
		You have 3 wrong attempts for all question.\n
		One right answer = +1 Score.\n
		Good Luck! """)
question_answer = {'1 + 2 = ? ': '3', 'What language we learn? ':'Python', '5 > 4 ?(Y/N)': 'Y'}
for key, value in question_answer.items():
	answer_score = answer_score + 1
	while attempts != 0:
		answer = input(str(key))
		if answer.upper() == value.upper():
			print('You right, it is: ' + str(value))
			score = score + 1
			break
		else:
			if attempts > 0:
				attempts = attempts - 1
				print('Answer is wrong... Please answer again, you have - ' + str(attempts) + ' attempts!')
print(' All answer = ' + str(answer_score) + '\n' + ' Your attempts = ' + (str(3 - attempts)) + '\n' +  ' Your right answer = ' + str(score) + '\n' + 
	' Your wrong answer = ' + str(answer_score - attempts))

#Sorting list
y_list = [1, 2, 5, 3, 8, 10]
y_list.sort()
for l in my_list:
	print(l)

#Input key and value
my_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'for', 5: 'five'}
for k in my_dict:
	print(k, my_dict[k])

#max and min
user_tuple = (1.234, 4.5, 6.34, 1.333, 9.999, 123.2, 0.555, 1000.1)
print(str(max(user_tuple)))
print(str(min(user_tuple)))

#Concat
user_list = ['Earth', 'Russia', 'Moscow']
concat = user_list[0] + '->' + user_list[1] + '->' + user_list[2]
print(concat)

#?
user_string = '/bin:/usr/bin:/usr/local/bin'

#Numbers are multiple of 7
numbers = []
i = 0
while i < 100:
	if i % 7 == 0 and i != 0:
		numbers.append(i)
		i = i + 1
	else:
		i = i + 1
print ('Number multiply of 7: ' + str(numbers))

#Matrix. Print all rows and print all columns
matrix = [	[1,2,3],
			[7,38,39],
			[4,27,18]]

#rows
for row in matrix:
	for elem in row:
		print(elem, a ='|')
	print()

 #columns
