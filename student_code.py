import math

class PossiblePaths(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return not self.queue

    def insert(self, data):
        self.queue.append(data)

    def delete(self):
        try:
            mini = 0
            for i in range(len(self.queue)):
                if (self.queue[i][-1] + self.queue[i][-2]) < (self.queue[mini][-1] + self.queue[mini][-2]):
                    mini = i
            item = self.queue[mini]
            del self.queue[mini]
            return item
        except IndexError:
            print()


def shortest_path(M, start, goal):
    global intersection_dict, roads, possible_paths, heuristic_values, next_cost

    if start == goal:
        return [start]

    heuristic_values = {}
    next_cost = []
    intersection_dict = M.intersections
    roads = M.roads

    for node in intersection_dict:
        heuristic_values[node] = math.sqrt((intersection_dict[node][0] - intersection_dict[goal][0]) ** 2 + abs(
            intersection_dict[node][1] - intersection_dict[goal][1]) ** 2)

    for i in range(len(roads)):
        plan_queue = []
        for path in roads[i]:
            plan_queue.append(math.sqrt((intersection_dict[i][0] - intersection_dict[path][0]) ** 2 + abs(
                intersection_dict[i][1] - intersection_dict[path][1]) ** 2))
        next_cost.append(plan_queue)

    possible_paths = PossiblePaths()
    possible_paths.insert([[start], 0, heuristic_values[start]])
    return helper_path(goal)


def helper_path(goal):
    global intersection_dict, roads, possible_paths, heuristic_values, next_cost

    if possible_paths.isEmpty():
        return "No possible path"
    else:
        item = possible_paths.delete()

    current = item[0][-1]
    if current == goal:
        return item[0]

    for i, front in enumerate(roads[current]):
        if front in item[0]:
            continue
        g = next_cost[current][i] + item[-2]
        h = heuristic_values[front]
        possible_paths.insert([item[0] + [front], g, h])

    return helper_path(goal)