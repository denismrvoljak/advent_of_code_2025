input = [line for line in open("input.txt").read().split("\n") if line.strip()]


def rotate(start: int, code: str):
    direction = code[0]
    amount = int(code[1:])
    count = 0

    for i in range(1, amount + 1):
        if direction == "L":
            start = (start - 1) % 100
        elif direction == "R":
            start = (start + 1) % 100
        else:
            raise ValueError(f"Invalid input: {code}")

        if start == 0:
            count += 1

    return start, count


def move_dial(input: list, dial_value: int):
    total_count = 0

    for code in input:
        dial_value, count = rotate(start=dial_value, code=code)
        total_count += count

    return total_count


print(move_dial(input, 50))
