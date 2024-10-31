import random
# project file is always named main.py and not main_project.py like here
computer= random.choice([-1,0,1])# here we used the random module withe the choice the random module chooses a number at random from the given data and the choose helps in specifying the dataset within the random module this is crucial as we need the computer to choose the choices randomly
youstr= input("enter your choice: ")
youdict={"r":1,"p":-1,"s":0} # first we get the r p s to be converted in number  
reverseDict={1:"rock", -1:"paper", 0:"scissor"}# then we use the reverse dictionary to convert number into the choice of rock paper scissor

you = youdict[youstr]

print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if (computer==you):
    print("its a draw")

else:
    if(computer==-1 and you==1):
        print("you win")
    elif(computer==-1 and you==0):
        print("you lose")
    elif(computer==1 and you==-1):
        print("you lose")
    elif(computer==1 and you==0):
        print("you win")
    elif(computer==0 and you==-1):
        print("you win")
    elif(computer==0 and you==1):
        print("you lose")
    else:
        print("something went wrong")


