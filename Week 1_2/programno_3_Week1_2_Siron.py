#Write a program that will convert Celsius value to Fahrenheit.

#taking celsius value from user
print("Enter a celsius value to convert into fahrenheit: \n")
celsius = int(input("Celsius value =  ")) #storing user input in variable 'celsius'

#Program to convert Celsius value to Fahrenheit.
fahrenheit = (9/5)*celsius+32

#Displaying the fahrenheit value
print(f"\n {celsius}°C is equal to {fahrenheit:.2f}°F")