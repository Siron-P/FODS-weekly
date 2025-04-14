'''Write a function called add_daily_temp that is given a (possibly empty)
dictionary meant to hold the average daily temperature for each day of the week,
a temperature value, and the day of the week for the recorded temperature. 
The function should then add the temperature to the dictionary only if 
it does not already contain a temperature for that day. The function 
should return the resulting dictionary, whether it is updated or not'''

#Creating function , giving 3 parameters -- temp_dict, temperature and day
def add_daily_temp(temp_dict, temperature, day):
    if day not in temp_dict: #if the day is not already in temp_dict
        temp_dict[day] = [temperature] 
    return temp_dict #return the updated temp_dict

dict={} 
n = int(input("Enter the number of inputs: "))
for i in range(n):  #prompt user
    day = input("Enter the day: ")
    temperature = int(input("Insert temperature: "))
    add_daily_temp(dict, temperature, day)
print(dict)
