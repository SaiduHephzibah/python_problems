#script to find the factorial of a given number
n=input('Enter a number: ')
fact=1
for i in range(2,n+1):
    fact=fact * i
print (str(n) + '! = ' +str(fact))
