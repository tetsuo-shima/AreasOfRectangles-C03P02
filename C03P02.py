# Areas of Rectangles

# The area of a rectangle is the rectangle’s length times its width. Write a
# program that asks for the length and width of two rectangles. The program
# should tell the user which rectangle has the greater area, or if the areas are
# the same.

import collections

Rectangle = collections.namedtuple("Rectangle", "length width area")
NUMBER_OF_RECTANGLES = 2


def main():
    rectangle_list = []

    for index in range(1, NUMBER_OF_RECTANGLES + 1):
        print("Enter dimensions for Rectangle", index)
        rectangle_list.append(build_rectangle())
        print()

    compare_rectangle_area(rectangle_list)


def build_rectangle():
    length = float(input("Enter rectangle length: "))
    width = float(input("Enter rectangle width: "))
    area = length * width  # tuples are immutable, so why not?
    return Rectangle(length, width, area)


def compare_rectangle_area(rectangle_list):
    if rectangle_list[0].area > rectangle_list[1].area:
        print("Rectangle 1 has a greater area.")
    elif rectangle_list[0].area < rectangle_list[1].area:
        print("Rectangle 2 has a greater area.")
    else:
        print("The rectangles have an equal area.")


if __name__ == '__main__':
    main()