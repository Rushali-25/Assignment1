# Take two numbers as input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Check the parity of the numbers and print the result
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even.")
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Both numbers are odd.")
else:
    print("One number is even and the other is odd.")
