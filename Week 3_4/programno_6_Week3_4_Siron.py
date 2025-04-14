
'''Write a program that prompts the user for a series of integers and
 stores in a list only the values between 1-100, and displays the resulting list'''

def integer():
    numbers = []  # List to store valid numbers
    while True:
        # Prompt the user for input
        user_input = input("Enter a number between 1-100 or type 'exit' to finish: ")
        
        # Check if the user wants to exit
        if user_input.lower() == "exit":
            break

        try:
            # Convert the input to an integer
            inputs = int(user_input)

            # Check if the number is within the valid range
            if 1 <= inputs <= 100:
                numbers.append(inputs)  # Add valid number to the list
            else:
                print("The number does not lie between 1 and 100. Please try again.")

        except ValueError:
            # Handle invalid input (not an integer)
            print("Invalid input. Please enter a valid integer.")

    return numbers

def main():
    display_result = integer()  # Get the list of valid numbers
    print("The resulting list is:", display_result)

# Run the main function
main()

