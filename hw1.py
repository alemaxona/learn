# Home work++ for video1
score = 0
answer_attempts = 0
print("""\n
		It\'s 5 questions!\n 
		You have 20 attempts for all question.\n
		One right answer = +1 Score.\n
		One false answer = -1 Score.\n
		4+ Score - You win!\n
		1-2 Scores - You Lost!\n
		3 Scores - It\'s a draw\n
		Good Luck! """)
while answer_attempts < 20:
	answer = input('3 > 2? y/n:')
	answer_attempts = answer_attempts + 1
	if answer != 'y' and answer != 'n' and answer != 'Y' and answer != 'N': 
		print('Please enter Y/y or N/n')
	else: 
		if answer == 'y' or answer == 'Y':
			score = score + 1
			print('Answer accepted!')
			break
		else:
			if answer == 'n' or answer =='N':
				if score == 0:
					score = 0
					break
				else:
					score = score - 1
					print('Answer accepted!')
					break
while answer_attempts < 20:
	answer = input('What is my name? Maxim or Alex? y/n:')
	answer_attempts = answer_attempts + 1
	if answer == 'maxim' or answer == 'MAXIM' or answer =='Maxim':
		score = score + 1
		print('Answer accepted!')
		break
	else:
		if answer == 'alex' or answer =='ALEX' or answer == 'Alex':
			if score == 0:
				score = 0
				break
			else:
				score = score - 1
				print('Answer accepted!')
				break
		else:
            if score == 0:
                score = 0
            else:
                score = score - 1
                print ('My name not ' + str(answer))
            break
while answer_attempts < 20:
    answer = input('What my love Phone? y/n:')
    answer_attempts = answer_attempts + 1
    if answer == 'Iphone' or answer == 'iPhone' or answer =='IPHONE':zscore = score + 1
		print('Answer accepted!')
		break
	else:
		if score == 0: 
			score = 0
		else:	
			score = score - 1
			print ('My Love Phone not ' + str(answer))
			break
while answer_attempts < 20:
	answer = input('8 * 8 =')
	answer_attempts = answer_attempts + 1
	if answer == str('64'):
		score = score + 1
		print('Answer accepted!')
		break
	else:
		if score == 0: 
			score = 0
		else:	
			score = score - 1
			print ('8 * 8 != ' + str(answer) + '!')
			break
while answer_attempts < 20:
	answer = input('The biggest animal?  ')
	answer_attempts = answer_attempts + 1
	if answer == 'Elephant':
		score = score + 1
		print('Answer accepted!')
		break
	else:
		if score == 0: 
			score = 0
		else:	
			score = score - 1
			print (str(answer) + 'is not the biggest animal' + '!')
			break


if score > 4:
	print('You win!' + 'Your score: ' + str(score) +'!' + ' Answer attempts: ' + str(answer_attempts) + '!')
else:
	if score < 2:
		print('You lost!' + 'Your score: ' + str(score) +'!' + ' Answer attempts: ' + str(answer_attempts) + '!')
	else:
		print('It\'s a draw' + 'Your score: ' + str(score) +'!' + ' Answer attempts: ' + str(answer_attempts) + '!')


#Numbers are multiple of 5
list_multiple = []
number = 1
user_number = input('Please enter number other than 0: ')
while number <= int(user_number):
	if number % 5 == 0:
		print('Number - ' + str(number) + ' is a multiple of 5')
		list_multiple.append(number)
		number = number  + 1
	else:
		print('Number -  ' + str(number) + ' is not a multiple of 5!')
		number = number  + 1
print ('Numbers are multiple of 5: ' + str(list_multiple))