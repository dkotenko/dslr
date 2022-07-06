import csv
import os

def describe(name):
    with open('eggs.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        ...
        print(', '.join(row))


if __name__ == '__main__':
    describe('PyCharm')
