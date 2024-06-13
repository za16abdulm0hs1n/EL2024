import calendar

while True:
    year = int(input('Please enter the year: ' ))
    month = int(input('Please enter no. of the month (1-12): ' ))
    if 1 <= month <=12:
            break   

print(calendar.month(year, month))