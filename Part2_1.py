# Take input for first and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Reverse the first and last name and join them with a space
reversed_name = last_name[::-1] + " " + first_name[::-1]

# The `[::-1]` is a string slicing method that reverses the string.
# `+ " "` is used to concatenate the reversed names with a space in between.

# Print the reversed names
print("Reversed name:", reversed_name)
