#Q1: Greatest of 3 numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Greatest is:", a)
elif b > c:
    print("Greatest is:", b)
else:
    print("Greatest is:", c)
#Q2: Odd or Even

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
#Q3: Uppercase or Lowercase

ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
else:
    print("Not an alphabet")
#Q4: Number or Character

x = input("Enter something: ")

if x.isdigit():
    print("It is a number")
else:
    print("It is a character")
