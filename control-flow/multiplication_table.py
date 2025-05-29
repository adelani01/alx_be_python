# Multiplication times table

#Prompt User for a Number:
number = int(input("Enter a number to see it multiplication table: "))


#Generate and Print the Multiplication Table:

for n in range(1,11):
    z = number * n
    print(f"{number} * {n} = {z} ")
    