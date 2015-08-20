"""
Joshua Palmer   Z23280034
STA   4821      MWF 1:00 - 1:50
Homework 1      August 24, 2015
"""

import random
from string import Template

def output_string(j):
   ##  return "{0:>5}    {1:>2}    {2:.4f}\n"
   # else:
    return "{0:>6}    {1:>2}    {2:.4f}\n"

def header():
    return """Joshua Palmer    Z23280034
STA   4821       MWF 1:00 - 1:50
Homework 1       August 24, 2015

exp_num num_asked     avg
-------   ---    --------
"""

def main():
    with open('hw1_output.txt', "w") as outfile:
        outfile.write(header())

        m = 0
        for j in range(1, 100001):
            n = 1
            while random.random() > n / 365:
                n += 1
            m += n
            if j in (1, 2, 3, 4, 5, 10, 25, 50, 100, 1000, 10000, 100000):
                output = output_string(j).format(j, n, m/j)
                print(output.rstrip())
                outfile.write(output)

if __name__ == '__main__':
    main()
