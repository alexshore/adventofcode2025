import re
from pathlib import Path

PART_ONE_REGEX = r"^(\d+)\1$"
PART_TWO_REGEX = r"^(\d+)\1+$"


class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"{self.start=}, {self.end=}"


def part_one(ranges: list[Range]):
    result = 0

    for range_ in ranges:
        for i in range(range_.start, range_.end + 1):
            if re.search(PART_ONE_REGEX, str(i)):
                result += i

    print(result)


def part_two(ranges: list[Range]):
    result = 0

    for range_ in ranges:
        for i in range(range_.start, range_.end + 1):
            if re.search(PART_TWO_REGEX, str(i)):
                result += i

    print(result)


def parse_input(txt: str) -> list[Range]:
    ranges = []

    for range_ in txt.rstrip().split(","):
        ranges.append(Range(*map(int, range_.split("-", maxsplit=2))))

    return ranges


def main() -> None:
    txt = Path("inputs/day02.txt").read_text()
    ranges = parse_input(txt)

    part_one(ranges)
    part_two(ranges)


if __name__ == "__main__":
    main()
