import random


def generate_header():
    return """Joshua Palmer    Z: 23280034
STA 4821 001
200 coin flips
2 October 2015

"""


def get_face():
    return 'tails' if random.randint(0, 1) % 2 else 'heads'


def get_formatted_face(i):
    return "{}. {}\n".format(i, get_face())


def main():
    faces = [get_formatted_face(i) for i in range(1, 201)]
    with open("coinflips.txt", "w") as ofile:
        ofile.write(generate_header())
        ofile.writelines(faces)


if __name__ == '__main__':
    main()
