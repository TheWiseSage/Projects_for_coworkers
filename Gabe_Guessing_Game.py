#!/usr/bin/env python3

#Imported modules

import random
from time import sleep

#variables

rnum=random.randrange(1,9999)
rnum1=random.randrange(1,9999)
L=("Loading")
dot=(".")
score=0
yes=["Y","y"]
no=["N","n"]
#score=("1")

#Title

print(''




                                                            'This is the random number memory game!''')
print(" You must remember the number printed, then enter the number again to score points. You only get 3 strikes then game over.")
sleep(5)

#Prompt to ask if user wants to play game

response=input("Would you like to play? Enter Y for yes and N for no.")
if (response in yes):
    print("Game Starting")
    sleep(2)
else:
    response in no
    print("Exiting Game.......")
    sleep(3)
    quit()
    
#Loading screen    

for x in range(0,5):
    print(L)
    L= ((L)+(dot))
    dot=((dot)+("."))
    sleep(1)

#random number generator on loop

while True:     

    print("You must try to remember the random number then retype it!")
    print(rnum)
    sleep(5)

#Clears random number from screen.

    for y in range(0,150):
        print("Remember this number!")
  
        
        sleep(.009)
        
    #Cheater catch

    print(''




                                                        'This is the random number memory game!''')
    print(" You must remember the number printed, then enter the number again to score points. You only get 3 strikes then game over.")
    print("You must try to remember the random number then retype it!")
    print("Would you like to play? Enter Y for yes and N for no.")
    print("Game starting")
    print("loading")
    print("loading.")
    print("loading..")
    print("loading...")
    print("loading....")
    print("loading.....")
    print("loading........")
    print("You must try to remember the random number then retype it!")
    print("Remember this number!")
    print(rnum1)

    for z in range( 0,150):
        print("Remember this number!")
    sleep(0.009)
#User guesses random numbers loop

    while True:         
        sleep(5)
        random1=input("What was the random number?") 
#---------------------------------------------------        
        #random2=(rnum)
        if random1==str(rnum):
#---------------------------------------------------        	
   # ((score)+ int (1) +("points"))
            score=score+1
            print (str(score)+("Points"))
            rnum=rnum+rnum1#
            break
        elif random1==str(rnum1):
            print ("You are a cheater!! Lol. Self destructing in 3 seconds!")
            quit()
#Strikes implemented to enable a Game Over

        else:
            for x in range(0,3):
                print("Strike! Game Over at 3 strikes.")
                counter=0
                counter=counter+1
                if counter==3:
                    print(("Game Over. Final score is ")+score)
                    sleep(7)
                    quit()