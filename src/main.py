import sys

from game import Game
from search import bfs


def parse(g: str):
    you, dots, boxes, blocks = None, [], [], []
    col, row = 1, 1

    for c in g:
        if c == "\n":
            row += 1
            col = 0

        elif c == "d":
            dots.append((col, row))

        elif c == "y":
            you = (col, row)

        elif c == "Y":
            you = (col, row)
            dots.append((col, row))

        elif c == "b":
            boxes.append((col, row))

        elif c == "B":
            boxes.append((col, row))
            dots.append((col, row))

        elif c == "W":
            blocks.append((col, row))

        col += 1

    return Game(you, dots, boxes, blocks)


def print_solution(moves):
    mapping = {(0, -1): "up", (0, 1): "do", (-1, 0): "le", (1, 0): "ri"}
    for move in moves:
        print(mapping[move])


if __name__ == "__main__":
    lv = int(sys.argv[1])

    with open(f"./levels/level_{lv}.txt") as file:
        g = parse(file.read())

    solution = bfs(g)

    if solution is not None:
        print_solution(solution)

    else:
        print("no solution")
