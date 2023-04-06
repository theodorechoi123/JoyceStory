from work import *
from johnson import *
from car import *

inv = []

def BedroomDoor():
    print("You go out of your room and you notice that your Theo is cooking some eggs. ")
    print("Theo: Hi my babyyy. Did you sleep okay? I got eggs for you!")
    user = input("Would you like to eat the eggs?(y/n/inv): ")
    while(user != "y" and user != "n" and user != "inv"):
        user = input("Would you like to eat the eggs?(y/n/inv): ")
    if(user == 'y'):
        print("You eat your eggs and you feel famished. You feel so full already!")
        print("Theo: 'I love you so much my baby! Don't work too hard and get to work safe!' ")
        FrontDoor()
    elif(user == 'n'):
        print("Theo becomes really sad and goes back to cooking his share of breakfast. ")
        print("Theo: 'Make sure you get to work safe.. I love you...' ")
        FrontDoor()
    elif(user == "inv"):
        print(inv)
        print("")
        BedroomDoor()
        
def FrontDoor():
    print("You go outside and feel the fresh warm air on your face. ")
    print("In front of you, you see your neighbor across the street mowing the lawn. You can start walking this way to get to work. ")
    print("On your left, you see your neighbor's house. Miss Johnson lives there and she's a widow. She lost her husband recently so her house has been gloomy ever since. ")
    print("On your right, you see Theo's car and it's almost glistening in the sunlight. ")
    user = input("What do you want to do?(forward, left, right, inv): ")
    while(user != "forward" and user != "left" and user != "right" and user != "inv"):
        user = input("What do you want to do?(forward, left, right, inv): ")
    if(user == "forward"):
        Workplace()
    elif(user == "left"):
        print("You walk over to your neighbors house and see that its covered in vines. It's very quiet and when you peer into the house, you don't see anything moving.")
        print("It's very dark inside and you see that theres white sheets over the furniture. ")
        print("You look over at the front door and you see that it's not closed. There's a small crack in the front door and you could easily walk inside. ")
        ans = input("Do you want to go inside?(y/n/inv): ")
        while(ans != "y" and ans != "n" and ans != "inv"):
            ans = input("Do you want to go inside?(y/n/inv): ")
        if(ans == "y"):
            Neighbor()
        elif(ans == "n"):
            FrontDoor()
        elif(ans == "inv"):
            print(inv)
            print("")
            FrontDoor()
    elif(user == "right"):
        print("You look at Theo's car some more. ")
        print("It's a green Toyota Rav4 and it has its wear and tear from driving countless hours to work and bringing you around. ")
        print("You try to open the door and you realize it's unlocked. ")
        ans = input("Do you want to see what's inside?(y/n/inv): ")
        while(ans != "y" and ans != "n" and ans != "inv"):
            ans = input("Do you want to see what's inside?(y/n/inv): ")
        if(ans == "y"):
            TheoCar()
        elif(ans == "n"):
            FrontDoor()
        elif(ans == "inv"):
            print(inv)
            print()
            FrontDoor()
    elif(user == "inv"):
        print(inv)
        print()
        FrontDoor()
            

def Closet():
    print("You go over to your closet and stumble and fall on your dirty laundry. ")
    print("You smell it so deeply that you lost your train of thought and end up sleeping there. ")
    print("Game Over")
    exit()

def NightStand():
    user = input("Which item would you like?(phone/wallet/lighter/knife): ")
    while(user != "phone" and user != "wallet" and user != "lighter" and user != "knife"):
        user = input("Which item would you like?(phone/wallet/lighter/knife): ")
    if(user == "phone"):
        print("You pick up your phone and put it in your pocket")
        print("You just aquired an item.")
        inv.append("phone")
        BedroomDoor()
    elif(user == "wallet"):
        print("You pick up your wallet and look inside. You are poor. You put it in your pocket. ")
        print("You just aquired an item.")
        inv.append("wallet")
        BedroomDoor()
    elif(user == "lighter"):
        print("You pick up your lighter and try turning it on. It shines bright like a diamond! You put it in your pocket. ")
        print("You just aquired an item.")
        inv.append("lighter")
        BedroomDoor()
    elif(user == "knife"):
        print("You pick up the knife and examine it. You see how sharp it is and put it in your pocket. ")
        print("You just aquired an item. ")
        inv.append("knife")
        BedroomDoor()

def Main():
    print("For this game, type one word answers")
    user = input("Do you understand?(y/n): ")
    while(user != "y" and user != "n"):
        user = input("Enter y or n: ")
    if(user == "n"):
        print("ok byeeeee")
        exit()
    elif(user == "y"):
        print("")

    print("You wake up from your slumber and you see that you've woken up way past your bedtime. ")
    print("You're nervous that you're going to be late for work and so you jump out of bed in a hurry")
    print("On your left you can walk out of your room.  ")
    print("On your right, you see your phone, wallet, lighter, and a small knife")
    print("Ahead of you, you see your closet doors filled with so many clothes. ")
    print("Behind you is your messed up bed while you were getting up. ")
    ans = input("What would you like to do?(forward, backward, left, right): ")
    while(ans != "forward" and ans != "backward" and ans != "left" and ans != "right"):
        ans = input("What would you like to do?(forward, backward, left, right): ")
    if(ans == "left"):
        BedroomDoor()
    elif(ans == "right"):
        NightStand()
    elif(ans == "forward"):
        Closet()
    elif(ans == "backward"):
        print("You go back to sleep and don't care about your job. ")
        print("Game Over")
        exit()

Main()
    