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
   choice = input('Would you like to think again? Please type yes/no:')
   if choice == "yes" :
    print('you can live a bit longer if you do not drink all the water in one go')
   elif choice == "no":
    print('You will probably die soon, so Carpe Diem')

elif choice == "2":
   print("good choice, but you should drink very little, try to save some water if you wanna survive")
   #continue tree here
elif choice == "3": 
   print("only God knows what will happen to you")
else:
   print("you're rescued by the Coast Guard, life is good")

