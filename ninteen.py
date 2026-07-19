def show(num):
    if num<=0 :
        return
    print(num)
    show(num-1)
show(5)

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
       return n * fact(n-1)
    
print((fact(7)))