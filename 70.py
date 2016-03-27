"""import math

def primeNumberCheck(n):
	if n==1: return True
	elif n<1: return False
	elif n%2==0: return False

	for i in range(3,int(math.sqrt(n))+1,2):
		if n%i==0:
			return False
	return True

def GetDivisitors(n):
	div = [1]
	if n < 1: return []
	elif n ==1: return div
	elif n ==2: return [1,2]	
	for i in range(2,n//2+1):
		if n%i == 0:
			div.append(i)
	return div


mas = []
for i in range (10**4):
	mas.append(GetDivisitors(i))
	
print (mas[10])

	
inp = int(input("Push The number"))
print(GetDivisitors(inp)) """
iterSize = 10**7
"""some text yet"""
div = []
for i in range(iterSize):
	div.append([1])

for i in range(2,iterSize):
	for j in range(2,iterSize // i +1 ):
		div[i*j-1].append(i)
		#print('i=%s, j = %s, div[%s] = %s' %(i,j,i*j-1,div[i*j-1]))

#print (div)
