import math

class Space(object):
    def __init__(self, start):
        self.opened_set = {start}
        self.closed_set = set()

    def visit_node(self, node):
        self.opened_set.remove(node)
        self.closed_set.add(node)

    def is_visited(self, node):
        return node in self.closed_set

    def has_to_explore(self):
        return len(self.opened_set) != 0

    def explore(self, node):
        self.opened_set.add(node)

    def is_explored(self, node):
        return node in self.opened_set

    def minimized_node(self, f_score):
        mini_node = None
        mini_score = float('inf')

        for node in self.opened_set:
            current_score = f_score[node]
            if current_score < mini_score:
                mini_score = current_score
                mini_node = node

        return mini_node


def shortest_path(M, start, goal):
    if start == goal:
        return [start]

    nodes = M.intersections
    roads = M.roads

    nodes_count = len(nodes)
    came_from = {}
    g_score = [float('inf')] * nodes_count
    f_score = [float('inf')] * nodes_count

    g_score[start] = 0.0
    f_score[start] = euclidean_distance(nodes[start], nodes[goal])
    space = Space(start)

    while space.has_to_explore():
        current_node = space.minimized_node(f_score)

        if current_node == goal:
            return reconstruct_path(came_from, current_node)

        space.visit_node(current_node)
        nearby_nodes = roads[current_node]

        for nearby_node in nearby_nodes:
            if space.is_visited(nearby_node):
                continue

            if not space.is_explored(nearby_node):
                space.explore(nearby_node)

            updated_g_score = g_score[current_node] + euclidean_distance(nodes[current_node], nodes[nearby_node])

            if updated_g_score >= g_score[nearby_node]:
                continue

            came_from[nearby_node] = current_node
            g_score[nearby_node] = updated_g_score
            f_score[nearby_node] = g_score[nearby_node] + euclidean_distance(nodes[nearby_node], nodes[goal])

    return None


def euclidean_distance(x, y):
    return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)


def reconstruct_path(came_from, current_node):
    path = [current_node]

    while current_node in came_from.keys():
        current_node = came_from[current_node]
        path.append(current_node)

    return path[::-1] # reversed path
