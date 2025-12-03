with open("input.txt", encoding="utf-8") as f:
    ranges = f.read().strip().split(",")


def parse_input(input: str):
    parts = input.split("-")

    return int(parts[0]), int(parts[1])


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


if __name__ == "__main__":
    print(check_all(ranges))
