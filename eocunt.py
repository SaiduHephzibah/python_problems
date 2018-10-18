lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
zcount=count=0;
print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
  
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
			   count+=1;
			   break
       else:
           print(num)
		   zcount+=1;