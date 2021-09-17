
import sys
import argparse
import datetime

print(type(sys.argv))
print('Script name:', sys.argv[0])

print('Arguments:', sys.argv[1:])

parser = argparse.ArgumentParser()
parser.add_argument('--square', help ="display a square of agiven number", type=int, default=10)
args = parser.parse_args()
if args.square:
  print(args.square**2)


# Practical
#Problem 1
import sys
print(type(sys.argv))
print('Script name:', sys.argv[0])
print('Number of Arguments',len(sys.argv[0]))
print('Arguments list', str(sys.argv))
print('Arguments Value ', sys.argv[1])
print('Arguments Value ', sys.argv[2])

#problem 2

user_nam = input ("Enter your text please")
print(f'Wlecome f{user_nam}')

#Problem 3
parser = argparse.ArgumentParser()

parser.add_argument('name', help="Enter your name",type=str)

args = parser.parse_args()
print("Welcome ", args.name)


#Problem 4

parser = argparse.ArgumentParser()

parser.add_argument('--age', help= "Enter your age", type=int)

args = parser.parse_args()

print("Happy Bithday ", args.age)

#Problem 5

parser = argparse.ArgumentParser()

parser.add_argument('text', help= "Enter your any text", type=str)

args = parser.parse_args()
lower_text = args.text.lower()
uper_text = args.text.upper()
capitalize_text = args.text.capitalize()

print(lower_text)
print(uper_text)
print(capitalize_text)

#Homework
#Problem 1

parser = argparse.ArgumentParser()

parser.add_argument('--num_y', help= "Enter your any year", type=int)
parser.add_argument('--num_d', help= "Enter your any day", type=int)
args = parser.parse_args()

first_arg = args.num_y
second_arg = args.num_d




if first_arg and second_arg:
  print(datetime.datetime.today()-datetime.timedelta(days = first_arg*365 + second_arg))
else:
  print(datetime.datetime.today()) 

#Problem 2

parser = argparse.ArgumentParser()

parser.add_argument('text', help= "Enter your any year", type=str)


args = parser.parse_args() 
text_1 = args.text
mid_tree = text_1[(len(text_1)-2)//2:(len(text_1)+3)//2]
print(mid_tree)
mid_tree_uper = text_1[:(len(text_1)-2)//2]+mid_tree.upper()+text_1[(len(text_1)+3)//2:]
print(mid_tree_uper)

parser = argparse.ArgumentParser()

parser.add_argument('text', help= "Enter your any year", type=str)
parser.add_argument('first_word', help= "Enter your any year", type=str)
parser.add_argument('second_word', help= "Enter your any year", type=str)

args = parser.parse_args()
if args.first_word in args.text:
    new_text = args.text.replace(args.first_word,args.second_word)
print(new_text)