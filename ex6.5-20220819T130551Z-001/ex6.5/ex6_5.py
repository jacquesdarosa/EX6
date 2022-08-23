#STORY PROGRAM

# This program should take user input() and based on the choice
#the user made change the course of the story.

# For example:
# this is my story 

print("You're in a boat all alone in the middle of the ocean with only 500 ml of drinking water left. What do you do?")
print("(1) you drink all the water (2) you drink some (3) you do nothing")
choice = input("choose: ")

if choice == "1":

   print("your chances of surviving this are not high")

   choice_2 =input('Would you like to think again? Please type yes/no:')

   if  choice_2 == "yes":
          print('you can live a bit longer if you do not drink all the water in one go')
   
   elif  choice_2 == "no":
     print('You will probably die soon, so Carpe Diem')





elif choice == "2":
    print("good choice, but you should drink very little, try to save some water if you wanna survive")
    print(int(input('How much do you want to drink? Please enter number in ml:')))
   #continue tree here
    for ml in (1, 500):

      if 50 < ml < 100: 
       print('You might live roughly up to 24 hours')
      elif 100 < ml <=150:
       print('be careful, you will probably run out of water in less than 24 hours')
      elif 150 < ml <=250: 
       print(' you might live perhaps more than 15 hours')
      elif 250 < ml <= 300: 
       print('This is not good, man, this is going too fast', "you've got 10 hours maybe less?")
      elif 300 < ml: 
       print('Really, do you want to die here?:')
   
if choice == "3" :
   print("only God knows what will happen to you")

else: print("you're rescued by the Coast Guard, life is good")
   
