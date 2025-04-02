'''
ASSIGNMENT 2:
Module 3: Control Structures in Python

Task 1: Check if a Number is Even or Odd
Problem Statement:  Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.


num1=int(input('Enter a number: '))
if num1 %2==0:#using % to ensure whether the number is divisible by 2 or not
    print(f'{num1} is an Even number')
else:
    print(f'{num1} is an Odd number')


Task 2: Sum of Integers from 1 to 50 Using a Loop

Problem Statement: Write a Python program that:
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.

'''
# Initialize a variable to store the sum
total_sum = 0

# Use a for loop to iterate over numbers from 1 to 50
for number in range(1, 51):  # range(1, 51) generates numbers from 1 to 50
    total_sum += number  # Add the current number to the total_sum

# Display the final sum
print(f"The sum of integers from 1 to 50 is: {total_sum}")
