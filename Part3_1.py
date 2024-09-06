while True:
    # Ask the user for a number
    user_input = input("Enter a number (or type 'exit' to stop): ")

    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        break  # Exit the loop

    try:
        # Convert the input to a float
        number = float(user_input)

        # Determine if the number is positive, negative, or zero
        if number > 0:
            print("The number is positive.")
        elif number < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")
    except ValueError:
        # If the input is not a valid number, continue the loop
        print("Invalid input, please enter a valid number.")
        continue
