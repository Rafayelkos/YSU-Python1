""""
#Problem 1
set1 = {1,2,3,4,5}
set2 = {5,2,10,5,8,9}

print(set1.intersection(set2))
print(set1.union(set2))

#Problem2
set3 = {1,2,3,4,5,6,7,8}
my_int = int(input("Enter any integer"))

print(min(set3)<my_int<max(set3))

#problem 3

dict1 = {
    "Rafayel":33,
    "Ruben":50,
    "Ani": 41}

my_key = input("Any string as new key")
my_value = input("Any Value ")

dict1['my_key'] = my_value
print(dict1)
#Problem4
t2 = ('Armenia', 'USA', 'Canada','Russia','Italy')
print(t2)

my_t2_list = list(t2)
my_t2_list[4]='hello'
print(tuple(my_t2_list))

#Problem 5
l1 = [(1,'a'),(2,'b'),(3,'c')]

d1 = dict(l1)
print(d1)


#Homework
#Problem1
d = {
    'name':'Armen',
    'age':15,
    'grades':[10, 8, 8, 4, 6, 7] }

if 'weigght' not in d:
    my_n = int(input('Enter any integer'))
    d['weight'] = my_n
    print(d)

#Problem2
market = {
    "dairy": ["yogurt", "cheese"],
    "Fruits":['banana','apple','orange','lemon','apple','banana','banana']}  
print('\n initial dict:',market)
market['candies'] = ['mars','kinder', 'twix']

print('\nAfter addin candies:', market)

my_set = set(market['Fruits'])
my_list = list(my_set)
my_list2 = sorted(my_list)

market['Fruits']= my_list2
print('\n last version:', market)
"""
#Problem3
t1 = (2,'cat', 'a', -2, "Anna")
t1_list = list(t1)
t1_list.remove('a')
t1 = tuple(t1_list)
print(t1)

t2 = (1,2,3,4,5)
t3 = t1[:3]+t2[:3]
print(t3)
print(t3[2])

t4 = [(1,3,5), (8,9),('Anna','Bob','Alice')]
print(t4[0][1])