#script to generate calendar of a month given the start-day and
#the number of days in that month
startday = input('Enter the start day of month(1-7): ')
numberofdays = input('Enter the number of days: ')
print ("Sun Mon Tues Wed Thurs Fri Sat ")
for i in range(startday-1):
       print(end = "    ")
       i = startday-1
       for j in range(1,numberofdays+1):
           if(i>6):
               print()
           i=1
           else:
               i = i +1
           print (str(i)+"  ", end = " ")
       
       
