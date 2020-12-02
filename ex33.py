i = 0
numbers = []

print("Beginning of loop.")
while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)
    print("Middle of the loop.")
    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")
print("Ending of the loop.")

for num in numbers:
    print(num)
