class A:
    def showA(self):
        print("A")
class B(A):
    def showB(self):
        print("B")
obj = B()
obj.showA()
obj.showB()


class A1:
    def show(self):
        print("A1")
class B1(A1):
    pass
class C1(B1):
    pass
C1().show()



class Parent:
    def msg(self):
        print("Parent")
class Child1(Parent):
    pass
class Child2(Parent):
    pass
Child1().msg()
Child2().msg()


class X:
    def __init__(self):
        print("X")
class Y(X):
    def __init__(self):
        super().__init__()
        print("Y")
Y()

class Father:
    def work(self):
        print("Father Working")
class Son(Father):
    def work(self):
        print("Son Studying")
Son().work()




class Dog:
    def sound(self):
        print("Bark")
class Cat:
    def sound(self):
        print("Meow")
Dog().sound()
Cat().sound()


class Car:
    def start(self):
        print("Car Start")
class Bike:
    def start(self):
        print("Bike Start")
def start_vehicle(v):
    v.start()
start_vehicle(Car())
start_vehicle(Bike())


class Parent:
    def show(self):
        print("Parent")
class Child(Parent):
    def show(self):
        print("Child")
Child().show()



# ENCAPSULATION


class Bank:
    def __init__(self):
        self.__money = 500
    def show(self):
        print(self.__money)
Bank().show()

class Student:
    def __init__(self):
        self.__marks = 90
    def getMarks(self):
        print(self.__marks)
Student().getMarks()


