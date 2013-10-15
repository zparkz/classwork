# Homework Week2:
# Practice with finding information
# spark carranza

"""Use the internet to figure out how to get python to give you a random
integer between 0 and 100.  Write down what function you would use:

In guessmynumber.py, write a program which picks a single random
integer between 0 and 100 and repeatedly asks the user to guess it.

 - When the user is correct, print "You win!" and end the program
 - When the user is incorrect, tell them whether their guess was
   too high or too low, and then let them guess again until they get it.

Hint:

    import foo

is a python statement that makes module foo available from your
program.  For example, if there is a function in foo called flip(),
then you would be able to write foo.flip() in your program.
"""
import random

#while input != "no":
	 
computer = random.randint(0,101)
playguess = raw_input("Guess the number: " )

	#print "Computer selection is: "  + computer

if playguess == computer:
	print "You win!"
if playguess > computer:
	print "You were too high, guess again." , computer
if playguess < computer:
	print "You were too low, try again, as the computer is: ", computer  
 

	#input = raw_input("play again?! ")