import math
import sys


class Edge:
    def __init__(self, destination, weight):
        self.destination = destination
        self.weight = weight


def hash_func(x, numb_of_vertices):
    return x % numb_of_vertices


def convert(vertices, v_dict, num_of_vertices):
    for vertex in vertices:
        hashed = hash_func(vertex, num_of_vertices)
        while hashed in v_dict.values():
            hashed += 1
            hashed %= num_of_vertices
        v_dict[vertex] = hashed
    return v_dict


def get_vertex(num):
    for key, value in vertices_dictionary.items():
        if value == num:
            return key


def dfs(graph, num_of_vertices):
    visited = [False for _ in range(num_of_vertices)]
    stack = list()
    stack.append(0)

    while len(stack):
        e = stack[-1]
        stack.pop()
        if not visited[e]:
            print(get_vertex(e), end=' ')
            visited[e] = True

        for node in graph[e]:
            if not visited[node.destination]:
                stack.append(node.destination)
    print()


def print_graph_edges():
    for element in graph:
        for edge in element:
            print(edge.destination, edge.weight, end=' / ')
        print()


def find_min(distance, finalized):
    index = 0
    minimum = math.inf
    for i in range(number_of_vertices):
        if distance[i] < minimum and not finalized[i]:
            minimum = distance[i]
            index = i
    return index


def dijkstra(graph, source):
    distance = [math.inf for _ in range(number_of_vertices)]
    finalized = [False for _ in range(number_of_vertices)]
    distance[source] = 0
    for _ in range(number_of_vertices):
        index = find_min(distance, finalized)
        finalized[index] = True
        for node in graph[index]:
            if not finalized[node.destination]:
                distance[node.destination] = min(distance[node.destination], distance[index] + node.weight)
    print(distance)


number_of_vertices, number_of_edges = list(map(int, input().split()))
vertices_dictionary = dict()
graph = [[] for _ in range(number_of_vertices)]
participants = list()

vertices_id = list(map(int, input().split()))
vertices_dictionary = convert(vertices_id, vertices_dictionary, number_of_vertices)

for _ in range(number_of_edges):
    u, v, w = list(map(int, input().split()))
    u = vertices_dictionary[u]
    v = vertices_dictionary[v]
    e1 = Edge(v, w)
    graph[u].append(e1)
    e2 = Edge(u, w)
    graph[v].append(e2)


while True:
    command = input()
    if command == 'test':
        dfs(graph, number_of_vertices)

    elif command.startswith('join'):
        tokens = command.split(' ')
        node_number = int(tokens[1])
        node_number = vertices_dictionary[node_number]
        participants.append(node_number)
        print(participants)

    elif command.startswith('left'):
        tokens = command.split(' ')
        node_number = int(tokens[1])
        node_number = vertices_dictionary[node_number]
        participants.remove(node_number)
        print(participants)

    elif command == 'exit':
        sys.exit(1)
