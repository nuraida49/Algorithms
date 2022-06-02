#Question 1
def format_sequence_helper(dict, source, destination, short_path=[]):
    short_path = short_path + [source]
    if source == destination:
        return short_path
    if source not in dict.keys():
        return("No solution!")
    req_path = None
    for val in dict[source]:
        if val not in short_path:
            new_path = format_sequence_helper(dict, val, destination, short_path)
            if new_path:
                if not req_path or len(new_path) < len(req_path):
                    req_path = new_path
    return req_path

def format_sequence(converters_info, source_format, destination_format):
    dict = {}
    for line in converters_info.splitlines():
        k, v = line.split()
        if (k!='D'):
            if k in dict:
                dict[k].append(v)
            else:
                dict[k] = [v]
    res = format_sequence_helper(dict, str(source_format), str(destination_format), short_path=[])
    if res == None:
        return "No solution!"
    if res[0] == 'N':
        return res
    else:
        res = [int(i) for i in res]
        return res
    
#converters_info_str = """\
#D 2
#0 1
#"""

#source_format = 0
#destination_format = 1

#print(format_sequence(converters_info_str, source_format, destination_format))

#converters_info_str = """\
#D 2
#0 1
#"""

#print(format_sequence(converters_info_str, 1, 1))

#converters_info_str = """\
#D 2
#0 1
#"""

#print(format_sequence(converters_info_str, 1, 0))

#converters_info_str = """\
#D 5
#1 0
#0 2
#2 3
#1 2
#"""

#print(format_sequence(converters_info_str, 1, 2))

#converters_info_str = """\
#D 1
#"""

#print(format_sequence(converters_info_str, 0, 0))


#converters_info_str = """\
#D 5
#0 1
#0 2
#1 2
#2 3
#1 3
#3 0
#"""

#print(format_sequence(converters_info_str, 1, 0))
#print(format_sequence(converters_info_str, 0, 3) in [[0, 1, 3], [0, 2, 3]])
#print(format_sequence(converters_info_str, 4, 4))
#print(format_sequence(converters_info_str, 3, 3))
#print(format_sequence(converters_info_str, 3, 2))
#print(format_sequence(converters_info_str, 3, 4))

#Question 2
def bubbles(physical_contact_info):
    first,second,third=[],[],[]
    #split the text
    x = physical_contact_info.split("\n")
    #x = ['U 2', '0 1', '']
      
    #convert physical_contact_info into list
    for i in range(0,len(x)-1):
        first += x[i].split(' ')
        #first = ['U', '2', '0', '1']

    #***changes made from here**
        
    #function for checking if two sub list contains atleast onecommon element
    #using set property
    def hasComm(a, b):
        a_set = set(a)
        b_set = set(b)
        if (a_set & b_set):
            return True 
        else:
            return False 
    
          
    #**changed
    #join will join list with common element
    def join(any_dcl):
        temp = []
        removeLis = []
        for i in range(0,len(any_dcl)):
            #this condition will help to filter unprocesed lists
            #if(len(any_dcl[i]) == 2):
            if(i == 0):
                for ele in range(len(any_dcl[i])):
                    temp.append(any_dcl[i][ele])
                
                removeLis.append(i)
            else:
                if hasComm(temp,any_dcl[i]):
                    for ele in range(len(any_dcl[i])):
                        temp.append(any_dcl[i][ele])
                    removeLis.append(i)

        temp = list(set(temp))
        #append temp only if tem is not empty
        if(temp):
            any_dcl.append(temp)
        
        #removing merged elements
        for ele in sorted(removeLis, reverse=True):
            del any_dcl[ele]

        return any_dcl       
        
    
    #contacted people in set contacted
    #remove same element
    #contacted = set(first[2:]) #{'5', '3', '2', '4', '6', '1'}
    #contacted as it is making every element in int
    #duplicate values are there
    conAsItIs = list(map(lambda y:int(y), first[2:]))
   

    #detailed contact list
    dcl = []
    #this will be the final detailed list
    #dcl2 = []
    #temporary list
    temp = []


    #as length is always even
    #filling dcl like this
    for i in range(0,len(conAsItIs),2):
        temp.append(conAsItIs[i])
        temp.append(conAsItIs[i+1])
        dcl.append(temp)
        temp = []
    
    #join dcl in desired way until we get same list two times
    while(True):
        if(len(dcl) == len(join(dcl))):
            dcl = join(dcl)
            break
        else:
            dcl = join(dcl)
                    
    #second list ready to save
    second = dcl    
                  
    #if people not contacted with another people, insert in list 'third'
    for j in range(0,int(first[1])):
        if j not in conAsItIs:
            third.append(j)

    #making third as a list of single elements:
    third = list(map(lambda y:[y], third))

    
    #result
    result = second + third    
 
        
    
        #[[0, 1]]
    return result
    
