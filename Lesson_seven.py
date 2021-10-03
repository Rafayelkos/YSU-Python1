""""
#Homework
#Problem1
d = {
    "name":"Armen",
    "age": 15,
    "grades":[10,8,8,4,6,7]
    }

sum_grades = sum(d["grades"])
if sum_grades/len(d["grades"])>7:
    print("Good Job")
else:
    print("You need to work")   

#Problem2
square_elem = [x**2 for x in range(1,51)]     
print(square_elem)    

#Problem3
list2 = ["a", "abc", "xyz", "s", "aba", "1221"]
counter = 0
for i in list2:
    
    if len(i) >= 2:
        counter+=1
    if  i[0] == i[-1]:
        print(i)
print(counter)    

#Problem4
lis1 = [1,3,5,7,9,11,13,15]
list2 = [4,6,14,11,8,16]

for i in lis1:
    if i in list2:
        print(f'number {i} -exist in list2')
        break

#Problem5
menu = [ "ice cream", "chocolate", "apple crisp", "cookies"]   

desert = input("Please input desert")
while True:
    if desert in menu:
        print("Your desert will arrive in 10 minutes")
        break
    else:
        desert = input ("Please input desert")    

#Practical
#Problem1
num = [7, 8, 120, 25, 44, 20, 27 ]
new_list = [x for x in num if x%2==0]

print(num)
print(new_list)

#Problem2
str1 = input("pleas insert any string you want")
l1 = [i for i in str1]
print(str1)
print(l1)

#Problem3
def avarage_func(x,y,z):
    mean = (x+y+z)/3
    return mean

print(avarage_func(5,8,5))

#Problem4

print('Password must contain at least 10 charachters, and must contain at least 2 digits')    
password = input("Please Enter your password")
def chek_pass(my_pass):

        if len(my_pass) < 10 or len([x for x in password if x.isdigit()])<2 :
            
            print("Your password is not correct")
            return False           
        
        return True 

print(chek_pass(password))  
"""
#Problem5
def my_func(name, *argv):
    if argv:
        result = 0
        for i in argv:
            result+=i

        av = result/len(list(argv))
        print(f"{name} Your avarage Grade is {av}")
        return f"{name} Your avarage Grade is {av}"
    else:    
        print(f'No Grades avalible for {name}')
        return f'No Grades avalible for {name}'
           

my_func("Armen",9,9,9)
