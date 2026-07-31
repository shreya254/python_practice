from collections import Counter
data = input("enter a word")
char_count = Counter(data)
print(char_count)

for char in data:
    if char in char_count :
        char_count[char] +=1
else:
    char_count[char]= 1

print(char_count)