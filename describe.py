import csv
import sys
import pandas as pd
from dslr_utils import print_error, print_exit, load_csv
from dslr_math import *
import numpy as np

default_padding = 12
float_fmt = '>12.4f'
int_fmt = '>12.0'
delim = ' | '

    

def describe():
    df = load_csv()
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
