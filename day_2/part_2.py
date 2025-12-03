with open("input.txt", encoding="utf-8") as f:
    ranges = f.read().strip().split(",")


def parse_input(input: str):
    parts = input.split("-")

    return int(parts[0]), int(parts[1])


def check_validity(number_range: tuple):
    """
    Finds the sum of all 'invalid' numbers in a range.
    An invalid number is one formed by repeating a smaller number pattern
    two or more times (e.g., 1212, 777, 123123).
    """
    start, end = number_range
    invalid_numbers = set()

    # The maximum possible length of a number in the range
    max_num_len = len(str(end))

    # 1. Iterate through possible lengths of the base pattern
    # A pattern's length can't be more than half the max length
    for pattern_len in range(1, (max_num_len // 2) + 1):
        # 2. Iterate through all possible numbers for a given pattern length
        p_start = 10 ** (pattern_len - 1)
        p_end = 10**pattern_len
        for p in range(p_start, p_end):
            s_p = str(p)

            # 3. Repeat the pattern string to generate invalid numbers
            num_repeats = 2
            while True:
                s_num = s_p * num_repeats
                num_len = len(s_num)

                # Optimization: if we exceed the max length, this pattern
                # can't generate any more valid numbers.
                if num_len > max_num_len:
                    break

                num = int(s_num)

                # Optimization: if the number is already past the end of
                # the range, we can stop generating for this pattern.
                if num > end:
                    break

                # Check if the number is within the range and add it to the set
                if num >= start:
                    invalid_numbers.add(num)

                num_repeats += 1

    for n in sorted(list(invalid_numbers)):
        print(f"Invalid number: {n}")

    return sum(invalid_numbers)


def check_all(list_of_ranges: list):
    sum_of_invalid_ids = 0

    for range in list_of_ranges:
        parsed_range = parse_input(range)

        sum_of_invalid = check_validity(parsed_range)

        sum_of_invalid_ids += sum_of_invalid

    return sum_of_invalid_ids


if __name__ == "__main__":
    print(check_all(ranges))
