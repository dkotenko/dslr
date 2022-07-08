import csv
import sys
import pandas as pd
import numpy as np


def describe():
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        print('Provide filepath as ./describe \'filepath\' or as argument to function describe(\'filepath\')')
        sys.exit(0)

    df = pd.read_csv(filepath,
                     delimiter=',',
                     index_col=0)

    only_num = df.select_dtypes('number')
    print(df.select_dtypes('number'))
    print(list(only_num.columns))
    exit(0)

    with open(filepath, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            for cell in row:
                if not cell.isnumeric():
                    break
            print(', '.join(row))


if __name__ == '__main__':
    describe()
