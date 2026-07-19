n=5
def sum(n):
    if n>0:

        total = 0
        total = total+n
        sum(n-1)
    else:
        return total


print(sum(n))