#script to determine the largest of given three numbers
a = int(input('Enter the 1st number: '))
b = int(input('Enter the 2nd number: '))
c = int(input('Enter the 3rd number: '))
if(a>b):
    if(a>b):
        print(a, 'is greater than',b,'and', c)
    else:
        print(c, 'is greater than',a,'and', b)
elif b>c:
    print(b, 'is greater than',a,'and', c)
else:
    print(c, 'is greater than',a,'and', b)
