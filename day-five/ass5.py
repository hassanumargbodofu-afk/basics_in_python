# # #  exercise 1

# # umar = []

# # food = ["amala", "rice", "beans", "spag", "yam"]

# # print(len(food))

# # print(food[0])
# # print(food[2])
# # print(food[4])

# # mixed_data_types = ["umar", "19", "67", "single", "olaiya plaza" ]

# it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# print(it_companies)
# print(len(it_companies))
# print(it_companies[0])
# print(it_companies[3])
# print(it_companies[6])

# it_companies[0] = "instagram"

# it_companies.append("IT companies")

# it_companies.insert(3, "IT companies")

# it_companies[1] = it_companies[1].upper()

# print(it_companies)

# print("#; ".join(it_companies))

# print("Facebook" in it_companies)

# print(it_companies.reverse())

# print(it_companies[:3])

# print(it_companies[5:7])

# print(it_companies[:4])

# print(it_companies.remove(it_companies[1]))

# print(it_companies.clear())

# del it_companies

from statistics import median


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

print(" ".join(front_end + back_end))

full_stack = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']

full_stack.insert(0, 'SQL')
full_stack.insert(1, 'Python')

print(full_stack)

# execise 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)
print(min(ages) + max(ages))

average = sum(ages) / len(ages)
print(average)

range = max(ages) - min(ages)
print(range)

