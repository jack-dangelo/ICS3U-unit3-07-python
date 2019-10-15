#!/usr/bin/env python3

# Created by: Jack D'Angelo
# Created on: October 2019
# This program tells you if you can date my grandchild


def main():
    while True:
        try:
            age = int(input("Please enter your age: "))

            if age >= 25 and age <= 40:
                print()
                print("You can date my grandchild")

            else:
                print()
                print("You cannot date my grandchild")

        except ValueError:
            print()
            print("Invalid age")
            print()
            continue

        else:
            break


if __name__ == "__main__":
    main()
