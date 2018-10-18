r=int(input("enter the radius of the circle:\n"));
if(r<0):
	print("negative radius is not allowed");
elif(r==0):
	print("circle with zero radius does not exist");
else:
	area=3.14*r*r;
	print("area of the circle is"+str(area));
