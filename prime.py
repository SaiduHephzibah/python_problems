pcount=ccount=0;
zcount=0;
while(True):
	c=0;
	num = int(input("Enter number: "))
	if(num==-1):
		break;
	if num >=1:
		for i in range(2,num):
				if (num % i) == 0:
					c+=1;
					if(c>0):
						ccount+=1;
				else:
					pcount+=1;
	else:
		print("prime numbers cannot be negative");
print("prime numbers are:" +str(pcount));
print("composite numbers are:" +str(ccount));
