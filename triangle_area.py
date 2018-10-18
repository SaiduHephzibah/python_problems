#Script to find the area of a triangle for the given THREE sides
a=float(input('Enter the 1st dise of the triangle: '))
b=float(input('Enter the 2nd dise of the triangle: '))
c=float(input('Enter the 3rd dise of the triangle: '))
s= (a+b+c)/2
area = (s * (s-a)*(s-b) * (s-c))**0.5
print('The sides of the triangle are: ',a,b,c)
print ('Area is: ',round(area,2))
