#!/usr/bin/env python3

"""Entry point."""

import sys
import prompt

import argparse

from fizz_buzz.core import convert_number


def parse_args():
    """Parse input parameters."""

    parser = argparse.ArgumentParser(
        prog="fizz_buzz",
        description="Console utility to convert number to FizzBuzz notation")
    parser.parse_args()


def make_iter() -> None:
    """Iteration to read and convert number."""

    try:
        number = prompt.integer("Number: ")
        result = convert_number(number)
        print(result)
    except KeyboardInterrupt:
        sys.exit(0)


def main() -> None:
    """Main function"""

    parse_args()
    print("Welcome to Fizz Buzz!\nSubmit a number and get an answer!")
    while True:
        make_iter()


if __name__ == "__main__":
    main()
