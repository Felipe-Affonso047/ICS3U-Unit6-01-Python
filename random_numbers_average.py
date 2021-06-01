#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: June 2021
# This program generate random numbers and shows their average

import random


def main():
    # This program generate random numbers and shows their average
    number_of_random_numbers = 10
    numbers = []
    average = 0

    print("{} random numbers:".format(number_of_random_numbers))

    for random_numbers in range(0, number_of_random_numbers):
        temp = random.randint(1, 100)
        numbers.append(temp)
        print("{}".format(numbers[random_numbers]))
        average = average + numbers[random_numbers]

    average = average / number_of_random_numbers

    print("\nAverage: {}".format(average))

    print("\nDone.")


if __name__ == "__main__":
    main()
