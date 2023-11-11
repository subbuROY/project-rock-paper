import random

User_number = int(input("Enter the Number 0 to 3:->"))
Computer_number = random.randrange(0, 3)
if User_number == Computer_number:
    print("Congratulations You Win")
else:
    print("Sorry Beter Luck Next Time")
