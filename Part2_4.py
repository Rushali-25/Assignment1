# Prompt the user to enter the length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area of the rectangle
area = length * width

# Display the result using the format method to show two decimal places
print("The area of the rectangle is: {:.2f}".format(area))