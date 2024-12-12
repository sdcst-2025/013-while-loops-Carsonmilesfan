#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:

username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied

example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 12345
Access granted


"""

skibidi = ""
toilet = ""

while skibidi != "admin" and toilet != "12345":
    skibidi = input("what is your name=> ")
    toilet = input("what is your password=> ")
    if skibidi != "admin" and toilet != "12345":
        print("incorrect answer, please try again")

print("correct answer, access granted")