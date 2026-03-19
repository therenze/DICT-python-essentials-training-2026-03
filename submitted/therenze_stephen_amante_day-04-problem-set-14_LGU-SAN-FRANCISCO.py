import datetime


month = int(input("Enter Month of Birth #: "))
day = int(input("Enter Day of Birth #: "))
year_short = int(input("Enter Year of Birth Last Two #: "))


special_date = {6, 7, 10, 17, 87, 24, 26}


today = datetime.date.today()
today_num = today.day


pin_date = special_date.copy()


pin_date.add(month)
pin_date.add(day)
pin_date.add(year_short)
pin_date.add(today_num)


print(f"Special Date #: {special_date}")
print(f"PIN Date: {pin_date}")