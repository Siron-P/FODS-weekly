#Write a program to create a number guessing game for the user. 
#The program should ask the user to input a number.

#importing random number
import random

#creating a function
def num_guess():
    n=random.randrange(1,25) #range for random number import

    attempts = 5 #maximum attempts=5

    print("-------------------------------------------")
    print("----WELCOME TO THE NUMBER GUESSING GAME----")
    print("-------------------------------------------")
    print("I have selected one number from 1 to 25.You have to guess than number in 5 attempts")
    #displaying about the game

    #for loop to let user only do 5 attempts
    for attempts in range(1,attempts+1):
        guess=int(input("Enter your guess: "))
        #input number from user

        while guess!=n: #while loop until the guess is wrong
            if guess<n: 
                print("Too Low")
                guess=int(input("Enter another guess: "))
            #if guess is lower than the random number

            elif guess>n:
                print("Too High")
                guess=int(input("Enter another guess: "))
            #if guess is higher than the random number
        
            else:
                break
        print("Correct number")
            #Breaking the while loop if the guess is correct

            #if the user have reached maximum attempts
        if attempts==attempts:
                print("Game Over!!")

#calling function to execute program
num_guess()                    