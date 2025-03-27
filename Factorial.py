#This is a Factorial program.
#It firsts asks the user for their name then welcomes them to the program.
name = input("What is your name?" )
print('Hello' + name + ' Welcome to this Factorial program!')
#Then the program asks the user which factorial they want to calculate
n = int(input("What factorial would you like to calculate?"))
while n <= 0:
  n = int(input("Please enter a positive integer: ")) #This ensures that the user enters a positive integer.
#The program then calculates the factorial of the number(n) that the user entered using a loop.
def calculate_factorial(n):
    result = 1
    #This is the loop to calculate the factorial
    for i in range(1, n + 1):
        result *= i
    return result

# Calculate the factorial of the entered number
factorial = calculate_factorial(n)

# Display the result
print(f"The factorial of {n} is {factorial}")


