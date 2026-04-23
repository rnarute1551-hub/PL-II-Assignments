#Q1: Add two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a + b
print("Sum =", sum)
#Q2: Display variable types

a = 10
b = 3.5
c = "Python"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
#Q3: Type casting

a = "100"
b = int(a)   # string to int
print(b, type(b))

c = 10
d = float(c)  # int to float
print(d, type(d))
#Q4: Logical operators

a = True
b = False

print("AND:", a and b)
print("OR:", a or b)
print("NOT:", not a)
