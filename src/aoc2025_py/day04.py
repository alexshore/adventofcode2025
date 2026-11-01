from pathlib import Path


class Grid:
    def __init__(self, grid: list[str]):
        self.grid = grid
        self.width = len(grid[0])
        self.height = len(grid)

    def check_neighbours(self, cell: tuple[int, int]) -> int:
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if (
                    0 <= (test_x := cell[0] + i) < self.height
                    and 0 <= (test_y := cell[1] + j) < self.width
                    and self.grid[test_x][test_y] == "@"
                ):
                    count += 1
        return count

    def __repr__(self):
        return "\n".join(self.grid)


def part_one(papers: Grid) -> int:
    result = 0

    for i, line in enumerate(papers.grid):
        for j, cell in enumerate(line):
            if cell == "@" and papers.check_neighbours((i, j)) < 4:
                result += 1

    return result


def part_two(papers: Grid) -> int:
    result = 0

    while True:
        new_grid = papers.grid.copy()
        mid_sum = 0

        for i, line in enumerate(papers.grid):
            for j, cell in enumerate(line):
                if cell == "@" and papers.check_neighbours((i, j)) < 4:
                    new_grid[i] = new_grid[i][:j] + "." + new_grid[i][j + 1 :]
                    mid_sum += 1

        if mid_sum == 0:
            break

        result += mid_sum
        papers.grid = new_grid

    return result


def parse_input(txt: str) -> Grid:
    return Grid(txt.splitlines())


def main() -> None:
    txt = Path("inputs/day04.txt").read_text()

    parsed_input = parse_input(txt)

    print(part_one(parsed_input))
    print(part_two(parsed_input))


if __name__ == "__main__":
    main()
