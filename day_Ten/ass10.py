#  Exercises: Day 10
for i in range(11) :
    print(i)

count = 0
while count <= 10 :
    print(count)
    count += 1

for i in range(10, -1, -1) :
    print(i) 

count = 10
while count >= 0 :
    print(count)
    count -= 1

for i in range (1, 8):
    print("#" * i)

for i in range(9) :
    for j in range (9) :
        print("# " *  i, j)


for i in range(11):
    print(f"{i} x {i} = {i * i}")


items = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

for item in items:
    print(item)

for i in range(0, 101, 2):
    print(i)


for i in range(1, 101, 2):
    print(i)


total = 0

for i in range(101):
    total += i

print("The sum of all numbers is", total)


even_sum = 0
odd_sum = 0

for i in range(101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("The sum of all evens is", even_sum)
print("The sum of all odds is", odd_sum)



