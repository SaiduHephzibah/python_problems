#script to check whether a given number is prime or not 
n=input('Enter a number: ')
prime=1
for i in range(2,n):
    if (n%i == 0):
        print (str(n)+ ' is not a prime')
        prime=0
        break 
if(prime!=0):
    print (str(n)+ ' is a prime')
