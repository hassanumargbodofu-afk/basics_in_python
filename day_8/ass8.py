# Exercises: Day 8

dog = {}
dog ['name']= 'faruq'
dog['colour']= 'brown'
dog ['breed']= 'german shepherd'
dog ['age']= 200

student = {
    'first_name': "umar",
    'last_name': "hassan",
    "gender": "male",
    'age': 25,
    'marital_status': "single",
    'skills': "Python",
    'country': "Nigeria",
    'city': "Ilorin" ,
    'address': 'GbaGba phase 2, opposite royal valley estate'
}
print(len(student))

student_skill = list(student['skills'])      
print(student_skill)
print(type(student_skill))

student['skills'] = ['skills','graphic design', 'media buyer'] 
print(student)

student_key = list(student.keys())
print(student_key)

student_list = list(student.values())
print(student_list)

students= (student.items())
print(students)

del student['age']

del student
