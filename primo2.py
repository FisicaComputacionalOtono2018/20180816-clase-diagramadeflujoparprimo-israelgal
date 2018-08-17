import math
def isPrimeFor(num):
	flag=True
        raiz=int(round(math.sqrt(num),0))
	for i in range (2,raiz+1):
		if num%i==0:
			flag=False
			break
	return flag
num=input("<Numero: ")
if num==1:
	print("No es primo")
if num==2:
	print("Es Primo")
if num>2:
	if isPrimeFor(num):
		print("ES Primo")
	else:
		print("No Es Primo")

