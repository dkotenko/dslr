import csv
import sys
import pandas as pd

err = "Error: "
fmt = ':>12.4f'

def describe():
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        print('Usage: ./describe \'filepath\'')
        sys.exit(0)
    df = None
  
    try:
        df = pd.read_csv(filepath, delimiter=',', index_col=0)
    except FileNotFoundError:
        sys.exit(err + "Invalid filepath")
    except PermissionError as e:
        sys.exit(err + "Permission denied")
    except pd.errors.EmptyDataError as e:
        sys.exit(err + "File is empty")
    except Exception:
        raise RuntimeError("Unknown error, read stacktrace")

    header = 1
    print(
        f'{"":15} |{"Count":>12} |{"Mean":>12} |{"Std":>12} |{"Min":>12} |{"25%":>12} |{"50%":>12} |{"75%":>12} |{"Max":>12}')
    sys.exit(0)
    only_num = df.select_dtypes('number')
    print(only_num)
    print(list(only_num.columns))
    exit(0)

    for x in [count_(data), mean_(data), std_(data), ]
    print(f'{values}{format}'.format(values=, format=fmt), end=' |')
    print(f'{values}{format}'.format(values=, format=fmt), end=' |')
    print(f'{values}{format}'.format(values=, format=fmt), end=' |')

    print(f'{mean_(data):>12.4f}', end=' |')
    print(f'{std_(data):>12.4f}', end=' |')
    print(f'{min_(data):>12.4f}', end=' |')
    print(f'{percentile_(data, 25):>12.4f}', end=' |')
    print(f'{percentile_(data, 50):>12.4f}', end=' |')
    print(f'{percentile_(data, 75):>12.4f}', end=' |')
    print(f'{max_(data):>12.4f}')

    


if __name__ == '__main__':
    describe()
