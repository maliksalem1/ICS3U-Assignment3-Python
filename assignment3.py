#!/usr/bin//env python3

# Created by: maliksalem1
# Created on: October 2022
# This program compares two numbers


def main():
    # This functions compares 2 numbers
    print("This program compares two numbers")
    print("")

    # Input
    integer_1 = float(input("Enter a number: "))
    integer_2 = float(input("Enter a second number: "))
    # Process
    if integer_1 == integer_2:
        print("These numbers are equal.")
    elif integer_1 > integer_2:
        print("{} is the larger of the two numbers".format(integer_1))
    elif integer_1 < integer_2:
        print("{} is the larger of the two numbers".format(integer_2))
    else:
        print("One or more inputs are invalid numbers")


if __name__ == "__main__":
    main()
