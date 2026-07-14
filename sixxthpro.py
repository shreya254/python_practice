list1 = [1,2,1]
copy_list = list1.copy()
copy_list.reverse()
if(list1 == copy_list):
    print("palindrome")
else:
    print("not palindrome")

grade =["A","C","D","A","E","A"]
print(grade.count("A"))
grade.sort()
print(grade)