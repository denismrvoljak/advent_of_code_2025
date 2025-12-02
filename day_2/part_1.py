import csv
import re

with open("input.txt", newline="", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=",")
    rows = [row for row in reader if any(field.strip() for field in row)]

print(rows[0][0])  # each row is a list of strings, quotes handled correctly


PATTERN = re.compile(r"^\s*([+-]?\d+)\s*-\s*([+-]?\d+)\s*$")


def parse_input(input: str):
    match = PATTERN.match(input)

    if not match:
        raise ValueError("Invalid Input")

    return int(match.group(1)), int(match.group(2))


print(parse_input("300-240"))


def check_validity(set: tuple):
    a, b = set

    sum_of_invalid = 0

    for i in range(a, b + 1):
        num_of_digits = len(str(i))
        num_of_digits_halved = int(num_of_digits / 2)

        if num_of_digits % 2 > 0:
            continue  # skip odd

        first_half = int(str(i)[:num_of_digits_halved])

        second_half = int(str(i)[num_of_digits_halved:])

        if first_half == second_half:
            print(f"Invalid number: {i}")

            sum_of_invalid += i

    return sum_of_invalid


def check_all(list_of_ranges: list):
    sum_of_invalid_ids = 0

    for range in list_of_ranges:
        parsed_range = parse_input(range)

        sum_of_invalid = check_validity(parsed_range)

        sum_of_invalid_ids += sum_of_invalid

    return sum_of_invalid_ids


result = check_validity((1188511880, 1188511890))

print(result)

print(check_all(rows[0]))
