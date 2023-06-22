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

#Write your code below this line 👇

out = [rock, paper, scissors]


while True:
    state = False
    num = random.randint(0, 2)
    while state == False:
        userIn = int(input("Please choose Rock (1), Paper (2) or Scissors (3): ")) - 1
        if userIn <= 2 or userIn > 0:
            state = True

    print(f"Computer played: \n{out[num]}")
    print(f"User played: \n{out[userIn]}")


    if num == userIn:
        print("It's a draw!")
    elif num == 0 and userIn == 1: 
        print("You won, Congrats!")
    elif num == 0 and userIn == 2: 
        print("Computer won!")
    elif num == 1 and userIn == 0: 
        print("Computer won!")
    elif num == 2 and userIn == 0: 
        print("You won, Congrats!")
    elif num == 2 and userIn == 1: 
        print("Computer won!")
    elif num == 1 and userIn == 2: 
        print("You won, Congrats!")
