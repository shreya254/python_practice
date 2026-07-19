f= open("demo.txt","r")
data = f.read()
print(data)
f.close()

with open("demo.txt","w")as s:
    s.write("new data")