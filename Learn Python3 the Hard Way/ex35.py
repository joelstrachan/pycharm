from sys import exit

def gold_room():
    print("THis room is full of gold. how much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, your to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You Greedy basterd")

def bear_room():
    print("There is a bear here.")
    print("The bean has a bunch of honey")
    print("The fat bean is in front of another door.")
    print("how are oyu going to move the bear?")
    bear_moved = false

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear look at you and then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("Thje bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("i got no idea what that means")

def cathulhu_room():
    print("Her you see the great eveil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life oe eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cathulhu_room()

def dead(why):
    print(why, "good job!")
    exit(0)

def start():
        print("You are in a dark room.")
        print("There is a door at your right and left.")
        print("Which one do you take?")

        choice = input("> ")

        if choice == "left":
            bear_room()
        elif choice == "right":
            cathulhu_room()
        else:
            dead("You stumble around the room untill you starve")

start()