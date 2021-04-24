#Dijkstra's algorithm using a dictionary and priority queue

#Given a graph and a source vertex in the graph, find shortest paths
# from source to all vertices in the given graph.

#Input: The start position is: 0 . The end position is: 5
#Output : The shortest route from the start to end is:  ['0', '7', '6', '5']

import heapq
class HeapEntry:
    def __init__(self, node, priority):
        self.node = node
        self.priority = priority
    def __lt__(self, other):
        return self.priority < other.priority

class Graph:
    def __init__(self):
        self.nodes = {}
    def add_node(self, key, neighbours):
        self.nodes[key] = neighbours
    def traceback_path(self, target, parents):
        path = []
        while target:
            path.append(target)
            target = parents[target]
        return list(reversed(path))

    def shortest_path(self, start, finish):
        OPEN = [HeapEntry(start, 0.0)]
        CLOSED = set()
        parents = {start: None}
        distance = {start: 0.0}
        while OPEN:
            current = heapq.heappop(OPEN).node
            if current is finish:
                return self.traceback_path(finish, parents)
            if current in CLOSED:
                continue
            CLOSED.add(current)

            for child in self.nodes[current].keys():
                if child in CLOSED:
                    continue
                tentative_cost = distance[current] + self.nodes[current][child]
                if child not in distance.keys() or distance[child] > tentative_cost:
                    distance[child] = tentative_cost
                    parents[child] = current
                    heap_entry = HeapEntry(child, tentative_cost)
                    heapq.heappush(OPEN, heap_entry)

g = Graph()
g.add_node('0', {'1': 4, '7': 8})
g.add_node('1', {'2': 8, '0': 4})
g.add_node('2', {'1': 8, '3': 7, '5': 4})
g.add_node('3', {'2': 7, '4': 9, '5': 14})
g.add_node('4', {'3': 9, '5': 10})
g.add_node('5', {'2': 4, '3': 14, '4': 10, '6': 2})
g.add_node('6', {'5': 2, '7': 1})
g.add_node('7', {'6': 1, '0': 8, '8': 7})
g.add_node('8', {'7': 7})
print("The start position is: 0")
print("The end position is: 5")
print("The shortest route from the start to end is: ",g.shortest_path('0', '5'))