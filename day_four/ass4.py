# exercise 4
string = 'thirty'+ ' ' + 'days' + ' ' + 'of' + ' ' + 'python'
print(string)

coding = 'coding ' + ' ' + 'for' + ' ' + 'all'
print(coding)

company = "Coding For All"

print(company)

length ="company"
print(len(length))

print(company.upper())

print(company.lower())

print(company.capitalize())

print(company.title())

print(company.swapcase())

print(company[7:14])

print(company.find("Coding"))

print(company.replace("Coding", "Python"))

python = "Python for Everyone"
print(python.replace("Python for Everyone", "Python for All"))

coding = 'Coding For All'
print(coding.split())

social = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(social.split(','))

print(coding[0])

print(coding[10])

print(len(coding)-1)

python = 'Coding For All'
abbrev = python[0] + python[7] + python[11]
print(abbrev)

print(coding.index('C'))
print(coding.index('F'))

print(coding.rfind('l'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

sentences = 'You cannot end a sentence with because because because is a conjunction'
print(sentences.rindex('because'))

sentencess = 'You cannot end a sentence with because because because is a conjunction'
print(sentencess[30:55])

print(coding.startswith('Coding'))
print(coding.endswith('Coding'))

codin = '   Coding For All      ' 
print(codin.strip())

print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# " .join(libraries))

print("I am enjoying this challenge.\nI just wonder what is next.")
print(f"Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

radius = 10
area = 3.14 * radius ** 2

print(f"The area of a circle with radius {radius} is {area:.0f} meters square.")

x = 8
y = 6

print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")