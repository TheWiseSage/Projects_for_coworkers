#!/usr/bin/env python3

import random
import os
from time import sleep

clear = lambda: os.system('clear')
timer = 10
timer2 = 10
timer3 = 10
'''
firstnum = random.randint(0,9)
secondnum = random.randint(0,9)
thirdnum = random.randint(0,9)
fourthnum = random.randint(0,9)
'''

number = random.randint(000,999)
x = 'y'
score = 0
bran = 000
tran = 999
while x == 'y':
	#num = int(str(firstnum)+str(secondnum)+str(thirdnum)+str(fourthnum))
	
	initialcounter = 3
	for x in range (3):
		if initialcounter == 1:
			clear()
			print('Your score is ' + str(score)+ ' points')
			print('You Only Have ' + str(initialcounter) + ' second to remember this number: ')
			print(number)
			sleep(1)
		else:
			clear()
			print('Your score is ' + str(score)+ ' points')
			print('You Only Have ' + str(initialcounter) + ' seconds to remember this number: ')
			print(number)
			sleep(1)
		initialcounter = initialcounter -1
		

	
	#print(str(firstnum)+str(secondnum)+str(thirdnum)+str(fourthnum))
	#sleep(3)
	timer3 = timer
	for x in range(timer2):
		if timer3 == 1:
			clear()
			print('Remember for ' + str(timer3) + ' more second')
			timer3 = timer3 -1
			sleep(1.0)
		else:
			clear()
			print('Remember for ' + str(timer3) + ' more seconds')
			timer3 = timer3 -1
			sleep(1.0)
	clear()
	print('OK, Time to guess')
	print('--debug--' + str(number))
	guess = input('What was it: ')

	if guess == str (number):
		print('\n')
		print('Good Job')
		score = score + 1
		print('Your score is ' + str(score)+ ' points')
		print("Now we'll add five more seconds and one more number")
		timer = timer + 5
		timer2 = timer2 +5
		'''
		firstnum = random.randint(0,9)
		secondnum = random.randint(0,9)
		thirdnum = random.randint(0,9)
		fourthnum = random.randint(0,9)
		'''
		x = input('Keep Going? type y: ')
		bran = int(str(bran)+str(0))
		tran = int(str(tran)+str(9))
		number = random.randint(bran,tran)
		
		clear()

	else:
		print('\n')
		print("Almost, guess we'll try again")
		print('Your score is ' + str(score)+ ' points')
		x = input('Type y to Guess again: ')
		clear()



