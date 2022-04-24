import calendar

print(calendar.weekheader(3))
print()

print(calendar.firstweekday())

print(calendar.month(2022,3,))

print(calendar.monthcalendar(2022,3))

print(calendar.calendar(2022))

day_of_the_week =calendar.weekday(3000,3,8)
 
is_leap = calendar.isleap(2022)
print(is_leap)

how_many_leap_days = calendar.leapdays(2021,2022)
print(how_many_leap_days)




