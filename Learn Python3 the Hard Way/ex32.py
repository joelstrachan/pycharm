the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears','apricots']
change = [1, 'pennies', 2, 'dimes',3, 'quarters']

#this first kind of for-loop goes through a list

for number in the_count:
    print(f"this is count {number}")

#same as fruits
for fruit in fruits:
    print(f"A fuuit of type: {fruit}")

# we can also build lists , first start with an empty one
elements = []

# then use the range fucntion to do 0 to 5 counts
for i in range (0, 6):
    print(f"Adding {i} to the list.")
    #append is a function that lists understands
    elements.append(i)

#now we can print them out too
for i in elemets:
    print(f"Element was: {i}")


