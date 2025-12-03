num = 12344

def sumDigits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

print("Sum =", sumDigits(num))


# lambda

square = lambda x: x * x
print(square(5))



add = lambda a, b: a + b
print(add(10, 20))



even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(even(7))


map


numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, numbers))
print(result)


nums = [10, 20, 30]
print(list(map(lambda x: str(x), nums)))



nums = [2, 3, 4]
print(list(map(lambda x: x*x, nums)))


# filter

numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)


nums = [5, 12, 7, 18, 3]
print(list(filter(lambda x: x > 10, nums)))



words = ["apple", "banana", "ant", "cat"]
print(list(filter(lambda w: w.startswith("a"), words)))





# reduce


# it must be import  reduce

from functools import reduce

numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)
print(result)


from functools import reduce
nums = [2, 3, 4]
print(reduce(lambda x, y: x * y, nums))


from functools import reduce
nums = [10, 50, 20, 7]
print(reduce(lambda x, y: x if x > y else y, nums))

