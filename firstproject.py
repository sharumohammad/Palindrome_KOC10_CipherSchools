a=int(input())
b=str(a)
e=len(b)
c=b[::-1]
d=True
for i in range(e):
    if(b[i] != c[i]):
        d=False
        break
isprime=True
for i in range(2,a):
    if(a%i==0):
        isprime=True
if(d==True and isprime==True):
    print("It is a Prime palindrome")
else:
    print("It is not a Prime palindrome")