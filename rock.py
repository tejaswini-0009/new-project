import random

game_list =["Rock","Papper","Scissors"]

computer = c = 0
command = p =0
print("Score: Computer"+str(c)+"Player "+str(p))

run=True
while run:
    computer_choice = random.choice(game_list) # line of code gives random choice in game_list
    command = input("Rock ,Papper, Scissors or Quit :")
    if command ==computer_choice:
        print("Tie")
    elif command =='Rock':
        if computer_choice == 'Scissors':
            print("Player Won!")
            p+=1
        else:
            print("Computer Won!")
            c+=1
    elif command =="Papper":
        if computer_choice=='Rock':
            print("Player Won !")
            p+=1
        else:
            print("Computer won !")
            c+=1
    elif command=="Scissors":
        if computer_choice=='Papper':
            print("Player Won!")
            p+=1
        else:
            print("Computer Won!")
            c+=1
    elif command=="Quit":
        break
    else:
        print("Wrong Command")
    print("Player:"+command)
    print("Computer :"+computer_choice)
    print("")
    print("Score:Computer"+str(c)+"Player:"+str(p))
    print("")

