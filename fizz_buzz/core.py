"""Core."""


def convert_number(number: int) -> str:
    """Convert number to FizzBuzz notation."""

    if number == 0:
        return f"{number}"

    if number % 3 != 0 and number % 5 != 0:
        return f"{number}"

    result = ""
    if number % 3 == 0:
        result = f"{result}Fizz"
    if number % 5 == 0:
        result = f"{result}Buzz"
    return f"{result}!"
