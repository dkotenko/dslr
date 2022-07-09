import sys

def print_exit(s):
    print(s)
    sys.exit(0)
        
def print_error(s):
    print("Error: ", end='')
    print_exit(s)


