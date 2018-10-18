#Script to print the calendar of any given year
import calendar
y=int(input("Enter the year: "))
print ("\n*******CALENDAR*******")
cal = calendar.TextCalendar(calendar.SUNDAY)
i=1
while i<=6:
    cal.prmonth(y,i)
    i+=1
