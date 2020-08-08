password = 'a123456'
x = 3
while True:
	pw = input('Enter password: ')
	if pw == password:
		print('correct password')
		break
	else:
		x = x - 1
		print('you still can try' , x ,'times')
		if x == 0:
			print('sorry, you cannot try anymore')
			break
	