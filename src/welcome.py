# Define a function that prints the instructions
def print_instructions():
    print("Welcome to the NYT Spelling Bee solver!")
    print("This script will generate an answer key for the daily spelling bee puzzle. All you have to do is enter the day's words!")
    print("You will be asked to enter the ring letters and center letter. The center letter is the yellow, highlited one.")
    print("All of the other letters in a ring around the center letter are ring letters.")
    print("Don't confuse ring letters with the center letter when prompted to input them.")
    

# Define a function that outputs the instructions based on whether or not the reader wants to see them
def get_instructions():
    global instructions_request
    while True:
        instructions_request = input("Would you like to read the instructions? Type y for yes and n for no: ")
        if instructions_request == 'y' or instructions_request == 'Y':
            print_instructions()
            print("Have fun!")
            break
        if instructions_request == 'n' or instructions_request == 'N':
            print("Have fun!")
            break