def get_char():
    char = input('Please Enter a Charater: ')
    while len(char) !=1:
        print("Please enter exactly one character.")
        char = input('Please Enter a Charater: ') 
    return(char)

#------------------------------------------------------------

def find_ascii_vaule(char):
    ascii_value = ord(char)
    return ascii_value

#---------------------------------------------------------

another_choice ='1'
user_choice = input("Welcome to ASCII Vaule Finder \nEnter '1' to continue or '0' to exit: ")


while user_choice not in ['1', '0']:
    print("Invalid input. Please enter '1' to continue or '0' to exit!")
    user_choice = input("Welcome ASCII Vaule Finder \nEnter '1' to continue or '0' to exit: ")

if user_choice == '1':
    print("Continuing with the ASCII Value Finder...")
    
    while another_choice is '1':
        char = get_char()
        ascii_value = find_ascii_vaule(char)

        print(f"The ASCII Vaule for the Character {char} is {ascii_value}. Thank you for your patience.")
        another_choice = input(f"Do you want to find anoter ASCII value?\nEnter '1' to yes or '0' to no:")

        while another_choice not in ['1', '0']:
            print("Invalid input. Please enter '1' to yes or '0' to no!")
            another_choice = another_choice = input(f"Do you want to find anoter ASCII value?\nEnter '1' to yes or '0' to no:")

    print("Exiting. Goodbye!")           
else:
    print("Exiting. Goodbye!")