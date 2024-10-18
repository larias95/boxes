import copy


def _displace(pos, dir):
    x, y = pos
    dx, dy = dir
    return x + dx, y + dy


class Game:
    _moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def __init__(self, you, dots, boxes, blocks):
        self._you = you
        self._dots = dots[:]
        self._boxes = set(boxes)
        self._blocks = set(blocks)

    def clone(self):
        return copy.deepcopy(self)

    def get_moves(self):
        return Game._moves

    def play(self, move):
        if self._try_move_you(self._you, move):
            self.victory = all((dot in self._boxes) for dot in self._dots)

    def _try_move_you(self, pos, dir):
        new_pos = _displace(pos, dir)

        if (new_pos not in self._blocks) and ((new_pos not in self._boxes) or self._try_move_box(new_pos, dir)):
            self._you = new_pos
            return True

        return False

    def _try_move_box(self, pos, dir):
        new_pos = _displace(pos, dir)

        if (new_pos not in self._boxes) and (new_pos not in self._blocks):
            self._boxes.remove(pos)
            self._boxes.add(new_pos)
            return True

        return False

    def __hash__(self):
        return sum(self._you) + sum(sum(box) for box in self._boxes)

    def __eq__(self, other):
        return self._you == other._you and self._boxes == other._boxes
