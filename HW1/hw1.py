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
        "Homework 1       August 24, 2015\n"
    return h


def table_header():
    header = "      j    n        avg\n" \
             "  -----   --    -------\n"
    return header


def menu(saved=False):
    menu = "[q]uit  [r]erun"
    if not saved:
        menu += " [s]ave to file"
    menu += "\n:> "
    return menu


def output_string(j):
    return "{0:>6}    {1:>2}    {2:>7.3f}\n"


def output(j, n, avg):
    if j in (1, 2, 3, 4, 5, 10, 25, 50, 100, 1000, 10000):
        out = output_string(j).format(j, n, avg)
        return out
    return None


def show_menu(output_strings, saved=False):
    user_input = None
    menu_choices = ('q', 'r') if saved else ('q', 'r', 's')
    while user_input not in menu_choices:
        user_input = input(menu(saved)).lower()
        if user_input.lower().rstrip() == 's' and not saved:
            with open('hw1_output.txt', "w") as ofile:
                ofile.write("{}\n{}".format(header(), table_header()))
                ofile.writelines(output_strings)
            print("Done writing.")
        elif user_input.lower().rstrip() == 'r':
            pass
        elif user_input.lower() == 'q':
            print("Goodbye.")
        else:
            choices = ', '.join(menu_choices[:-1])
            choices = "{}, or {}".format(choices, menu_choices[-1])
            print("Please enter {}".format(choices))
    return user_input


def simulate():
    print(table_header().rstrip())
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
            user_input = show_menu(output_strings, saved=True)


if __name__ == '__main__':
    main()
