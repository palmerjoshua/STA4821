"""
Simulates 200 coin flips, and
prints the results to a file.
"""
import random


def get_header():
    return """Joshua Palmer    Z: 23280034
STA 4821 001
200 coin flips
2 October 2015

"""


def get_face():
    return 'X' if random.randint(0, 1) % 2 else 'O'


def get_flip_line():
    return " ".join(get_face() for i in range(20)) + "\n"


def get_faces():
    return ["{:2}. ".format(i+1) + get_flip_line() for i in range(10)]


def main():
    faces = get_faces()
    with open("coinflips.txt", "w") as ofile:
        ofile.write(get_header())
        ofile.writelines(faces)


if __name__ == '__main__':
    main()
