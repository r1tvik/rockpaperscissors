import random
options=["rock", "paper", "scissors"]
print("These are the options:" + "\n"+  str(options))

computer=random.choice(options)
print(computer)
while True:
    guess = input("Pick one: ")
    guess=guess.lower()
    if guess==computer:
        print("You drawed")
        break
    elif guess=="rock" and computer=="scissors":
        print("You won!")
        print("Computer:", (computer))
        break
    elif guess == "paper" and computer == "scissors":
        print("You lost!")
        print("Computer:", (computer))
        break
    elif guess=="scissors" and computer=="paper":
        print("You won!")
        print("Computer:", (computer))
        break
    elif guess=="scissors" and computer=="rock":
        print("You lost!")
        print("Computer:", (computer))
        break
    elif guess=="paper" and computer=="rock":
        print("You won!")
        print("Computer:", (computer))
        break
    else:
        print("Error")
