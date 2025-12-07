class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(self.name, self.marks)
s1 = Student("Rahul", 85)
s1.display()


class Bank:
    def __init__(self, bal):
        self.bal = bal
    def deposit(self, amt):
        self.bal += amt
    def show(self):
        print(self.bal)
b = Bank(1000)
b.deposit(500)
b.show()



class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def area(self):
        print(self.l * self.w)
r = Rectangle(5, 4)
r.area()


class Calculator:
    def add(self, a, b):
        print(a + b)
c = Calculator()
c.add(10, 20)


class Employee:
    def __init__(self, sal):
        self.sal = sal
    def bonus(self):
        print(self.sal + 2000)
e = Employee(25000)
e.bonus()


class Person:
    def __init__(self, age):
        self.age = age
    def voting(self):
        print(self.age >= 18)
p = Person(20)
p.voting()


class Number:
    def __init__(self, n):
        self.n = n
    def square(self):
        print(self.n * self.n)
n1 = Number(6)
n1.square()


class Book:
    def __init__(self, price):
        self.price = price
    def discount(self):
        print(self.price - 100)
b = Book(500)
b.discount()


class Product:
    def __init__(self, qty, price):
        self.qty = qty
        self.price = price
    def total(self):
        print(self.qty * self.price)
p = Product(3, 150)
p.total()


class Temperature:
    def __init__(self, c):
        self.c = c
    def to_f(self):
        print((self.c * 9/5) + 32)
t = Temperature(30)
t.to_f()


class Login:
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd
    def verify(self):
        print(self.user == "admin" and self.pwd == "1234")
l = Login("admin", "1234")
l.verify()


class EvenOdd:
    def __init__(self, n):
        self.n = n
    def check(self):
        print(self.n % 2 == 0)
e = EvenOdd(15)
e.check()


class SumDigits:
    def __init__(self, n):
        self.n = n
    def calculate(self):
        s = 0
        for i in str(self.n):
            s += int(i)
        print(s)
s = SumDigits(1234)
s.calculate()


class Reverse:
    def __init__(self, s):
        self.s = s
    def rev(self):
        print(self.s[::-1])
r = Reverse("python")
r.rev()
