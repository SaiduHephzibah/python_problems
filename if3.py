#script to check whether a given number is +ve, -ve or equal to 0
n = input('Enter a number: ')
if (n == 0):
    print(str(n)+ ' is zero')
elif (n>0):
    print(str(n)+ ' is +ve')
else:
    print(str(n)+ ' is -ve')
