a=10
b=200
c=30
d=40

if(a>b and a>c):
    if(a>d):
        print(a)
    else:
        print(d)
elif(b>c and b>d):
    print(b)
else:
    print(d)