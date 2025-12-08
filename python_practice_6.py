

# 1) Check if a number is positive, negative or zero


num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#---------------------------------------


# 2) Check if a number is even or odd


n = int(input(" Enter a number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

#---------------------------------------



# 3) Find the largest of three numbers


a = int(input("Enter first number: "))
b = int(input(" Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest =", largest)

#---------------------------------------


# 4) Print numbers from 1 to N using a for loop

N = int(input("Enter N: "))
for i in range(1, N + 1):
    print(i, end=" ")
print()

#---------------------------------------


# 5) Sum of first N natural numbers using a while loop


N = int(input("Enter N: "))
total = 0
i = 1
while i <= N:
    total += i
    i += 1
print("Sum of first", N, "numbers =", total)

#---------------------------------------

# 6) Factorial of a number using a loop


n = int(input("Enter number for factorial: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial of", n, "=", fact)

#---------------------------------------


# 7) Check if a number is prime


num = int(input("Enter a number to check prime: "))
if num <= 1:
    print("Not Prime")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime")
    else:
        print("Not Prime")

#---------------------------------------

# 8) Count digits of a number using a loop
num = int(input("Enter a number to count digits: "))
count = 0
temp = abs(num)
if temp == 0:
    count = 1
else:
    while temp > 0:
        count += 1
        temp //= 10
print("Number of digits =", count)

#---------------------------------------

# 9) Reverse a number using a loop
num = int(input("Enter a number to reverse: "))
rev = 0
temp = abs(num)
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
if num < 0:
    rev = -rev
print("Reversed number =", rev)

#---------------------------------------


# 10) Print a simple pattern (right triangle of stars)
rows = int(input("Enter number of rows for pattern: "))
for i in range(1, rows + 1):
    print("*" * i)

#---------------------------------------
