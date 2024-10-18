import numpy as np
from scipy.optimize import linear_sum_assignment


def min_match(dots):
    cache = {}

    def h(game):
        key = frozenset(game._boxes)
        value = cache.get(key)

        if value is not None:
            return value

        D = []
        for box_x, box_y in game._boxes:
            for dot_x, dot_y in dots:
                D.append(abs(box_x - dot_x) + abs(box_y - dot_y))

        D = np.asarray(D).reshape(-1, len(dots))
        i, j = linear_sum_assignment(D)
        cache[key] = value = D[i, j].sum()

        return value

    return h
