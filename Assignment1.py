# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Initialize the sum variable
sum_of_evens = 0

# Loop through the list
for num in numbers:
    # Check if the number is even
    if num % 2 == 0:
        # Add it to the sum
        sum_of_evens += num

# Print the result
print("Sum of even numbers:", sum_of_evens)
