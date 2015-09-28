"""
Joshua Palmer   Z23280034
STA   4821      MWF 1:00 - 1:50
Homework 1      August 24, 2015
"""

import random


def output_string(j):
    return "{0:>6}    {1:>2}    {2:.4f}\n"


def header():
    return """Joshua Palmer    Z23280034
STA   4821       MWF 1:00 - 1:50
Homework 1       August 24, 2015
"""


def table_header():
    return """  j       n     avg
  -----   --    -------
"""


def output(j, n, avg):
    if j in (1, 2, 3, 4, 5, 10, 25, 50, 100, 1000, 10000):
        return output_string(j).format(j, n, avg)
    return None


def main():
    output_strings = []

    print(table_header().rstrip())

    m = 0
    for j in range(1, 10001):
        n = 1
        while random.random() > n / 365:
            n += 1
        m += n
        out = output(j, n, m/j)
        if out:
            output_strings.append(out)
            print(out.rstrip())

    user_input = None
    while user_input not in ('y', 'n'):
        user_input = input("\nSave to file? (y/n): ")
        if user_input.lower().rstrip() == 'y':
            with open('hw1_output.txt', "w") as ofile:
                ofile.writelines(output_strings)
            print("Done writing. Goodbye.")
        elif user_input.lower().rstrip() == 'n':
            print("Goodbye.")
        else:
            print("Please enter 'y' or 'n'")

if __name__ == '__main__':
    main()
