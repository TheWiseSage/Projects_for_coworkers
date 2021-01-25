#!/usr/bin/env python3

import random
import os
from time import sleep
#Creates a function so I can be a lazy boi
clear = lambda: os.system('clear')

#Creates the plethora of silly timers for this absurd code to work
timer = 5
timer2 = 5
timer3 = 5

#Generates the first instance of the random num, 3 digits
number = random.randint(0,9)

#creates the var for the while loop to allow play choices
x = 'y'

#initializes the score variable
score = 0

#initializes the top and bottom ranges for the random number
bran = 0
tran = 9

#Creates the loop that the game lives within.
while x == 'y':
	
#from here to 45 is just to make a countdown timer.
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

#From here to 59 is just another countdown timer for the memory		
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

#Debug, uncomment for always win mode
	print('--debug--' + str(number))
	
	guess = input('What was it: ')

#Checks the guess against the first num
	if guess == str (number):
		print('\n')
		print('Good Job')
		
		#Adds one to score
		score = score + 1
		print('Your score is ' + str(score)+ ' points')
		print("Now we'll add five more seconds and one more number")
		
		#Adds five seconds to the timer, the double timers
		#allow for the addition without adding it to a negative 
		#num
		timer = timer + 5
		timer2 = timer2 +5
		
		#If anything other than y is typed, while loop breaks
		#and game ends
		x = input('Keep Going? type y: ')
		
		#A clever way to add another number to the previous 3 digit
		#number, it just converts the current number held in
		#bran and tran into a str then adds a str 0 or 9 
		#resectively. This is all the reconverted into an int

		bran = int(str(bran)+str(0))
		tran = int(str(tran)+str(9))

		#This line is here so that a new number is not generated 
		#until a correct guess has been inputted
		number = random.randint(bran,tran)
		
		#My clever boi lazy function
		clear()

#basic line of print commands that just loops back over the 
#while loop without regenerating new numbers
	else:
		print('\n')
		print("Almost, guess we'll try again")
		print('Your score is ' + str(score)+ ' points')
		x = input('Type y to Guess again: ')
		clear()



