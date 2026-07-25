data = input("enter the word : ")
reverse =""
for char in data :
    reverse = char+reverse
print(reverse)
if(data == reverse):
    print("it is palindrome")
else:
    print("not a palindrome")