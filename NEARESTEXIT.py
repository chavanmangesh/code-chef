# There are two exits in a bus with 100 seats:

# First exit is located beside seat number 1.
# Second exit is located beside seat number 100.
# Seats are arranged in a straight line from 1 to 100with equal spacing between any 2 adjacent seats.

# A passenger prefers to choose the nearest exit while leaving the bus.

# Determine the exit taken by passenger sitting on seat X.

# Input Format
# The first line of input will contain a single integer TT, denoting the number of test cases.
# Each test case consists a single integer X, denoting the seat number.
# Output Format
# For each test case, output LEFT if the passenger chooses the exit beside seat 1, RIGHT otherwise.

# You may print each character of the string in uppercase or lowercase (for example, the strings LEFT, lEft, left, and lEFT will all be treated as identical).


# Explanation:
# Test case 1: The exit is located beside seat 1. Hence, the passenger can take this exit without moving to any other seat.

# Test case 2: To take exit at seat 1, the passenger needs to move 4949 seats. However, to take the exit at seat 100, the passenger needs to move 50 seats. Thus, exit at seat 1 is closer.

# Test case 3: The exit is located beside seat 100. Hence, the passenger can take this exit without moving to any other seat.

# Test case 4: To take exit at seat 1, the passenger needs to move 2929 seats. However, to take the exit at seat 100, the passenger needs to move 7070 seats. Thus, exit at seat 1 is closer.


# 1====100
# X 

# cook your dish here

T = int(input())

for x in range(T):
    X=int(input())
    if(X>50):
        print('RIGHT')
    else:
        print('LEFT')