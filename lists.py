#Write a program to find the largest and smallest number in a list.
list=[1,4,8,5,9]
largest=max(list)
smallest=min(list)

print(largest)
print(smallest)

#Merge two lists into one.
a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)

#Check if a specific item (e.g., "grape") exists in a list.
fruits = ["apple", "banana", "orange", "grape", "mango"]

# Check if "grape" exists
if "grape" in fruits:
    print("Grape is in the list.")
else:
    print("Grape is not in the list.")
