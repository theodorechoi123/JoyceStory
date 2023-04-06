def BedroomDoor():
    print("You go out of your room and you notice that your Theo is cooking some eggs. ")
    print("Theo: Hi my babyyy. Did you sleep okay? I got eggs for you!")
    user = input("Would you like to eat the eggs?(y/n): ")
    while(user != "y" and user != "n"):
        user = input("Would you like to eat the eggs?(y/n): ")
    if(user == 'y'):
        print("You eat your eggs and you feel famished. You feel so full already!")
    elif(user == 'n'):
        print("Theo becomes really sad and goes back to cooking his share of breakfast. ")
        print("Theo: 'Make sure you get to work safe! I love you!' ")
        

def Closet():
    print("You go over to your closet and stumble and fall on your dirty laundry. ")
    print("You smell it so deeply that you lost your train of thought and end up sleeping there. ")

def NightStand():
    user = input("Which item would you like?(phone/wallet/lighter/knife): ")
    if(user == "phone"):
        print("You pick up your phone and put it in your pocket")
    elif(user == "wallet"):
        print("You pick up your wallet and look inside. You are poor. You put it in your pocket. ")
    elif(user == "lighter"):
        print("You pick up your lighter and try turning it on. It shines bright like a diamond! You put it in your pocket. ")
    elif(user == "knife"):
        print("You pick up the knife and examine it. You see how sharp it is and put it in your pocket. ")
    else:
        print("You don't know what you're doing and end up stabbing yourself with the knife and burning yourself on fire. ")

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

    user = input("Would you like to play again?(y/n): ")
    while(user != "y" and user != "n"):
        user = input("Would you like to play again?(y/n): ")

    if(user == "y"):
        Main()
    if(user == "n"):
        exit()

Main()
    