'''fruits=["apple","banana","mango"]
for i in fruits:
    print(i)'''
# creating an empty list
lst = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
    #ele = str(input())  #for typing alphabets
    # adding the element
    lst.append(ele)  
 
print(lst)
