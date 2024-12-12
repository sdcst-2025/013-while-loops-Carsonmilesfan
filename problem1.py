##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied

example:
example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 1234
Access denied
Too many failed attempts. Access denied.
"""
z = 0
x = ""
y = ""
while x != "admin" and y != "1234" and z != 3:
    x = input("Enter username => ")
    y = input("enter password => ")
    z = z + 1
    if x != "admin" and y != "1234" and z != 3:
        print("access denied")
    

if x == "admin" and y == "1234":
    print("access granted")
else:
    print("Too many failed attempts, access denied")