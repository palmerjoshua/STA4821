"""
Joshua Palmer   Z23280034
STA   4821      MWF 1:00 - 1:50
Homework 1      August 24, 2015

Note: Simulation function on line 66.
      Main function on line 82.
"""

import random


def header():
    h = "Joshua Palmer    Z23280034\n" \
        "STA   4821       MWF 1:00 - 1:50\n" \
        "Homework 1       August 24, 2015"
    return h


def table_header():
    header = "      j    n        avg\n" \
             "  -----   --    -------"
    return header


def menu(saved=False):
    menu = "[q]uit  [r]erun"
    if not saved:
        menu += " [s]ave to file"
    menu += "\n:> "
    return menu


def output(j, n, avg):
    if j in (1, 2, 3, 4, 5, 10, 25, 50, 100, 1000, 10000):
        out = "{0:>6}    {1:>2}    {2:>7.3f}\n".format(j, n, avg)
        return out
    return None

# todo remove 'TEST' from file name
def save_to_file(output_strings):
    with open('hw1_outputTEST.txt', "w") as out_file:
        out_file.write("{}\n{}\n".format(header(), table_header()))
        out_file.writelines(output_strings)


def show_menu(output_strings=None, saved=False):
    user_input = None
    menu_choices = ('q', 'r') if saved else ('q', 'r', 's')
    while user_input not in menu_choices:
        user_input = input(menu(saved)).lower().rstrip()
        if user_input == 'q':
            print("Goodbye.")
        elif user_input == 'r':
            pass
        elif user_input == 's' and not saved:
            save_to_file(output_strings)
            print("Saved to hw1_output.txt")
        else:
            choices = ', '.join(menu_choices[:-1])
            choices = "{}, or {}".format(choices, menu_choices[-1])
            print("Please enter {}".format(choices))
    return user_input


def simulate():
    print(table_header())
    output_strings = []
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
    return output_strings


def main():
    user_input = None
    while user_input != 'q':
        output_strings = simulate()
        user_input = show_menu(output_strings)
        if user_input == 's':
            user_input = show_menu(saved=True)


if __name__ == '__main__':
    main()
