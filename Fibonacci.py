#This ia a Fibonacci program.
#This program will ask the user for a number and then print the Fibonacci sequence up to that number.
#First the program asks for the user's name and greets the user.
name = input("What is your name? ")
print("Hello " + name + " Welcome to this Fibonacci program.")
#Then the program asks the user how many numbers(n) they want in the sequence.
n = int(input("How many numbers would you like in the sequence? "))
#This ensures that the user enters a positive integer.
while n <= 0:
  n = int(input("Please enter a positive integer: "))
#Then the program generates a fibonacci sequence up to the term(n) the user entered.
#The first two terms are 0 and 1.
#The terms are defined by the formula Fn = Fn-1 + Fn-2.
def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    #The program is recalling itself to generate the next term.
    return fibonacci(n-1) + fibonacci(n-2)

#The program prints the fibonacci sequence up to the term(n) the user entered.
for i in range(n):
  print(fibonacci(i))