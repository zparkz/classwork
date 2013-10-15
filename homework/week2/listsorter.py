## Homework Week 2: List sorting
## spark carranza
'''
#In the provided file listsorter.py, write a program that prompts a
user for 5 numbers. Store those numbers in a list. Print out a list
containing those numbers from smallest to largest.  When you run the
program, you should get output like the following:

    Enter a number: 3
    Enter a number: 2
    Enter a number: 1
    Enter a number: 10000
    Enter a number: -5

    [-5, 1, 2, 3, 10000]

You may want to refer to [this section of the Python
docs](http://docs.python.org/tutorial/datastructures.html#more-on-lists) for
handy functions that you can call on lists.

You can assume that the user of this program will always enter a
number. Don't worry about handling non-number input.
'''

#enterNums = raw_input("Enter a series of numbers here: ")
numList = []
# create the list
for i in range(5):
    numList.append(raw_input("Enter a number here: "))

numList.sort()

print "Sorted list here: ", numList

