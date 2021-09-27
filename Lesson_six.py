"""
#Practical
#Problem1
name ="Senior Rafayel"
age = 33
password = 203040

if "Rafayel" in name:
    print(f"\nWelcome Mr.{'Rafayel'}")
if age < 16:
    print(f"\nDear {name} you are too young")
if age > 16:
    print(f'\nDo not worry {name} you have a long life')
if '*' or '&' not in password:
    print("\nPlease enter a different password")

#Problem2
counter = 1
for ind, i in enumerate(range(1,100)):
    
    if i % 2 != 0:
        print(f'{counter} - {i}')    
    counter +=1    

#Problem3
for j in range(1,20):
    if j%15 == 0:
        break 
    print(j)       

"""
#Problem 4
num = [7,8, 120, 25, 44, 20,27]

new_list = [x for x in num if x % 2 == 0]

print(num)
print(new_list)

#Problem 5
str1 = input('Enter any string')

my_list_str=[i for i in str1]
print(my_list_str)




