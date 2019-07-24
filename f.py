import math
from fractions import Fraction


def find_min(h,a,c,m):
    cnt=0
    x=a*m
    while 1:
    	if x>=h:
    		return c
    	x+=c
    	cnt+=1
    	if cnt>m:
    		return -1

def reduce(k1,k2):
	x = math.gcd(k1,k2)

	return k1//x,k2,x

def factorial(n):
	c=1;
	for i in range(2,n+1):
		c*=i
	return c

t = int(input())

for _ in range(t):

	a,h,l1,l2,m,c = map(int,input().split())

    
	v=[]

	mi = find_min(h,a,c,m)
	if mi==-1:
		print('RIP')
		continue
	if mi==0:
		print('1/1')
		continue

	fact = factorial(m)
	#print(fact,mi)
	for z in range(mi,m+1):

		k1 = fact * (l1**z) * ((l2-l1)**(m-z))
		k2 = factorial(z) * factorial(m-z) *(l2**m)
		#print(k1,k2)
		#x,y = reduce(k1,k2)
		#print(x,y)
		v.append([k1,k2])

	res=Fraction(0/1)

	for i in v:
		res += Fraction(i[0],i[1])

	print(res)







