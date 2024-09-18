import random

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

options_list=[0,1,2]
computer_choice= random.choice(options_list)
user_choice=int(input("What do you choose ? type 0 for rock, 1 for scissor or 2 for paper:\n"))
if user_choice==0:
    print(rock)
elif user_choice==1:
    print(scissors)
elif user_choice==2:
    print(paper)
else:
    print("You have not chosen a correct answer. Good Bye")
    exit()
if computer_choice==0:
    print("computer chose:\n")
    print(rock)
elif computer_choice==1:
    print("computer chose:\n")
    print(scissors)
elif computer_choice==2:
    print("computer chose:\n")
    print(paper)
if (user_choice==0 and computer_choice==2) or (user_choice==2 and computer_choice==1) or (user_choice==1 and computer_choice==0):
    print("You lose")
elif user_choice==computer_choice:
    print("Its a Draw !!")
else:
    print("you win !!")

