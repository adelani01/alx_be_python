# Drawing Patterns with Nested Loops

# Prompt User for Pattern Size:
Pattern_size = int(input("Enter the size of the pattern: "))

# Draw the pattern
row = 0
count = 0
while count < Pattern_size:
        for  row in range(Pattern_size):
            print("*", end="")
        print()
        count += 1
        