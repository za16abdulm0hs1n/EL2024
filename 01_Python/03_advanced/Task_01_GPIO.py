
def choose_port():

    valid_ports = ['A', 'B', 'C', 'D']

    port = input("Please select a port name from the following options ['A', 'B', 'C', 'D']: ").upper()

    while port not in valid_ports:
        print(f"Invalid port name '{port}'. Please choose a valid port name from ['A', 'B', 'C', 'D'].")
        port = input("Please select a port name from the following options ['A', 'B', 'C', 'D']: ").upper()

    return port

#----------------------------------------------------------

def choose_bits_mode():

    valid_modes = ['IN', 'OUT']
    bits_mode = []
    for bit in range(8):
        bit_mode = input(f"Please select a mode for bit {bit} from the following options ['IN', 'OUT']: ").upper()
        while bit_mode not in valid_modes:
            print(f"Invalid mode '{bit_mode}'. Please choose a valid mode from ['IN', 'OUT'].")
            bit_mode = input(f"Please select a mode for bit {bit} from the following options ['IN', 'OUT']: ").upper()
        if bit_mode == 'IN':
            bits_mode.append(0)
        elif bit_mode == 'OUT':
            bits_mode.append(1)

    return bits_mode

#----------------------------------------------------------------

def generate_gpio_init_c_code(port ,bits_mode):

    ddrx = ''.join(str(bit)for bit in bits_mode)
    ddrx = f"ob{ddrx}"

    code = f"""
    // Initialization function for GPIO Port {port}
    void GPIO_Init(void) {{
        // Set data direction register for Port {port}
        DDR{port} = {ddrx};
        //Initialize port values (all set to low)
        PORT{port} = 0x00;
    }}
    """
    return code

#------------------------------------------------------------------------

def save_code(code, port):
    file_name = f"AVR_int_gpio_port_{port.lower}"
    file_path = './' + file_name
    with open(file_path, 'w') as file:
        file.write(code)

#------------------------------------------------------------------------------


user_choice = input("Welcome to AVR's GPIO Initializer Code Generator for C!\nEnter '1' to continue or '0' to exit: ")

while user_choice not in ['1', '0']:
    print("Invalid input. Please enter '1' to continue or '0' to exit.")
    user_choice = input("Welcome to AVR's GPIO Initializer Code Generator for C!\nEnter '1' to continue or '0' to exit: ")
   
if user_choice == '1':
    print("Continuing with the GPIO initializer...")
    port = choose_port()
    bits_mode = choose_bits_mode()
    code = generate_gpio_init_c_code(port,bits_mode)
    save_code(code, port)
    print(f"Code generation for Port {port} is complete. Thank you for your patience. Goodbye!")
   
else:
    print("Exiting. Goodbye!")

