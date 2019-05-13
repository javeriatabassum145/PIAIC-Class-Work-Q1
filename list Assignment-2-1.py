import random
#CREATING_RANDOM_LIST
random_list=[]
for i in range(100):
    random_list.append(random.randint(1,100))
print(random_list)
#MINIMUM_NUMBER
var1=random_list[0]
for i in random_list:
    if var1 > i:
        var1=i
print("Minimum number is : " , var1)
#MAXIMUM_NUMBER
var2=random_list[0]
for i in random_list:
    if var2 < i:
        var2 = i
print("Maximum number is : " , var2)
#INDEX
print("Index of minimum value in list is : " , random_list.index(var1))
print("Index of maximum value in list is : " , random_list.index(var2))
#MEAN_OF_VALUES
add=0
for i in random_list:
        add+=i
mean_of_randomlist=add/len(random_list)
print("Mean of values of list : " , mean_of_randomlist)

