input = [line for line in open("input.txt").read().split("\n") if line.strip()]


def rotate(start: int, code: str):
    direction = code[0]
    amount = int(code[1:])

    if direction == "L":
        return (start - amount) % 100
    if direction == "R":
        return (start + amount) % 100
    else:
        raise ValueError(f"Invalid input: {code}")


def move_dial(input: list, num: int):
    count = 0

    for code in input:
        num = rotate(start=num, code=code)
        if num == 0:
            count += 1

    return count


print(move_dial(input, 50))
