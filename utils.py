import os
import csv
from printer import Printer


class Utils:
    @staticmethod
    def read_data_file(path):
        if os.path.exists(path):
            km_list = []
            prices = []
            rows_counter = 1
            try:
                with open(path, 'r') as f:
                    rows = [row for row in csv.DictReader(f)]
                    for column_name in ['km', 'price']:
                        if column_name not in rows[0]:
                            Printer.print_error_exit(f"no column {column_name} in file {path}")
                    for row in rows:
                        rows_counter += 1
                        km_list.append(int(row['km']))
                        prices.append(int(row['price']))
                return km_list, prices
            except IOError:
                Printer.print_error_exit(f"can't open file {path}")
            except ValueError:
                Printer.print_error_exit(f"invalid values in file {path}")
            except TypeError:
                Printer.print_error_exit(f"Not enough data in file {path} at row {rows_counter}")

        else:
            Printer.print_error_exit('invalid path to data file')