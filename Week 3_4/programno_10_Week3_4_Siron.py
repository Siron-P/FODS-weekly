'''Create three dictionaries: [7]
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
'''

#creating three dictionaries as in the question
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

#concatenating the dictionaries
nums = {**dic1,**dic2,**dic3} #creating nums variable
print("Concatenated Nums",nums) #printing concatenated dictionaries stored in num

#adding new key/value pair to the dictionary nums
nums[7]=55 #adding '7' key with value '55'
print("New key and value added dictionary: " ,nums) 

#updating value of the item with key 3 in nums to 80
nums[3]=80 #updating as question says
print("Updated value in dictionary :",nums) 

#removing third item from dictionary nums
del nums[3] #3rd item deleted
print("Removing third item from the dictionary",nums) 

#sum all the items in the dictionary nums
sums = sum(nums.values()) #all items added
print("Sum of all the items in dictionary items are",sums) 

#multiply all the items in the dictionary nums
answer = 1 #initializing answer varible as 1
for i in nums: #for loop to multiply every items
    answer = answer*nums[i]
print("The multiplication of all the items in dictionary nums is",answer) 

#retrieve the maximum and minimum values in nums
max_value = max(nums.values()) #finding maximum values
min_value = min(nums.values()) #finding minimum values
print("The maximum value is ",max_value)
print("The minimum value is ",min_value)
