my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'white'
my_hair = 'brown'
h_ft = my_height
h_inch = 0

print(f"Lets talk about {my_name}")
print(f"He's {my_height} inches tall")
print(f"He's {my_weight} Pounds Heavy.")
print("Actually thats not too heavy")
print(f"He's got {my_eyes} eyes and {my_hair} hair")
print(f"His teech are usually {my_teeth} depending on the coffee")

#This line is tricky, try to get it exactly
total = my_age + my_height + my_weight
print(f"If i add {my_age}, {my_height}, and {my_weight} i get {total}")


h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)
print("Your height is : %d cm." % h_cm)
