# Assignment 6

# Program 2: Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

# generate number and print to answer
# if correct score++ 
# print score

import random

# declaration of variables
score = 0
n1 = 0
n2 = 0 
correctAnswer = 0
userAnswer = 0

for x in range(10):

    # assign random ints to n1 and n2
    n1 = random.randint(0,99)
    n2 = random.randint(0,99)

    # addition
    correctAnswer = n1 + n2

    # ask the user  
    userAnswer = int(input("Solve: " + str(n1) +" + "+ str(n2) + " = "))

    # check if the user's answer is correct
    if correctAnswer == userAnswer:
        score += 1
        print("correct sis " + str(score))

print("Result Summary: " + str(score) + "/10")