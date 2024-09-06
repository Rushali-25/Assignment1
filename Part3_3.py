# Take an integer input
num = int(input("Enter an integer: "))

# Print the binary, octal, and hexadecimal equivalents
print("Binary:", bin(num))
print("Octal:", oct(num))
print("Hexadecimal:", hex(num))

# Alternatively, using a for loop to demonstrate iterating over the formats
formats = ['Binary', 'Octal', 'Hexadecimal']
for fmt in formats:
    if fmt == 'Binary':
        print(f"{fmt}: {bin(num)}")
    elif fmt == 'Octal':
        print(f"{fmt}: {oct(num)}")
    elif fmt == 'Hexadecimal':
        print(f"{fmt}: {hex(num)}")
