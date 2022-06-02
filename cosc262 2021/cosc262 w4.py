def adjacency_list(graph_str):
    result = []
    for line in graph_str.splitlines():
        result.append(line.split())
        
    adj_list = [[] for i in range(int(result[0][1]))]
    if graph_str[0] == "D":
        i = 1
        while i < len(result):
            index = int(result[i][0])
            vertex = int(result[i][1])
            if len(result[i]) <= 2:
                weight = None
            else:
                weight = int(result[i][2])
            adj_tuple = (vertex, weight)
            adj_list[index].append(adj_tuple)
            i+=1
    elif graph_str[0] == "U":
        i = 1
        while i < len(result):
            index = int(result[i][0])
            vertex = int(result[i][1])
            if len(result[i]) <= 2:
                weight = None
            else:
                weight = int(result[i][2])
            adj_list[index].append((vertex, weight))
            adj_list[vertex].append((index, weight))
            i += 1
    return adj_list

def transpose(adj_list):
    transpose_adj_list = [[] for i in range(0, len(adj_list))]
    for i in range(0, len(adj_list)):
        for j in range(0, len(adj_list[i])):
            transpose_adj_list[adj_list[i][j][0]].append((i, adj_list[i][j][1]))
    return transpose_adj_list

def transpose(adj_list):
    transposes = [[] for i in range(0, len(adj_list))]
    for i in range(0, len(adj_list)):
        for j in range(0, len(adj_list[i])):
            transposes[adj_list[i][j][0]].append((i, adj_list[i][j][1]))
#graph_string = """\
#D 3
#0 1
#1 0
#0 2
#"""

#graph_adj_list = adjacency_list(graph_string)
#graph_transposed_adj_list = transpose(graph_adj_list)
#for i in range(len(graph_transposed_adj_list)):
#    print(i, sorted(graph_transposed_adj_list[i]))

#graph_string = """\
#D 3 W
#0 1 7
#1 0 -2
#0 2 0
#"""

#graph_adj_list = adjacency_list(graph_string)
#graph_transposed_adj_list = transpose(graph_adj_list)
#for i in range(len(graph_transposed_adj_list)):
#    print(i, sorted(graph_transposed_adj_list[i]))
    
# It should also work undirected graphs.
# The output will be the same as input.

#graph_string = """\
#U 7
#1 2
#1 5
#1 6
#2 3
#2 5
#3 4
#4 5
#"""

#graph_adj_list = adjacency_list(graph_string)
#graph_transposed_adj_list = transpose(graph_adj_list)
#for i in range(len(graph_transposed_adj_list)):
#    print(i, sorted(graph_transposed_adj_list[i]))
    
#graph_string = """\
#U 17
#1 2
#1 15
#1 6
#12 13
#2 15
#13 4
#4 5
#"""

#graph_adj_list = adjacency_list(graph_string)
#graph_transposed_adj_list = transpose(graph_adj_list)
#for i in range(len(graph_transposed_adj_list)):
#    print(i, sorted(graph_transposed_adj_list[i]))    

def is_strongly_connected(adj_list):
    something
    
    



def next_vertex(in_tree, distance):
    """Helper function to gain the next vertex to
    be used in Prim's and Dijkstra's algorithm"""
    possible_next = [] # Array to hold possible choices for next vertex
    next_vert = None # Initializing next vertex to None
    for index, vertex in enumerate(in_tree): # Looping over vertices in tree
        if not vertex:
            possible_next.append(index) # Vertex is not in tree so is considered for next vertex
    min_weight = distance[possible_next[0]] # Setting initial min weight
    next_vert = possible_next[0]
    for i in possible_next: # Looping over possible next vertices
        weight = distance[i] # Getting weight of current vertex
        if weight < min_weight: # Checking if current vertex has small weight than min weight
            min_weight = weight
            next_vert = i
    return next_vert # Returning next vertex


def next_vertex(intree, distance):
    possible = []
    nextvert = None
    for index, vertex in enumerate(intree):
        if not vertex:
            possible.append(index)
    minweight = distance[possible[0]]
    nextvert = possible[0]
    for i in possible:
        weight = distance[i]
        if weight < minweight:
            minweight = weight
            nextvert = i
    return nextvert

#from math import inf
#in_tree = [False, True, True, False, False]
#distance = [float('inf'), 0, 3, 12, 5]
#print(next_vertex(in_tree, distance))

#in_tree = [False, False, False]
#distance = [float('inf'), 0, float('inf')]
#print(next_vertex(in_tree, distance))

#from math import inf
#in_tree = [True, True, True, False, True]
#distance = [inf, 0, inf, inf, inf]
#print(next_vertex(in_tree, distance))


def dijkstra(adj_list, start):
    n = len(adj_list)
    in_tree = [False] * n
    distance = [float('inf')] * n
    parent = [None] * n
    distance[start] = 0
    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in adj_list[u]:
            if not in_tree[v] and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u
    return parent, distance
    

#graph_string = """\
#D 3 W
#1 0 3
#2 0 1
#1 2 1
#"""

#print(dijkstra(adjacency_list(graph_string), 1))
#print(dijkstra(adjacency_list(graph_string), 2))

#graph_string = """\
#U 4 W
#0 2 5
#0 3 2
#3 2 2
#"""

#print(dijkstra(adjacency_list(graph_string), 0))
#print(dijkstra(adjacency_list(graph_string), 2))

def prim(adj, s):
    n = len(adj)
    in_tree = [False]*n
    distance = [float('inf')]*n
    parent = [None]*n
    distance[s] = 0
    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in adj[u]:
            if not in_tree[v] and weight < distance[v]:
                distance[v] = weight
                parent[v] = u
    return parent, distance

#graph_string = """\
#U 7 W
#0 1 5
#0 2 7
#0 3 12
#1 2 9
#2 3 4
#1 4 7
#2 4 4
#2 5 3
#3 5 7
#4 5 2
#4 6 5
#5 6 2
#"""

#print(prim(adjacency_list(graph_string), 0))