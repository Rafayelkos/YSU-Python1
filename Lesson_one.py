"""""
#problem 2
course = " Intro to python"
student = "Rafayel Kosyan"
nickname = "Superman"
grade = 4
pythonExpert = True

print("course:" , course)
print("student:", student)
print("nickname:", nickname)
print("grade:", grade)
print("pythonExpert:", True)

print("=================================================")
#problem 3

AB = 3
AC = 4
BC = (AB**2 + AC**2)**(1/2)

print("The hypotenuse of the triangle ABC = ", BC)

#problem 4
text, start_index, end_index = input("Enter text, start_index, end_index using space").split()
print(text[int(start_index):int(end_index)])

# problem 5
# a
str1 = "How are you Jhon"
name = "Rafayel"
str2 = f'How are you {name}'
print(str2)

# b
str1 = "How are you Jhon"
name = "Rafayel"
str2 = f'{str1[:-4]} {name}'
print(str2)

#Homework
#Problem 1
project = "cake"
dificulty = 7
ingridents = ["flour", "butter", "sugar", "eggs", "coca powder", "baking powder"]

if "apple" in ingridents:
    print("Yes", "Apple is in Ingridents")
else:
    print("No")    

if "butter" in ingridents:
    print("Yes", "butter is in Ingridents")
else:
    print("NO")   




if "eggs" or "margarine" in ingridents:
    print("Yes")
else:
    print("NO")     


if "eggs" and "margarine" in ingridents:
    print("Yes")
else:
    print("NO")    


flour, butter, suger, eggs, cocoa_powder, baking_powder = 175, 175, 100, 2, 1, 0.5

print("flour type is-", type(flour))
print("butter type is-", type(butter))
print("suger type is-", type(suger))
print("eggs type is-", type(eggs))
print("cocoa_powder type is-", type(cocoa_powder))
print("bakin_powder type is-", type(baking_powder))

#Problem 2
a = 15
b = 8
c = 2
output_1 = 5*a**2 - a*b + (a%2) - a/5
print(output_1)

output_2 = b**3 + 3*a*b - 10*c
print(output_2)

#Problem 3

text  = input("Enter text")
first_word = input("Enter first word to change")
second_word =input("Enter second word to change")

if first_word in text:
    new_text = text.replace(first_word,second_word)
print(new_text)
"""
#Problem 4
text  = input("Enter text").lower()


if "usa" in text:
    new_text = text.replace("usa", "Armenia").upper()
print(new_text)

