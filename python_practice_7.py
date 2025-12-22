
# 1) Function to check even or odd

def is_even(num):
    return num % 2 == 0

x = int(input("Enter a number: "))
print("Even?" , is_even(x))

#---------------------------------------

# 2) Function to find factorial (iterative)

def factorial_iterative(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

n = int(input("Enter number for factorial: "))
print("Factorial =", factorial_iterative(n))

#---------------------------------------

# 3) Function to find factorial (recursive)


def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

n = int(input("Enter number for recursive factorial: "))
print("Factorial =", factorial_recursive(n))

#---------------------------------------

# 4) Function to check if a string is palindrome

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

s = input("Enter a string: ")
print("Palindrome?", is_palindrome(s))

#---------------------------------------

# 5) Function to return max of three numbers

def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Max =", max_of_three(a, b, c))

#---------------------------------------

# 6) Function to generate Fibonacci series up to n terms
def fibonacci(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

n = int(input("FEnter number of Fibonacci terms: "))
print("Fibonacci series:", fibonacci(n))

#---------------------------------------

# 7) Simple calculator function
def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Division by zero error"
        return a / b
    else:
        return "Invalid operator"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+,-,*,/): ")
print("Result =", calculator(a, b, op))

#---------------------------------------

# 8) Function to count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count

s = input("Enter a string: ")
print("Number of vowels =", count_vowels(s))

#---------------------------------------



