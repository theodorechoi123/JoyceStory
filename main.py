from inventory import *



########
########    Begin Story #################################################################################################################################################
########
def BedroomDoor():
    print("You go out of your room and you notice that your Theo is cooking some eggs. ")
    print("Theo: Hi my babyyy. Did you sleep okay? I got eggs for you!")
    user = input("Would you like to eat the eggs?(y/n/inv): ")
    while(user != "y" and user != "n" and user != "inv"):
        user = input("Would you like to eat the eggs?(y/n/inv): ")
    if(user == 'y'):
        print("You eat your eggs and you feel famished. You feel so full already!")
        print("Theo: 'I love you so much my baby! Don't work too hard and get to work safe!' \n")
        FrontDoor()
    elif(user == 'n'):
        print("Theo becomes really sad and goes back to cooking his share of breakfast. ")
        print("Theo: 'Make sure you get to work safe.. I love you...' \n")
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
        print()
        Workplace()
    elif(user == "left"):
        print("You walk over to your neighbors house and see that its covered in vines. It's very quiet and when you peer into the house, you don't see anything moving.")
        print("It's very dark inside and you see that theres white sheets over the furniture. ")
        print("You look over at the front door and you see that it's not closed. There's a small crack in the front door and you could easily walk inside. ")
        ans = input("Do you want to go inside?(y/n/inv): ")
        while(ans != "y" and ans != "n" and ans != "inv"):
            ans = input("Do you want to go inside?(y/n/inv): ")
        if(ans == "y"):
            print()
            Neighbor()
        elif(ans == "n"):
            print()
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
            print()
            TheoCar()
        elif(ans == "n"):
            print()
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
        print()
        BedroomDoor()
    elif(ans == "right"):
        print()
        NightStand()
    elif(ans == "forward"):
        print()
        Closet()
    elif(ans == "backward"):
        print("You go back to sleep and don't care about your job. ")
        print("Game Over")
        exit()

Main()


########
########    Car Story #################################################################################################################################################
########


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
    print("You go back out of the car and notice you're still late to work. So you start heading there now. \n")
    CarWork()


def CarWork():
    print("You go to work and you still work at Yogurtland. You're the manager of the place and you were supposed to open. ")
    print("When you get there you unlock the door and start to get to work. ")
    print("You head to the back and you see a note that was left in the break room. ")
    print("On the note it reads, 'Joyce make sure to clean the place, I'll be coming in at 11:00AM' ")
    print("You check the time and it reads '10:45'")
    print("There's not enough time so you start working right away. ")
    user = input("What do you do first?(machines, cooler, floors, register): ")
    while(user != "machines" and user != "cooler" and user != "floors" and user != "register"):
        user = input("What do you do first?(machines, cooler, floors, register): ")
    if(user == "machines"):
        print("You clean the machines and get rid of all the excess yogurt. You scrub it down as fast as you can but the boss walks in soon after. ")
        print("Boss: 'Joyce? How come the place is a mess? Didn't I tell you to clean the place? I left a note!' ")
        print()
        CleanMachines()
    elif(user == "cooler"):
        print("You clean the cooler and try to figure out what orders you need to get. Once you're finished, the boss comes in. ")
        print("Boss: 'Joyce? How come the place is a mess? Didn't I tell you to clean the place? I left a note!' ")
        print()
        CleanMachines()
    elif(user == "floors"):
        print("You clean the floor and throw away the excess trash on the ground from last night. You throw away the trash and then the boss comes in. ")
        print("Boss: 'Joyce? I like the floors, but the yogurt machines aren't cleaned yet?! I left a note!' ")
        print()
        CleanMachines()
    elif(user == "register"):
        print("You count the money in the register to figure out how much money you have. Then the boss comes in.  ")
        print("Boss: 'Joyce? How come the place is a mess? Didn't I tell you to clean the place? I left a note! Why are you looking through the register?!' ")



def CleanMachines():
    do = input("What do you do?(talk, inv, run, fight): ")
    while(do != "talk" and do != "inv" and do != "run" and do != "fight"):
        do = input("What do you do?(talk, inv, run, fight): ")
    if(do == "talk"):
        print("1. I came in late to work. ")
        print("2. I hate you. ")
        print("3. I quit! ")
        print("4. I tried my best, but I suck at cleaning. ")
        ans = input("What do you say?(1, 2, 3, 4): ")
        while(ans != "1" and ans != "2" and ans != "3" and ans != "4"):
            ans = input("What do you say?(1, 2, 3, 4): ")
        if(ans == "1"):
            print("Boss: 'You came in late?! You need to start being more punctual. Next time make sure to get here ON TIME!'")
            print("Boss: 'Make sure to clean up fast. Customers are coming in soon. '")
            print()
            Working()
        elif(ans == "2"):
            print("Boss: 'What? I am YOUR BOSS. You need to treat me with some respect! YOU'RE FIRED!' ")
            print()
            Fired()
        elif(ans == "3"):
            print("Boss: 'WHAT?! YOU CAN'T QUIT! ARE YOU KIDDING ME?! WHATEVER, GET OUTTT!'")
            print("Your boss gets heated up and starts approaching you with ill intent. ")
            print()
            Fight()
        elif(ans == "4"):
            print("Boss: 'You suck at cleaning? Aren't you the manager of this place? I hired you cause I thought you were good at your job. '")
            print("Boss: 'I think you're lying. If you want to leave so much just say so. You can leave, I'll just clean this up. Just come back tomorrow alright?'")
            print()
            LeftWork()
    elif(do == "inv"):
        print(inv)
        print()
        CleanMachines()
    elif(do == "fight"):
        print()
        Fight()
    elif(do == "run"):
        print("You run away from your boss and head out of the store. ")
        print()
        LeftWork()

def LeftWork():
    print("You left work and now you don't know what to do. ")

def Fight():
    print("\nBATTLE START")

def Fired():
    print("You get fired from your job and get kicked out. ")

def Working():
    print("You get to work and you try to do it fast. ")
    
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


########
########    Across the Street Neighbor Story #################################################################################################################################################
########


def OtherNeighbor():
    print("You use the car to go cross the street to see your neighbor. ")

########
########    Neighbor Story #################################################################################################################################################
########


def Neighbor():
    print("You enter the house. ")

########
########    Work Story #################################################################################################################################################
########

def Workplace():
    print("You arrive at your work. ")
    print("You work as a barber apprentice and your mentor's name is ")