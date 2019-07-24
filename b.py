def roman(num):
        val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        syb = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

place="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def place_value(c):
    return place.index(c)

def get(s,x):
    
    n=len(s)
    l,c = n,0

    for i in range(n):
        l-=1
        c += place_value(s[i])*x**l

    #print(c,x)
    #print()
    
    return c


def findleast(s):
    n=len(s)
    mi,x=10000000000,-1

    for i in s:
        x=max(x,place.index(i))
    
    mi=get(s,x+1)
    
    return mi



n=int(input())
while(n>0 and n<4000):
    
    s=roman(n)
    #print(s)
    n=findleast(s)
    #print(n)

print(n)

