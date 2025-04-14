'''Create two sets: [5]
set1 = {20, 40, 60}
set2 = {10, 20, 30, 40, 50, 60}
'''

#Creating 2 sets
set1 = {20,40,60}
set2 = {10,20,30,40,50,60}
print("set1: ",set1)
print("set2: ",set2)
#displaying set 1 and 2

#Union of these sets
set_union = set1|set2 #using "|" for union of sets
print("The union of set1 and set 2 is",set_union) #displaying set 3 as union of sets

#intersection of set1 and set2
set_intersect = set1 & set2 #Using "&" for intersection
print("The intersection of set1 and set2 is ",set_intersect)

#compute the symmetric difference between set1 and set2
set_sym_diff = set1^set2 #using "^" for symmetric difference
print("The symmetric difference between set 1 and set 2 are ",set_sym_diff)

#add the value 40 to set1
set1.add(40) #adding
print("The value 40 is added so that, set1 : ",set1)
print("No, the set didn't change!!")

#remove value 20 from set2
set2.remove(20) #removing
print("After removing the value 20 from set 2 : ",set2)
