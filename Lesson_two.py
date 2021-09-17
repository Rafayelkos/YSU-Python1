import datetime
import calendar
import time

td = datetime.datetime.today()


#problem 1
x = datetime.datetime(2021,8,24)
y = datetime.datetime(2021,7,24)
k =x-y
print(k)
print(k.total_seconds())



#problem 2
Yesterday = td - datetime.timedelta(days=1)
today = td
further_one_day = td + datetime.timedelta(days=1)

print("Yesterday-", Yesterday)
print("Today - ", today)
print("Tomorro -" , further_one_day)

#problem 3
c = calendar.TextCalendar(calendar.MONDAY)
str = c.formatmonth(2021,1)
print(str)

Current_dat_time = datetime.date.today()

print(Current_dat_time.strftime("%B-%d-%y"))
print('\n' , datetime.datetime.now().year)
print('\n' , datetime.datetime.now().month)
print('\n', td.strftime('%A'))
print('\n', td-datetime.timedelta(days= 5))
print('\n', td+datetime.timedelta(seconds= 5))

# problem 4
birthday = datetime.datetime(1988,10,24,1,30,0)
print("\n My Birthday", birthday)
print("\n The year of my birthday is-", birthday.year)
print("\n The month of my birthday is-", birthday.strftime("%B"))
print("\n The month of my birthday is-", birthday.day)
print("\n The month of my birthday is-", birthday.strftime("%A"))
print(datetime.datetime(2021,10,24)-td)
print(calendar.TextCalendar(calendar.MONDAY).formatmonth(2017,5))
print(td-datetime.timedelta(1))