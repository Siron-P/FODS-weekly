#Write a function to check whether the given number is Armstrong or not

#taking input from the user
num = int(input("Enter a number: "))


sum = 0 #initializing sum

temp = num #storing num in temp variable
while temp > 0:
   digit = temp % 10 #Getting the last digit of input
   sum += digit ** 3 #calculating cube of last digit and added to sum
   temp //= 10 #removing the last digit

#displaying the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

