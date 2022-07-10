import csv
import sys
import pandas as pd
from dslr_utils import print_error, print_exit
from dslr_math import *
import numpy as np

default_padding = 12
float_fmt = '>12.4f'
int_fmt = '>12.0'
delim = ' | '

    

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
    df_orig = df.copy()
    df = df.select_dtypes('number')
    
    df = df.apply(pd.to_numeric)
    #df = df.append(a_series, ignore_index=True)
    
    #df_buf = df_out.copy()
    #max_columns_len = []
    
    d = {'Index': ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']}
    df_buf = pd.DataFrame(d).set_index('Index')
    df_buf.index.name = None
    
    for column in df:
        df_buf[column] = [count_(df[column]), mean_(df[column]), std_(df[column]), min_(df[column]), percentile_(df[column], 25), percentile_(df[column], 50), percentile_(df[column], 75), max_(df[column])]
    print(df_buf)
    print('\n' + '#' * 100)
    print('\npandas.describe() to compare:\n')
    print(df_orig.describe())

if __name__ == '__main__':
    describe()