#physical_contact_info = """\
#U 2
#0 1
#"""

#print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

#physical_contact_info = """\
#U 2
#"""

#print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

#physical_contact_info = """\
#U 7
#1 2
#1 5
#1 6
#2 3
#2 5
#3 4
#4 5
#"""

#print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

#physical_contact_info = """\
#U 0
#"""

#print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))
#physical_contact_info = """\
#U 1
#"""

#print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

#physical_contact_info = """\
#U 5
#1 3
#2 0
#0 1
#0 4
#"""

#print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

def adjacency_list(converters_info_str):
    header, edges = [s.split() for s in converters_info_str.splitlines()]
    directed = header[0] == 'D'
    weighted = len(header) == 3 and header[2] == 'W'
    num_vertices = int(header[1])
    adj_list = [[] for _ in range(num_vertices)]
    for edge in edges:
        edge_data = map(int, edge)
        if weighted:
            source, target, weight = edge_data
        else:
            source, target = edge_data
            weight = None
        adj_list[source].append((target))
        if not directed:
            adj_list[target].append((source))
    return adj_list

def dfs_tree(adj_list, start):
    n = len(adj_list)
    state = ['U'] * n
    parent = [None]*n
    if len(adj_list) != 0:
        state[start] = 'D'
    visited_vertex = dfs_loop(adj_list, start, state, parent)
    return visited_vertex

def bubbles(physical_contact_info):
    adjacent = adjacency_list(physical_contact_info)
    visited = dfs_tree(adjacent, 0)
    return visited

def dfs_loop(adj_list, u, state, parent, visited, vertex=None):
    if vertex is None:
        vertex = []
        if visited_vertex is None:
            visited_vertex =[]
        if len(adj_list) == 0:
            return visited_vertex
        if u >= len(adj_list):
            return visited_vertex
        else:
            if len(adj_list[u])==0:
                visited_vertex.append([u])
                u+=1
                dfs_loop(adj_list, u, state, parent, visited_vertex)
            else:
                for v in adj_list[u]:
                    if v not in vertex:
                        vertex += [v]
                    if state[v] == 'U':
                        state[v] = 'D'
                        parent[v] = u
                        dfs_loop(adj_list, v, state, parent, visited_vertex, vertex)
                state[u] = 'P'
                if vertex not in visited_vertex:
                    visited_vertex.append(vertex)
        return visited_vertex
#physical_contact_info = """\
#U 4
#2 1
#"""

#print(sorted(sorted(bubble)
#      for bubble in bubbles(physical_contact_info)))
    
    
    
#Question 3
def build_order(dependencies):
    graphinput = dependencies.split("\n")
    n = int(graphinput[0].split(" ")[1])
    
    graph = [[] for _ in range(n)]
    for line in range(1, len(graphinput)-1):
        edge = graphinput[line].split(" ")
        graph[int(edge[0])].append(int(edge[1]))
        
    def dfs(u, visited, stack):
        visited[u] = True
        for v in graph[u]:
            if visited[v] == False:
                dfs(v, visited, stack)
        stack.insert(0, u)
        
    stack = []
    visited = [False] * n
    for u in range(n):
        if visited[u] == False:
            dfs(u, visited, stack)
    return stack

#dependencies = """\
#D 2
#0 1
#"""

#print(build_order(dependencies))
#dependencies = """\
#D 3
#1 2
#0 2
#"""

#print(build_order(dependencies) in [[0, 1, 2], [1, 0, 2]])

#dependencies = """\
#D 3
#"""
# any permutation of 0, 1, 2 is valid in this case.
#solution = build_order(dependencies)
#if solution is None:
#    print("Wrong answer!")
#else:
#    print(sorted(solution))



