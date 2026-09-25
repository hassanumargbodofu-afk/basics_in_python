#Exercise 1.1
age = 57
height = 22.3
z = 3 + 5j

base = int(input("Enter base: "))
height = int(input("enter height: "))
area_of_triangle =(0.5 *base * height)
print("The area of the triangle is ==", area_of_triangle)

side_a = int(input("enter side a :"))
side_b = int(input("enter side b :"))
side_c = int(input("enter side c :"))
parameter = side_a + side_b + side_c
print("The perimeter of the triangle is ==", parameter)

length = int(input("Enter length: "))
width = int(input("Enter width: "))
area_of_rectangle = length * width
print("The area of the rectangle is ==", area_of_rectangle)

length = int(input("Enter length: "))
width = int(input("Enter width: "))
perimeter_of_rectangle = 2 * (length + width)
print("The perimeter of the rectangle is ==", perimeter_of_rectangle)

radius_of_circle = int(input("Enter radius of the circle: "))
area_of_circle = 3.14 * radius_of_circle ** 2
print("The area of the circle is ==", area_of_circle)

radius_of_circle = int(input("Enter radius of the circle: "))
circumference_of_circle = 2 * 3.14 * radius_of_circle
print("The circumference of the circle is ==", circumference_of_circle)

slope = 2
x_intercept = 1
y_intercept = -2
print("slope:", slope)
print("x-intercept:", x_intercept)
print("y-intercept:", y_intercept)

slope = 0
x_1 = 2
x_2 = 6
y_1 = 2
y_2 = 10

slope = (y_2 - y_1) / (x_2 - x_1)

print("slope:", slope)

# Euclidean distance between point (2, 2) and point (6,10)

x_1 = 2
x_2 = 6
y_1 = 2
y_2 = 10

euclidean_distance = (x_2 - x_1)**2 +(y_2 -y_1) **0.5
print("Euclidean distance:", euclidean_distance)

# comparation of the slopes
slope_1 = 2
slope_2 = 2
print(slope_1 == slope_2)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0
x = 2
y = x**2 + 6*x + 9 
print("y:", y)

x = 1
y = x**2 + 6*x + 9 
print("y:", y)

x = 0
y = x**2 + 6*x + 9 
print("y:", y)

x = -1
y = x**2 + 6*x + 9 
print("y:", y)

x = -3
y = x**2 + 6*x + 9 
print("y:", y)

value_1 = 'python' 
value_2 = 'dragon'
print(len(value_1) != len(value_2)) or print(len(value_1) > len(value_2))

value_1 = "python" 
value_2 = "dragon"
print("on" in value_1 and "on" in value_2)

sentence = "I hope this course is not full of jargon"
print("jargon" in sentence)

value_1 = "python" 
value_2 = "dragon"
print("on" not in value_1 and "on" not in value_2)

length = "python"
print(float(len(length)))
print(str(len(length))) 

evennumber = 10
print(evennumber % 2 == 0)

floor_division = 7 // 3
print(floor_division)
print(2 == int(2.7))

type = "10"
print((type) == 10)

integer = "9.8"
print((integer) == 10)

hours = int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))
payment = hours * rate
print("Your weekly earning is:", payment)

number_years = int(input("Enter number of years you have lived: "))
number_of_seconds = 60 * 60 * 24 * 365 * number_years
print("You have lived for", number_of_seconds, "seconds.") 

for i in range(1, 6):
    print(f"{i} {i**0} {i**1} {i**2} {i**3}")
