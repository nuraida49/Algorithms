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
#graph_string = """\
#D 3
#0 1
#1 0
#0 2
#"""
#print(adjacency_list(graph_string))      

#graph_string = """\
#D 3 W
#0 1 7
#1 0 -2
#0 2 0
#"""
#print(adjacency_list(graph_string))

#from pprint import pprint

# undirected graph in the textbook example
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

#pprint(adjacency_list(graph_string))

#from pprint import pprint

#graph_string = """\
#U 17
#1 2
#1 15
#1 6
#2 13
#2 15
#13 4
#4 5
#"""

#pprint(adjacency_list(graph_string))



def adjacency_matrix(graph_str):
    result = []
    for line in graph_str.splitlines():
        result.append(line.split())
    
    num = int(result[0][1])
    graph_type = result[0][0]
    weight = False
    
    if len(result[0]) > 2:
        adj_matrix = [([None] * num) for i in range(num)]
        weight = True
    else:
        adj_matrix = [([0] * num) for i in range(num)]
    
    if graph_type == 'U':
        i = 1
        while i < len(result):
            index = int(result[i][0])
            vertex = int(result[i][1])
            if weight:
                weighted = int(result[i][2])
            else:
                weighted = 1
            adj_matrix[index][vertex] = weighted
            adj_matrix[vertex][index] = weighted
            i += 1
    elif graph_type == 'D':
        i = 1
        while i < len(result):
            index = int(result[i][0])
            vertex = int(result[i][1])
            if weight:
                weighted = int(result[i][2])
            else:
                weighted = 1
            adj_matrix[index][vertex] = weighted
            i += 1        
    
    return adj_matrix 
#graph_string = """\
#D 3
#0 1
#1 0
#0 2
#"""

#print(adjacency_matrix(graph_string))
#graph_string = """\
#D 3 W
#0 1 7
#1 0 -2
#0 2 0
#"""
#print(adjacency_matrix(graph_string))
#from pprint import pprint

#graph_string = """\
#U 7
#1 2
#1 5
#1 6
#3 4
#0 4
#4 5
#"""

#pprint(adjacency_matrix(graph_string))

#from pprint import pprint

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

#pprint(adjacency_matrix(graph_string))
    
def bfs_tree(adj_list, start):
    n = len(adj_list)
    state = [False] * n
    parent = [None] * n
    queue = []
    state[start] = True
    queue.append(start)
    return bfs_loop(adj_list, queue, state, parent)
    
def bfs_loop(adj_list, queue, state, parent):
    while len(queue) != 0:
        u = queue.pop(0)
        for v, weight in adj_list[u]:
            if state[v] is False:
                state[v] = True
                parent[v] = u
                queue.append(v)
    return parent

# an undirected graph

#adj_list = [
#    [(1, None)],
#    [(0, None), (2, None)],
#    [(1, None)]
#]

#print(bfs_tree(adj_list, 0))
#print(bfs_tree(adj_list, 1))

# a directed graph (note the asymmetrical adjacency list)

#adj_list = [
#[(1, None)],
#[]
#]

#print(bfs_tree(adj_list, 0))
#print(bfs_tree(adj_list, 1))

#graph_string = """\
#D 2
#0 1
#"""

#print(bfs_tree(adjacency_list(graph_string), 0))

#graph_string = """\
#D 2
#0 1
#1 0
#"""

#print(bfs_tree(adjacency_list(graph_string), 1))

# graph from the textbook example
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

#print(bfs_tree(adjacency_list(graph_string), 1))

#graph_string = """\
#D 2 W
#0 1 99
#"""

#print(bfs_tree(adjacency_list(graph_string), 0))
    
def dfs_tree(adj_list, start):
    n = len(adj_list)
    state = [False] * n
    parent = [None] * n
    state[start] = True
    dfs_loop(adj_list, start, state, parent)
    return parent
    
def dfs_loop(adj_list, u, state, parent):
    for v, weight in adj_list[u]:
        if state[v] is False:
            state[v] = True
            parent[v] = u
            dfs_loop(adj_list, v, state, parent)

# an undirected graph

adj_list = [
    [(1, None), (2, None)],
    [(0, None), (2, None)],
    [(0, None), (1, None)]
]

print(dfs_tree(adj_list, 0))
print(dfs_tree(adj_list, 1))
print(dfs_tree(adj_list, 2))

# a directed graph (note the asymmetrical adjacency list)

adj_list = [
[(1, None)],
[]
]

print(dfs_tree(adj_list, 0))
print(dfs_tree(adj_list, 1))

# graph from the textbook example
graph_string = """\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""

print(dfs_tree(adjacency_list(graph_string), 1))

gstring = """\
U 4
2 3
2 1
0 3
1 0
"""

print(dfs_tree(adjacency_list(gstring), 0))
     
