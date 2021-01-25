# Projects_for_coworkers
This is a place to dump the raw files of code that I have made for a coworker of mine

This is a simple command line game.
The concept originated from teaching one of my coworkers how to code basic python.
Now, I am no expert myself, but I was able to get the game working in a way that would still be simple emough for a new programmer to understand.


The game is simple. It generates a random one digit number, tells it to you with three seconds to remember it, then makes you remember for 5 seconds. 
On each correct input the game will ask if you would like to play again. If you say yes then a new number will be generated that is one digit longer for each repetition,
additionally, five seconds will be added to the memory timer on each correct guess. On an incorrect guess the game will loop back repeating the previous number and time
values. This game does keep score, however, it could also be viewed as a level counter. Each correct rememberization is also a point/level and each increase in points/levels
equals a one digit increase and a time increase. 

Additionally, there is debug output in the form of a print on line 64 that can be uncommented to print the correct number before the input command on each iteration. 
