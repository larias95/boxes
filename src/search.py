from collections import deque
from heapq import heappop, heappush


class Node:
    def __init__(self, game, move, parent):
        self.game = game
        self.move = move
        self.parent = parent


class NodeWithCost(Node):
    def __init__(self, game, move, parent, f, h):
        super().__init__(game, move, parent)
        self.f = f
        self.h = h
        self._cost = f + h

    def __lt__(self, other):
        return self._cost < other._cost


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

            new_node = Node(clone, move, node)

            if clone.victory:
                return _build_solution(new_node)

            pending.append(new_node)

    return None


def astar(game, heur):
    discovered = {game}
    pending = [NodeWithCost(game, None, None, 0, 0)]

    while len(pending) > 0:
        node = heappop(pending)

        for move in node.game.get_moves():
            clone = node.game.clone()
            clone.play(move)

            if clone in discovered:
                continue

            discovered.add(clone)

            new_node = NodeWithCost(clone, move, node, node.f + 1, heur(clone))

            if clone.victory:
                return _build_solution(new_node)

            heappush(pending, new_node)

    return None
