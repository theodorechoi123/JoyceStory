from main import *
from work import *
from otherNeighbor import *

noseBleed = False

def TheoCar():
    print("Inside Theo's car you see his keys are still inside. ")
    print("But with the keys, you also see something dirty under the passenger seat. It almost looks like dried up blood. ")
    print("You look around the entire car to see if you can find anything else that can hint at what the blood is about, but you find nothing else. ")
    user = input("What would you like to do?(inv, keys, back, trunk): ")
    while(user != "inv" and user != "keys" and user != "back" and user != "trunk"):
        user = input("What would you like to do?(inv, keys, back, trunk): ")
    if(user == "inv"):
        print(inv)
        print()
        TheoCar()
    elif(user == "trunk"):
        print("You go back to the trunk and you open it. ")
        print("You see that there's nothing there but a shovel and it's clearly been used.\n ")
        TheoCar()
    elif(user == "keys"):
        print("You take the keys and put it in your pocket. \n")
        inv.append("keys")
        TheoCar()
    elif(user == "back"):
        print()
        BackToTheo()

def TheoCarUpdate():
    print("You go back to Theo's car and you sit on the driver's side. ")
    if(noseBleed):
        print("You still see the dried up blood and still wonder if it's because of his nose? ")
    if(inv.count("keys") > 0):
        go = input("Do you want to drive the car somewhere?(y, n): ")
        while(go != "y" and go != "n"):
            go = input("Do you want to drive the car somewhere?(y, n): ")
        if(go == "n"):
            print()
            TheoCarUpdate()
        if(go == "y"):
            loc = input("Where do you want to go?(work, across the street neighbor, nowhere): ")
            while(loc != "work" and loc != "across the street neighbor" and loc != "nowhere"):
                loc = input("Where do you want to go?(work, across the street neighbor, nowhere): ")
            if(loc == "work"):
                print()
                Workplace()
            if(loc == "across the street neighbor"):
                print()
                OtherNeighbor()
            if(loc == "nowhere"):
                print()
                TheoCarUpdate()
    print("You sit in Theo's car thinking if you had the key, you could go somewhere. You think to yourself you shouldn't have given the key to him. ")
    print("You go back out of the car and notice you're still late to work. \n")
    print("ADD MORE STUFF HERE") #NOT DONE YET


    
def BackToTheo():
    print("You go back inside and go up to Theo who is still cooking his eggs. ")
    print("Theo: 'Oh you're back already? Did you forget something?' ")
    user = input("What would you like to do?(inspect theo, give keys, talk, go back to car): ")
    while(user != "inspect theo" and user != "give keys" and user != "talk" and user != "go back to car"):
        user = input("What would you like to do?(inspect theo, give keys, talk, go back to car): ")
    if(user == "inspect theo"):
        print("Theo is still wearing his pajamas from last night with his messed up hair. ")
        print("He smells awful since he just woke up and you don't think he showered this morning yet. ")
        print("He's wearing his slippers that you got for him and he seems happy this morning. \n")
        BackToTheo()
    if(user == "give keys"):
        print("You show him his keys. ")
        print("Theo: 'OH! My keys! I was trying to look for them earlier. Thank you! Where were they? ' ")
        print("You tell him that they were in the car. ")
        print("Theo: 'Oh, I must have left them in there overnight. My bad... Hopefully no one stole anything. But there isn't much there anyways. ' ")
        BackToTheo()
    if(user == "talk"):
        print("1. I found dried blood in the car.")
        print("2. I found a shovel in your car. ")
        talk = input("What do you want to say?(1, 2): ")
        while(talk != "1" and talk != "2"):
            talk = input("What do you want to say?(1, 2): ")
        if(talk == "1"):
            print("Theo: 'Dried blood? I think its cause my nose was bleeding the other day. There was A LOT!")
            print("You don't remember him ever telling you about the nose bleed\n")
            noseBleed = True
            BackToTheo()
        if(talk == "2"):
            print("Theo: 'Shovel? I think its there cause remember I helped you out with your plants? We shoveled the ground in the front, remember? ")
            print("You recall that that happened but that was a year ago. Why is the shovel still in the car? \n")
            BackToTheo()
    if(user == "go back to car"):
        TheoCarUpdate()



TheoCar()