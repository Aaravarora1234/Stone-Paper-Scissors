import random
while True :
    Choicelist = ["stone","paper","scissors"]
    Userinput = str(input("Enter your choice (Stone/Paper/Scissors) : ")).lower()
    Computerchoice = random.choice(Choicelist)
    Validchoicechecker = Userinput in Choicelist
    if Validchoicechecker == True :
        if (Userinput == "stone" and Computerchoice == "stone"):
            print("The Computer picked Stone. Match Draw.")
        elif (Userinput == "stone" and Computerchoice == "paper"):
            print("The Computer picked Paper. Paper wraps Stone. Better luck next time.")
        elif (Userinput == "stone" and Computerchoice == "scissors"):
            print("The Computer picked Scissors. Stone blunts Scissors. Congratulations you won.")
        elif (Userinput == "paper" and Computerchoice == "stone"):
            print("The Computer picked Stone. Paper wraps Stone. Congratulations you won.")
        elif(Userinput == "paper" and Computerchoice == "paper"):
            print("The Computer picked Paper. Match Draw.")
        elif(Userinput == "paper" and Computerchoice == "scissors"):
            print("The Computer picked Scissors. Scissors cut Paper. Better luck next time.")
        elif (Userinput == "scissors" and Computerchoice == "stone"):
            print("The Computer picked Stone. Stone blunts Scissors. Better luck next time.")
        elif (Userinput == "scissors" and Computerchoice == "paper"):
            print("The Computer picked Paper. Scissors cut Paper. Congratulations you won.")
        elif (Userinput == "scissors" and Computerchoice == "scissors"):
            print("The Computer picked Scissors. Match Draw.")
        Functionlist = ["Y","N"]
        Playagain = str(input("Press 'Y' to play again or 'N' to exit : ")).upper()
        Validfunctionchhecker = Playagain in Functionlist
        if Validfunctionchhecker == True :
            if Playagain == "Y" :
                print("New game started.")
            else :
                print("Game ended by user.")
                break
        else :
            print("Invalid Function.")
    else :
        print("Invalid Function.")