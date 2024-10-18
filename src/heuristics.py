import numpy as np
from scipy.optimize import linear_sum_assignment

# cost_matrix = np.array([[1, 5], [2, 8]])

# row_ind, col_ind = linear_sum_assignment(cost_matrix)

# for pair in zip(row_ind, col_ind):
#     print(pair)


def min_match(dots):
    def h(game):
        D = []
        for box_x, box_y in game._boxes:
            for dot_x, dot_y in dots:
                D.append(abs(box_x - dot_x) + abs(box_y - dot_y))

        D = np.asarray(D).reshape(-1, len(dots))
        i, j = linear_sum_assignment(D)
        return D[i, j].sum()

    return h
