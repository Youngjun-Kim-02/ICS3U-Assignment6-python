#!/usr/bin/env python3

# created by Youngjun Kim
# created on May 2021
# This program uses user defined functions

import math


def calculate_volume(radius, height):
    # this functions calculates volume of a cone

    # process
    volume = 1 / 3 * math.pi * radius * radius * height

    return volume


def main():
    # this function gets radius and height

    # input
    radius_value = int(input("Enter the radius of a cone: "))
    height_value = int(input("Enter the height of a cone: "))
    print("")

    # call functions
    calculated_volume = calculate_volume(radius_value, height_value)

    print("The volume is {0} cm³".format(calculated_volume))


if __name__ == "__main__":
    main()
