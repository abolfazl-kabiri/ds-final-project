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
    return distance


def min_avg(avgs):
    indices = list()
    whole_min = math.inf
    for i in range(len(avgs)):
        if avgs[i] == whole_min:
            indices.append(i)
        elif avgs[i] < whole_min:
            indices.clear()
            indices.append(i)
            whole_min = avgs[i]
    return indices, whole_min


def find_location():
    par_dij = list()
    avg_dis = list()
    for node in participants:
        if node in dijkstra_dictionary.keys():
            par_dij.append(dijkstra_dictionary[node])
        else:
            new_dij = dijkstra(graph, node)
            dijkstra_dictionary[node] = new_dij
            par_dij.append(new_dij)

    for i in range(number_of_vertices):
        if i in participants:
            avg_dis.append(math.inf)
            continue
        sum = 0
        n1, n2 = 0, 1
        while n1 < n2 and n1 < len(participants):
            n2 = n1 + 1
            while n2 < len(participants):
                sum += math.fabs(par_dij[n1][i] - par_dij[n2][i])
                n2 += 1
            n1 += 1
        avg_dis.append(sum / len(participants))
    fair_vertices, whole_min = min_avg(avg_dis)

    for vertex in fair_vertices:
        print(get_vertex(vertex), end=" ")
    print()


number_of_vertices, number_of_edges = list(map(int, input().split()))
vertices_dictionary = dict()
graph = [[] for _ in range(number_of_vertices)]
participants = list()

vertices_id = list(map(int, input().split()))
vertices_dictionary = convert(vertices_id, vertices_dictionary, number_of_vertices)

dijkstra_dictionary = dict()

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
        if len(participants) > 1:
            find_location()

    elif command.startswith('left'):
        tokens = command.split(' ')
        node_number = int(tokens[1])
        node_number = vertices_dictionary[node_number]
        participants.remove(node_number)
        if len(participants) > 1:
            find_location()

    elif command == 'exit':
        sys.exit(1)
