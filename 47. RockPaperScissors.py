rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
choice=int(choice)

if choice == 0:
  print(rock)
elif choice ==1:
  print(paper)
elif choice ==2:
  print(scissors)
else:
  print("You have typed different number..")
import random
computer_choice=random.randint(0,2)
if computer_choice == 0:
  print(rock)
elif computer_choice ==1:
  print(paper)
elif computer_choice ==2:
  print(scissors)

if computer_choice==0:
  if choice==2:
    print("Computer wins")
  elif choice==1:
    print("You win!..")
elif computer_choice==1:
  if choice==0:
    print("Computer wins")
  elif choice==2:
    print("You win!..")
elif computer_choice==2:
  if choice==0:
    print("You win!..")
  elif choice==1:
    print("Computer wins.")
else:
  print("It is a draw :/")