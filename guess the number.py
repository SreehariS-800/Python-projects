import random

print("ARE U READYY TO GUESS???? \nguess within 3 tries to win the challenge!")

#hmm please ignore this line cuz its a comment! i was just testing it to check something on github

from_number= input("Enter the top range: ")

if from_number.isdigit():
    from_number = int(from_number)
elif from_number <= 0:
    print("please type a number greater than 0")
    quit()
else:
    print("Please type a numerical number")
    quit()
        
        
    
random_number = random.randint(0,from_number)

guess=0

while True:
     guess +=1
     user_guess = input("Make guess:")
     if user_guess.isdigit():
         user_guess=int(user_guess)
     else:
         print("Please type in a number!")
         continue
     if user_guess == random_number:
         print("you got it correct! the number is ",random_number)
         break
     elif user_guess < random_number:
         print("Your guess was above the number")
     else:
         print("Your guess is below the number")
         
if guess <= 3:
    print("Hurray you won the challenge!")
else:
    print("You did it, but failed challenge!")
        

