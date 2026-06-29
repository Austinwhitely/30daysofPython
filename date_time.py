from datetime import datetime, date

today = datetime.now()
print(today)

formatted_today = today.strftime('%m/%d/%Y, %H:%M:%S')
print(formatted_today)

past = date(2020,12,5)
print(past)

today = datetime(year = 2026, month = 6, day = 28, hour = 10, minute = 21, second = 0)
newyears = datetime(year = 2027, month = 1, day = 1, hour = 0, minute = 0, second = 0)

difference = newyears -today 
print (difference)