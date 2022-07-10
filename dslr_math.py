import math
import numpy as np


def count_(X):
    return sum([1 for x in X if not math.isnan(x)])

def mean_(X):
    total = 0
    for x in X:
        if np.isnan(x):
            continue
        total = total + x
    return total / len(X)

def std_(X):
    mean = mean_(X)
    total = 0
    for x in X:
        if np.isnan(x):
            continue
        total = total + (x - mean) ** 2
    return (total / len(X)) ** 0.5

def min_(X):
    min_value = X[0]
    for x in X:
        val = x
        if val < min_value:
            min_value = val
    return min_value

def max_(X):
    min_value = X[0]
    for x in X:
        val = x
        if val > min_value:
            min_value = val
    return min_value

def percentile_(X, p):
    X.sort_values()
    k = (len(X) - 1) * (p / 100)
    f = np.floor(k)
    c = np.ceil(k)

    if f == c:
        return X[int(k)]

    d0 = X[int(f)] * (c - k)
    d1 = X[int(c)] * (k - f)
    return d0 + d1

'''
column is 'NaN column' if it has more than 50% of NaN values 
'''
def isnan_column(column):
    return sum([1 for cell in column if math.isnan(cell)]) > len(column) / 2  
