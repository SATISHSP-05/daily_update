student = ['satish','shyam','swaroop']
marks = [1,2,3]
result = zip(student, marks)
print(list(result))

arr = [1, 2, 3, 2, 4, 2, 5]
num = int(input("Enter number "))
count = arr.count(num)
print(count)


def add (a, b):
    return a + b
a = input("enter")
b = input("enter")
print(add)
    



num = [1,2,3,4]
result = map(lambda n: n*3, num)
print(list(result))


num = [1,2,3,4,44,553,23,32]
result = filter(lambda n: n>=3, num)
print(list(result))

from functools import reduce
num = [1,2,3,4,44,553,23,32]
result = reduce(lambda y,n: y+n, num)
print(result)

student = ['satish','hemanth','swaroop']
marks = [1,2,3]
result = zip(student, marks)
print(dict(result))



damar = {'satish': 1, 'hemanth': 2, 'swaroop': 3}
name, marks = zip(*damar.items())
print(name)
print(marks)

stydent = [('satish', 1), ('hemanth', 2), ('swaroop', 3)]
name, marks = zip(*stydent)
print(name)
print(marks)



# -------class-----------
class student:
    def __init__(self, name, marks):
        self.name =  name
        self.marks = marks
        print("adding")
s1 = student("satish", 97)
print(s1.name, s1.marks)





class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def avg_marks(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("you hav3", self.name, "average marks in", sum/3)
s1 = student("satish", [69,23,56,87])
s1.avg_marks()



