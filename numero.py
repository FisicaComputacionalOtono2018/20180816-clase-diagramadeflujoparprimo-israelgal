#Author: Jose Israel Galindo Rodriguez 
#Nombre:programa para exentar 
#Fecha:
N=input("Un numero")
S=12
A=2
P=1
while S!=0:
	if N%2==0:
  	   N=N+1
	   while A < N:
     	         R=N%A
      	         if R==0:
         	    P=0
      	A=A+1
	if P==1:
   	   if  N < 5:
       	       S=S-N
	S=S-1
print N   

     		
