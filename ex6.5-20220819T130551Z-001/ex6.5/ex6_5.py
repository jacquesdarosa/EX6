#STORY PROGRAM

# This program should take user input() and based on the choice
#the user made change the course of the story.

# For example:

print("You're in a boat all alone in the middle of the ocean with only 500 ml of drinking water left. What do you do?")
print("(1) drink all the water (2) drink some (3) none")
choice = input("choose: ")

if choice == "1":
   print("you're going to die soon")
elif choice == "2":
   print("you will live a bit longer")
   #continue tree here
elif choice == "3": 
   print("only God knows")
else:
   print("u just die for inaction")

