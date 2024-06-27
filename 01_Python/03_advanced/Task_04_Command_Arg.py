import sys

def get_arg():
    sys_arg = sys.argv
    return sys_arg
    

def print_arg(sys_arg):

    print(f"This is the name/path of the script: {sys_arg[0]}")
    print('Number of arguments:', len(sys_arg))
    print('Argument List:',end=' ')
    for arg in sys_arg:
        print(arg + ',',end=' ')
    print('')
        

sys_arg = get_arg()
print_arg(sys_arg)