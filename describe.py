import csv
import sys
import pandas as pd
from dslr_utils import print_error, print_exit
from dslr_math import *

fmt = ':>12.4f'

'''
column is 'NaN column' if it has more than 50% of NaN values 
'''

    

def describe():
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

    df_out = df.select_dtypes('number')
    for col in df_out:
        if isnan_column(df_out[col]):
            df_out.drop(col, axis=1, inplace=True)
    df_out = df_out.apply(pd.to_numeric)
    
    print(f'{"":15} |{"Count":>12} |{"Mean":>12} |{"Std":>12} |{"Min":>12} |{"25%":>12} |{"50%":>12} |{"75%":>12} |{"Max":>12}')
    for col in df_out:
        column = df_out[col]
        for calculated in [count_(column), mean_(column), std_(column), min_(column),
                           percentile_(column, 25), percentile_(column, 50),
                           percentile_(column, 75), max_(column)]:
            print(f'{calculated}{format}'.format(values=calculated, format=fmt), end=' |')

    
    
    print("pandas.describe() output")
    print(df_out.describe())


if __name__ == '__main__':
    describe()
