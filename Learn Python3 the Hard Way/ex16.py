from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("If you dont want thjat hit CTRL-C (^C).")
print("if you do wan that hit RETURN.")

input("?")

print("opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now im going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("Im going to write these to a file.")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

combined = line1 + line2 + line3

target.write(combined)

print("And finally, we close it")
target.close()