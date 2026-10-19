# Exercises: Day 7

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_companies.update(['tiktok', 'Snapchat', 'Instagram'])
print(it_companies)

it_companies.remove('Google')
print(it_companies)

# Exercises: Level 2

C = A.union(B)
print(C)
print(A.intersection(B))
print(A.isdisjoint(B))
print(A.issubset(B))

print(A.symmetric_difference(B))

del A
del B

# Exercises: Level 3

age_two = set(age)

print(len(age))
print(age_two)
print(len(age_two))