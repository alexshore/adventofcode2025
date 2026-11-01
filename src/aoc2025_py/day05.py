from pathlib import Path
from typing import Any


class Range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __repr__(self) -> str:
        return f"Range({self.start}-{self.end})"

    def overlaps_range(self, other: Range) -> bool:
        """
        self    other   result
        -------------------------------
        4-6     7-9     no intersection
        4-6     5-7     other=4-7
        5-7     4-6     other=4-7
        4-9     6-7     other=4-9
        6-7     4-9     other=4-9
        """
        return (
            # they overlap in some way, e.g.:
            # self  = x------------x
            # other =        x---------x
            # or
            # self  =        x----------x
            # other = x------------x
            # or
            # self  = x-----------------x
            # other =        x-----x
            # or
            # self  =        x-----x
            # other = x-----------------x
            (other.start <= self.start <= other.end)
            or (other.start <= self.end <= other.end)
            or (self.start <= other.start and self.end >= other.end)
            # SIDENOTE: upon completion, I realised this whole thing could be replaced
            #           by just `self.start <= other.end and self.end >= other.start`
        )


def part_one(parsed_input: tuple[list[Range], list[int]]) -> int:
    result = 0

    ranges, ingredients = parsed_input

    for ingredient in ingredients:
        for range_ in ranges:
            if range_.start <= ingredient <= range_.end:
                result += 1
                break

    return result


def part_two(parsed_input: tuple[list[Range], Any]) -> int:
    ranges = parsed_input[0]
    exp_ranges: list[Range] = []

    # work out the overlaps

    # e.g.
    # ex_ranges = [1-3, 4-6, 7-9]
    # test_range = 5-8
    # ex_ranges = [1-3, 4-6, 7-9]
    # loop ex_ranges
    # ex_ranges[0] has no overlap, do nothing
    # ex_ranges[1] has an overlap, so we update test_range to 4-8 and remove ex_ranges[1]
    # ex_ranges = [1-3, 7-9]
    # ex_ranges[1] again has an overlap, so we update test_range to 4-9, and remove ex_ranges[1]
    # then add test_range on to the end of ex_ranges, and go to the next test_range

    # SIDENOTE: upon completion, I realised that sorting the ranges by start before starting
    #           would mean that you would only need to compare against the last element of the
    #           merged list and in that case either expand the last element, or just add the
    #           current range and it would handle it fine

    for r in ranges:
        i = 0
        while i < len(exp_ranges):
            if r.overlaps_range(e := exp_ranges[i]):
                r.start = min(e.start, r.start)
                r.end = max(e.end, r.end)

                exp_ranges.pop(i)
            else:
                i += 1
        exp_ranges.append(r)

    # calculate the fresh ingredients
    result = 0

    for range_ in exp_ranges:
        result += range_.end - range_.start + 1

    return result


def parse_input(txt: str) -> tuple[list[Range], list[int]]:
    sides = txt.split("\n\n", maxsplit=2)

    ranges = []
    for line in sides[0].splitlines():
        ranges.append(Range(*map(int, line.split("-"))))

    ingredients = []
    for line in sides[1].splitlines():
        ingredients.append(int(line))

    return (ranges, ingredients)


def main() -> None:
    txt = Path("inputs/day05.txt").read_text()

    parsed_input = parse_input(txt)

    print(part_one(parsed_input))
    print(part_two(parsed_input))


if __name__ == "__main__":
    main()