#Question 4
# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # dictionary to store graph
        
    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
        
    # A utility function to find set of an element i
    # (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # The main function to construct MST using Kruskal's
    # algorithm
    def KruskalMST(self):
        result = []  # This will store the resultant MST
        # An index variable, used for sorted edges
        i = 0
        # An index variable, used for result[]
        e = 0
        # Step 1:  Sort all the edges in
        # non-decreasing order of their
        # weight.  If we are not allowed to change the
        # given graph, we can create a copy of graph
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])
        parent = []
        rank = []
        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:
            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            # If including this edge does't
            #  cause cycle, include it in result
            #  and increment the indexof result
            # for next edge
            if x != y:
                e = e + 1
                if u<v:
                    result.append((u, v))
                else:
                    result.append((v, u))
                self.union(parent, rank, x, y)
            # Else discard the edge
        return result
    
# function to find the which road segment to clear 
def which_segments(city_map):
    # splitting the data into lines
    lines = city_map.split('\n')
    # getting number of vertices
    vertex = int(lines[0].split()[1])
    # creating a graph object
    g = Graph(vertex)
    # reading data of lines
    for i in range(1,len(lines)-1):
        # splitting data of each line
        data = lines[i].split()
        # adding edges to the graph
        g.addEdge(int(data[0]),int(data[1]),int(data[2]))
    # calling kruskals algo to get the Minimum spanning tree
    return g.KruskalMST()
#city_map = """\
#U 3 W
#0 1 1
#2 1 2
#2 0 4
#"""

#print(sorted(which_segments(city_map)))
#city_map = """\
#U 1 W
#"""

#print(sorted(which_segments(city_map)))

#Question 5
import math

def min_capacity(city_map, depot_position):
    city_map = city_map.replace("\n", " ")
    map_data = city_map.split(" ")

    # delete unnecessary data
    map_data.pop()
    map_data.pop(0)
    map_data.pop(0)

    # no of vertices in the graph
    V = int(map_data[1])

    graph = []
    # creating the graph with all the edges
    for i in range(3, len(map_data), 3):
        u, v, w = int(map_data[i]), int(map_data[i + 1]), int(map_data[i + 2])
        graph.append((u, v, w))
        graph.append((v, u, w))

    # shortest path distance from depot_position to all other cities
    dist = get_shortest_path(graph, V, depot_position)
    max_dist = 0
    for d in dist:
        if d != float('inf') and d > max_dist:
            max_dist = d

    # calculate min_battery_capacity based on the requirements
    min_battery_capacity = int(math.ceil(max_dist * 12 * 3 * 1.25))
    return min_battery_capacity


# returns shortest path distance from depot_position to all other cities
# using bellman-ford algorithm
def get_shortest_path(graph, V, src):
    # Initialize distances from src to all other vertices
    # as INFINITE
    dist = [float("inf")] * V
    dist[src] = 0

    # Relax all edges |V| - 1 times. A simple shortest
    # path from src to any other vertex can have at-most |V| - 1
    # edges
    for i in range(V - 1):
        # Update dist value and parent index of the adjacent vertices of
        # the picked vertex. Consider only those vertices which are still in
        # queue
        for u, v, w in graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # check for negative-weight cycles. The above step
    # guarantees shortest distances if graph doesn't contain
    # negative weight cycle. If we get a shorter path, then there
    # is a cycle.

    for u, v, w in graph:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            return

    return dist
# testing the code

city_map = """\
U 4 W
0 2 5
0 3 2
3 2 2
"""

print(min_capacity(city_map, 0))
print(min_capacity(city_map, 1))
print(min_capacity(city_map, 2))
print(min_capacity(city_map, 3))

def bfs_loop(adj_list, queue, state):
    while len(queue) != 0:
        u = queue.pop(0)
        for v in adj_list[u]:
            print(v)
            if state[u] is False:
                state[u] = True
                queue.append(u)
    return queue

def bubbles(physical_contact_info):
    n = len(physical_contact_info)
    state = [False] * n
    queue = []
    components = {}
    for i in range(0, n-1):
        if state[i] is False:
            previous = state
            state[i] = True
            queue.append([i])
            bfs_loop(physical_contact_info, queue, state)
            new_component = i
            components = components.extend({new_component})
    return components    