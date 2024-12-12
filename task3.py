#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""

x = 0.5

while round(x,4) != round(x,0):
    x = float(input("what is your number=> "))
    x = x / 2
    if round(x,4) != round(x,0):
        print("that is not an even integer")

print("that is an even integer")