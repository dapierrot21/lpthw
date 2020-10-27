# When this file runs it wil first ask you for the script name and a created
# file name. Once done you will next be ask if you want to easre the file.
# if you dont you can just hit ctrl-c to exit the script or hit enter and empty
# the file and write to it. Next your prompt to enter 3 line that written to the
# created filename. Finally the file is closed.

from sys import argv

script, filename = argv

print(f"We're going to earse {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Emptying the file. Goodbye.")
# target.truncate() mot needed because the 'w' mode truncate the file also.

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

target.write(f"{line1}\n{line2}\n{line3}")


print("And finally, we close it.")
target.close()
