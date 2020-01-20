import time

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

#.split will seperate all items in the string in to seperate items between ,
stuff = ten_things.split(' ')
print(stuff)
time.sleep(5)
more_stuff = ["Day", "Night", "Song", "Frisby", "Corn", "Banada", "Girl", "Boy"]

while len(stuff) != 10:
    #.pop() will take the last items from the list
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    #.append will add the item to the list
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) #woah! fancy
print(stuff.pop())
print(' '.join(stuff)) # what? Cool!
print('#'.join(stuff[3:5])) # super stellar!

