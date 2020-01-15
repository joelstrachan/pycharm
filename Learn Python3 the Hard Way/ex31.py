print("""You enter a dark roiom with two doors
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("THese's a giant bear here eating a cheese cake")
    print("What doi you do?")
    print("1. Take the cake.")
    print("2. scream at the bear. ")


    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. good job!")
    elif bear == "2":
        print("the bear ears your legs off. good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away. ")

elif door == "2":
    print("You stare into the endless abyss at cthulu's retina.")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies")


    insanity = input("> ")

    if insanity == "1" or insanity == "2":
            print("Your body survives powered by a mind of jello.")
            print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck")
        print("Good Job!")

else:
    print("You stumble around and fall on a knife and die. good job")
