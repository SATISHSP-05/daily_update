
count=1
while count<=4:
    print("hello")
    count+=1




i=1
while i<=100:
    print(i)
    i+=1


i=100
while i>=1:
    print(i)
    i-=1


i=1
while i<=10:
    print("3*",3*i)
    i+=1




num=[9,8,7,6,6,5,5,4]
i=0
while i<len(num):
    print(num[i])
    i+=1



num=(1,22,33,44,55,4,4,6,6,6,77)
x=55
i=0
while i<len(num):
    if(num[i] == x):
        print("helo", x)
    i+=1



num=(1,22,33,44,55,4,4,6,6,6,77)
x=55
i=0
while i<len(num):
    if(num[i] == x):
        print("helo", x)
    else:
        print("finding...")
    i+=1



i=1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1


i=1
while i<= 5:
    if(i == 3):
        i+=1
        continue
    print(i)
    i+=1



i=1
while i<= 10:
    if(i%2 != 0):
        i+=1
        continue
    print(i)
    i+=1


str = "stish"
for i in str:
    if(i == 't'):
        print("found", i)
        break
    print(i)
else:
    print("end")

tup = (1,2,3,4,5,7,0)
x=5
i=0
for el in tup:
    if(el == x):
        print("found")
        break
        i+=1
else:
    print("end")

numbers = [1, 2, 3, 4, 5, 6]

for n in numbers:
    if n % 2 == 0:
        print(n)