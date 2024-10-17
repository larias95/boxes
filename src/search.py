from collections import deque


class Node:
    def __init__(self, game, move, parent):
        self.game = game
        self.move = move
        self.parent = parent


def _build_solution(node):
    moves = []

    while node.parent is not None:
        moves.append(node.move)
        node = node.parent

    moves.reverse()
    return moves


def bfs(game):
    discovered = {game}
    pending = deque([Node(game, None, None)])

    while len(pending) > 0:
        node = pending.popleft()

        for move in node.game.get_moves():
            clone = node.game.clone()
            clone.play(move)

            if clone in discovered:
                continue

            discovered.add(clone)

            if not clone.valid_state:
                continue

            new_node = Node(clone, move, node)

            if clone.victory:
                return _build_solution(new_node)

            pending.append(new_node)

    return None
