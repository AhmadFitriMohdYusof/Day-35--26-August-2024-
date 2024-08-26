# Task 1: Tuple

#Create Tuple
fruits = ("apple", "banana", "cherry", "date")

# Print the first and last element of the tuple.
print("First element:", fruits[0])
print("Last element:", fruits[-1])

#Tuple Operations
numbers = (1, 2, 3, 4, 5)

a, b, *rest = numbers

print("a:", a)
print("b:", b)
print("rest:", rest)

# Immutability
try:
    fruits[1] = "blueberry"
except TypeError as e:
    print("Error:", e)


# Task 2: Sets

#Create Set
colors = {"red", "green", "blue", "yellow"}
colors.add("purple")
print(colors) 

#Set Operations
primary_colors = {"red", "blue", "yellow"}

intersection = colors.intersection(primary_colors)
print("Intersection:", intersection)

union = colors.union(primary_colors)
print("Union:", union)

difference = colors.difference(primary_colors)
print("Difference:", difference)

# Set Membership
is_green_in_primary = "green" in primary_colors
print("Is 'green' in primary_colors?", is_green_in_primary)

is_orange_not_in_colors = "orange" not in colors
print("Is 'orange' not in colors?", is_orange_not_in_colors)


#Task 3:Dictionary

#Create Dictionary
student_grades = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "Diana": 92
}

print("Bob's grade:", student_grades["Bob"])

#Dictionary Operations
student_grades["Eve"] = 88

student_grades["Alice"] = 95

del student_grades["Charlie"]

print("Updated student grades:", student_grades)

#Loop
for name, grade in student_grades.items():
    print(f"Student: {name}, Grade: {grade}")
