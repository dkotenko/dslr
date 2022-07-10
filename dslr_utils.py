import sys
import pandas as pd

def print_exit(s):
    print(s)
    sys.exit(0)
        
def print_error(s):
    print("Error: ", end='')
    print_exit(s)

def load_csv():
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        print_exit('Usage: ./describe \'filepath\'')
    try:
        df = pd.read_csv(filepath, delimiter=',', index_col=0)
    except FileNotFoundError:
        print_error("Invalid filepath")
    except PermissionError as e:
        print_error("Permission denied")
    except pd.errors.EmptyDataError as e:
        print_error("File is empty")
    except Exception:
        raise RuntimeError("Unknown error, read stacktrace")
    return df


