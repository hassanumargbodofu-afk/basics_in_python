# Exercise level 1

food = ()
print(food)

sisters = ("Rihanat", 'husseinat', "Aisha")
brothers = ('Ahmad', 'bashir', 'Muhammad')
siblings = sisters + brothers
print(siblings)
print(len(siblings))

family_members = list(siblings)
family_members.extend(['hassan', 'hassanat'])
print(family_members)

# Exercise level 2

fruits = ('apple', 'banana', 'orange')
vegetables = ('okro', 'Ewedu', 'spinach')
animal_products = ('milk', 'meat', 'eggs')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)

print(food_stuff_lt[4])

print(food_stuff_lt[0:3])

del food_stuff_tp 

print(food_stuff_lt[4])
print('Ewedu' in food_stuff_lt)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print( 'Iceland' in nordic_countries)