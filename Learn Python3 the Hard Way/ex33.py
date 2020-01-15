
def numbers_loop(x):
    i = 0
    numbers = []

    while i < x:
        print(f"At the top i9 is {i}")
        numbers.append(i)

        i = i + 1

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

times_to_loop = int(input("Enter number of times to loop: "))



numbers_loop(times_to_loop)