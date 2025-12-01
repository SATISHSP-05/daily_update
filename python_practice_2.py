def sum_(a, b):
    n = a + b 
    print(n)
    return sum_  
sum_ (1, 4)
sum_ (1, 8)



def sum_1(a, b):
    return a + b 
one = sum_1(1, 2) 
print(one)


def calculate(a, b, c):
    sum_ = a + b + c
    avg =  sum_ / 3
    print(avg)
    return avg 
calculate(1, 2 ,5)



def defp(a = 3, b = 5):
    print( a + b)
    return defp
defp()



num = [1,3,4,5,6,8,9]
str_ = ['aa','dd','fff','ttt']

def print_len(list):
    print(len(list))

print_len(num)
print_len(str_)


def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)
cal_fact(5)


def print_len(list):
    print(len(list))
def print_len(list):
    for item in list:
        print(item, end=" ")

print_len(num)
print_len(str_)


def converter(usd_vl):
    inr_vl = usd_vl*90
    print(usd_vl, "usd = ", inr_vl, "inr")
converter(5)


def odd_even(n):
    if n % 2 == 0:
        print(n, "even")
    else:
        print(n, "odd")
odd_even(3)



# --------------------------calculatore-----------------------------------------------------
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
op = input("Enter operator")

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")

# --------------------------calculatore_ method2-----------------------------------------------------

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b 

n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))
op = input("Enter operator: ")

if op == "+":
    print(add(n1, n2))
elif op == "-":
    print(sub(n1, n2))
elif op == "*":
    print(mul(n1, n2))
elif op == "/":
    print(div(n1, n2))
else:
    print("Invalid operator")

# --------------------------calculatore_ method2-------------------------------------------------


n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))
op = input("Enter operator: ")

match op:
    case "+":
        print(n1 + n2)
    case "-":
        print(n1 - n2)
    case "*":
        print(n1 * n2)
    case "/":
        print(n1 / n2 if n2 != 0 else "Cannot divide by zero")
    case _:
        print("Invalid operator")

