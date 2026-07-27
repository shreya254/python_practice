list1 = ["a","b","c","d"]
list2 =["c","b","z","y"]
common =[]
for char in list1 :
    if char  in list2 :
        common.append(char)

print(common)
