#STORY PROGRAM

# This program should take user input() and based on the choice
#the user made change the course of the story.

# For example:
# this is my story 



print("You're in a boat all alone in the middle of the ocean with only 500 mL of drinking water left. What do you do?")
print("(1) you drink all the water (2) you drink some (3) you do nothing")
choice = input("choose: ")

if choice == "1":
   print("your chances of surviving this are quite low")

   choice_2 = input('Would you like to rethink your decision? Please type yes/no:')

   if  choice_2 == "yes":
          print('you can live a bit longer if you do not drink all the water in one go')
   
   elif  choice_2 == "no":
      print('You will probably die soon, so: Carpe Diem!')





elif choice == "2":
    print("Good choice, but you should drink very little, try to save some water if you wanna survive")


    mL = (int(input('How much do you want to drink? please enter mL ')))
    if 0 <= mL <=50: 
       print('You might live, roughly up to 24 hours or more')

    elif  50 < mL <= 150:
       print('Be careful, you will probably run out of water in less than 24 hours')
       
    elif 150 < mL <= 250:
       print('You might live perhaps more than 15 hours')

    elif 250 < mL <= 300:  
       print('This is not good, man, it is going down too fast', "you've got 10 hours left maybe less?")

    elif mL > 300: 
       print('Really, do you wanna die here?:')
       
   
if choice == "3" :
   print("Only God knows what will happen to you")

else: print("You're rescued by the Coast Guard: Life is good!")
   
