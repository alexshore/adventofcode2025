from pathlib import Path


def part_one(banks: list[list[int]]):
    result = 0

    for bank in banks:
        first = max(bank[:-1])
        first_idx = bank.index(first)
        second = max(bank[first_idx + 1 :])
        result += first * 10 + second

    return result


def part_two(banks: list[list[int]]):
    result = 0

    for bank in banks:
        joltage = 0

        for i in range(11, 0, -1):
            next_largest = max(bank[:-i])
            next_index = bank.index(next_largest)
            bank = bank[next_index + 1 :]
            joltage *= 10
            joltage += next_largest

        joltage *= 10
        joltage += max(bank)

        result += joltage

    return result


def parse_input(txt: str) -> list[list[int]]:
    return [[int(num) for num in line] for line in txt.splitlines()]


def main() -> None:
    txt = Path("inputs/day03.txt").read_text()

    parsed_input = parse_input(txt)

    print(part_one(parsed_input))
    print(part_two(parsed_input))


if __name__ == "__main__":
    main()
