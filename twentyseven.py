#reverse string
str = input("enter a word")
reverse_txt = ""
for char in str:
    reverse_txt= char+reverse_txt
print(reverse_txt)