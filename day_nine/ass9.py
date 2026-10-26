# Exercises: Level 1

user = int(input("Enter your age: "))
if user >= 18 :
    print("You are old enough to drive") 
else:
    missing_age = 18 - user
    print(f"You need {missing_age} more years to learn to drive.")

my_age = 19 
your_age =  int(input("Enter your age: ")) 

if my_age > your_age and (years_older := 19 - your_age):
    print(f"You are {years_older} years older than me")

else:
    print("We are the exact same age!")


a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b :
    print(f"{a} is grater than {b}")
elif a < b :
    print(f"{a} is smaller than {b}")
else :
    print(f"{a} is equal to {b}")


student_score = int(input("eneter your score: "))
if student_score > 100 or student_score < 0 :
    print("Invalid score") 
elif student_score >= 90 :
    print("A")
elif student_score >= 80 :
    print("B")
elif student_score >= 70 :
    print("C")
elif student_score >= 60 :
    print("D")
else :
    print("F")
    

month = input("Enter the month: ")

if month in ["September", "October", "November"]:
    print("The season is Autumn.")

elif month in ["December", "January", "February"]:
    print("The season is Winter.")

elif month in ["March", "April", "May"]:
    print("The season is Spring.")

elif month in ["June", "July", "August"]:
    print("The season is Summer.")

else:
    print("Invalid month")


fruits = ["banana", "orange", "mango", "lemon"]

new_fruit = input("Enter a fruit name: ")
if new_fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(new_fruit)
    print("Modified list:", fruits)



person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person and person['skills']:
    skills_list = person['skills']
    middle_index = len(skills_list) // 2
    print("Middle skill:", skills_list[middle_index])

if 'skills' in person:
    has_python = 'Python' in person['skills']
    print(f"Has Python skill: {has_python}")

if 'skills' in person:
    skills = person['skills']
     
    if len(skills) == 2 and 'JavaScript' in skills and 'React' in skills:
        print('He is a front end developer')
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print('He is a backend developer')
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print('He is a fullstack developer')
    else:
        print('unknown title')
else:
    print('unknown title')

if person.get('is_married') and person.get('country') == 'Finland':
    first = person['first_name']
    last = person['last_name']
    country = person['country']
    print(f"{first} {last} lives in {country}. He is married.")
