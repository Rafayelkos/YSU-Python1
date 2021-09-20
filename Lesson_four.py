
"""
# Practical

#Problem1
list1=['hello', 1, True]
print(dir(list1))
elem =input('Enter severel items').split()
print(list1+elem)
#Problem2
list2 = ['Rafayel', '9', 'Rafayel', 9]

elem2 = input('Enter item for checking')
print(f']Number of {elem2} is -',list2.count(elem2))


#problem3
l1 = [1,2,'Yes', 'No']
l2 = [4,6,7,22]
print(l1)
print(l2)
l1.pop(-1)
l1.append(l2)
print(l1)

#Problem 4

set1 ={1,2,9,5,8,48}
set2 = {2,48,5}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1 & set2)
print(set1 | set2)

# Problem 5

set3 = {1,3,45,7,87,96,5,4}

elem = int(input("Enter any int"))

answyer = (elem>min(set3)) & (elem<max(set3))

print(answyer)

#Homework
#Problem 1
list1=['hello', 1, True]

elem =input('Enter severel items').split()
list2 = list1.copy().__add__(elem)

print(list1)
print(list2)

#Problem2
list2 = [2,4,45, 5, 39]
print(list2)

x = input('Enter value')

list2.remove(x)

print(list2)

#Problem3

list3 = [1,3,'e','r','t',75,5,7,9]    
print(list3)
list3.pop(0)
del list3[4:6]
print(list3)

#Problem4
list4 = [1,3,'e','r','t',75,5,7,9]

l4 =list4.copy()
l4.pop(0)
del l4[4:6]
print(l4)
"""
#Problem 5
my_list = [1,4,5,7,8,-2,0,-1]
print(my_list[4])
print(my_list[6])
a_sorted = my_list.copy()

a_sorted.sort(reverse=True)

print(a_sorted)

print(a_sorted[0:3])
print(a_sorted[2:6])

del a_sorted[2]
del a_sorted[3]

print(a_sorted)

b = ['grapes', 'Potatoes', 'tomatoes', 'Orange', 'Lemon', 'Brocoli', 'Carrot', 'Sausages']

b_sorted = b.copy()
b_sorted.sort()
print(b_sorted)

c= my_list[0:3]+b[4:7]
print(c)






