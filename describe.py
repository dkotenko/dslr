import csv
import sys
import pandas as pd
from dslr_utils import print_error, print_exit
from dslr_math import *
import numpy as np

default_padding = 12
fmt = '>12.4f'
decorized_delim = ' | '


    

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
    [print_padding_header(x) for x in df_out]
    print()
    
    df_out = df_out.apply(pd.to_numeric)
    for col in df_out:
        if isnan_column(df_out[col]):
            df_out.drop(col, axis=1, inplace=True)
            continue
    #print(max_columns_len)
    
    
        max_columns_len = []
        max_column_len = df_out[col].astype(str).str.len().max()
        max_columns_len.append(max_column_len)
    
    
    
    
    
    
    
    
    
    
    #
    
    #print(f'{"":15} |{"Count":>12} |{"Mean":>12} |{"Std":>12} |{"Min":>12} |{"25%":>12} |{"50%":>12} |{"75%":>12} |{"Max":>12}')
    #[print(x) for x in df_out]
    for index, col_str in enumerate(df_out):
        column = df_out[col_str].apply(pd.to_numeric)
        for calculated in [count_(column), mean_(column), std_(column), min_(column),
                           percentile_(column, 25), percentile_(column, 50),
                           percentile_(column, 75), max_(column)]:
            if column.dtype == np.int64:
                to_print = str(calculated)
            else:
                to_print = f'{calculated:.6f}'
            padding = max_columns_len[index] - len(str(to_print))
            print(f'{to_print:>{padding}} | ', end= '')
        print()
    
    
    print("pandas.describe() output")
    print(df_out.describe())


def print_padding_header(header):
    max_len = max(len(header), default_padding)
    padding = 0 if max_len != default_padding else default_padding - len(header)
    print(f'{header:>{padding}} | ', end= '')

def print_padding_row(s, padding):
    max_len = max(len(header), default_padding)
    padding = max_len - len(str(s))
    
    
if __name__ == '__main__':
    describe()
