#COSC261 w4
def shuffle(s, t):
    if s == '':
        return {t}
    if t == '':
        return {s}
    else:
        just_s = [s[0] + i for i in shuffle(s[1:], t)]
        just_t = [t[0] + j for j in shuffle(s, t[1:])]
        just_s.extend(just_t)
        return set(just_s)


#print(sorted(shuffle('ab', 'cd')))
#print(sorted(shuffle('', 'e')))
#print(sorted(shuffle('abab', 'baba')))
#print(sorted(shuffle('', '')))

def shuffle_language(A, B):
    if A == {} or B == {}:
        return []
    else:
        answer = []
        for i in A:
            for j in B:
                answer.extend(shuffle(i, j))
    return set(answer)
    
       
#print(sorted(shuffle_language({'ab'}, {'cd', 'e'})))
#print(sorted(shuffle_language({''}, {'ab', 'aa', 'ac'})))

def all_subsets(s):
    """A is an iterable (list, tuple, set, str, etc)
    returns a set which is the power set of A."""
    length = len(s)
    elem = [item for item in s]
    result = set()

    for i in range(2 ** length):
        selector = f'{i:0{length}b}'
        subset = {elem[j] for j, bit in enumerate(selector) if bit == '1'}
        result.add(frozenset(subset))

    return result

#print(sorted(map(sorted, all_subsets({0, 1, 2}))))
#print(sorted(map(sorted, all_subsets({'a', 'b'}))))
#print(sorted(map(sorted, all_subsets({0, 1, 2}))))
#print({1} in all_subsets({0, 1, 2}))

#cosc262

def distance_matrix(adj_list):
    #finding number of edges
    n = len(adj_list)
    
    #initialising matrix with all infinity
    resultant_matrix = [([float('inf')] * n) for i in range(n)]
    
    #placing 0 at diagonals
    
    for i in range(n):
        resultant_matrix[i][i] = 0
        
    #filling the weights at the indexes combination representing edges
    for i in range(n):
        for k,v in adj_list[i]:
            resultant_matrix[i][k] = v
            
    return resultant_matrix

def distance_matrix(adj_list):
    n = len(adj_list)
    resultant = [([float('inf')] * n) for i in range(n)]
    for i in range(n):
        resultant[i][i] = 0
    for i in range(n):
        for k, v in adj_list[i]:
            resultant[i][k] = v
    return resultant

#graph_str = """\
#U 3 W
#0 1 5
#2 1 7
#"""

#adj_list = adjacency_list(graph_str)
#print(distance_matrix(adj_list))

# more readable output (less readable code):
#print("\nEach row on a new line:")
#print("\n".join(str(lst) for lst in distance_matrix(adj_list)))

#graph_str = """\
#D 2 W
#0 1 4
#"""

#adj_list = adjacency_list(graph_str)
#print(distance_matrix(adj_list))

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

def floyd(distance):
    n = len(distance)
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    return distance

      
#graph_str = """\
#D 3 W
#0 1 1
#1 2 2
#2 0 4
#"""

#adj_list = adjacency_list(graph_str)
#dist_matrix = distance_matrix(adj_list)
#print("Initial distance matrix:", dist_matrix)
#dist_matrix = floyd(dist_matrix)
#print("Shortest path distances:", dist_matrix)
    
    

def permutations(s):
    solutions = []
    dfs_backtrack((), s, solutions)
    return solutions


def dfs_backtrack(candidate, input_data, output_data):
    if should_prune(candidate):
        return
    if is_solution(candidate, input_data):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate, input_data):
            dfs_backtrack(child_candidate, input_data, output_data)

    
def add_to_output(candidate, output_data):
    output_data.append(candidate)

    
def should_prune(candidate):
    return False

def is_solution(candidate, input_data):
    """Returns True if the candidate is complete solution"""
    if set(candidate) == set(input_data):
        return True
    else:
        return False    


def children(candidate, input_data):
    """Returns a collestion of candidates that are the children of the given
    candidate."""
    child = []
    for x in input_data:
        #if x is not present in candidate make a new child by appending x in candidate
        #and inserting new child in child
        if x not in candidate:
            child.append(candidate + (x,))
    return child

def children(candidate, input_data):
    child =[]
    for x in input_data:
        if x not in candidate:
            child.append(candidate + (x,))
    return child

#print(sorted(permutations({1,2,3})))
#print(sorted(permutations({'a'})))
#perms = permutations(set())
#print(len(perms) == 0 or list(perms) == [()])



def all_paths(adj_list, source, destination):
    paths = []
    for neighbour, _ in adj_list[source]:
        pth = [source, neighbour]
        if neighbour == destination:
            paths.append(pth)
        else:
            node = finder(adj_list, neighbour, ['U'] * len(adj_list), pth, destination)
            paths.append(pth + [node])
    return paths

def finder(adj_list, current, state, pth, end):
    for neighbour, _ in adj_list[current]:
        if neighbour == end:
            state[neighbour] = 'D'
            return neighbour
        elif state[neighbour] == 'U':
            state[neighbour] = 'D'
            return finder(adj_list, neighbour, state, pth, end)

    
def permutations(s):
    solutions = []
    dfs_backtrack((), s, solutions)
    return solutions


def dfs_backtrack(candidate_path, adj_list, destination):
    if should_prune(candidate_path):
        return
    if is_solution(candidate_path, destination):
        add_to_output(candidate_path, output_data)
    else:
        for child_candidate in children(candidate_path, adj_list):
            dfs_backtrack(child_candidate, adj_list, destination)

    
def add_to_output(candidate, output_data):
    output_data.append(candidate)

    
def should_prune(candidate):
    return False

def is_solution(candidate_path, destination):
    """Returns True if the candidate is complete solution"""
    if set(candidate_path) == set(destination):
        return True
    else:
        return False    


def children(candidate_path, adj_list):
    """Returns a collestion of candidates that are the children of the given
    candidate."""
    child = []
    for x in adj_list:
        #if x is not present in candidate make a new child by appending x in candidate
        #and inserting new child in child
        if x not in candidate_path:
            child.append(candidate_path + (x,))
    return child

#triangle_graph_str = """\
#U 3
#0 1
#1 2
#2 0
#"""

#adj_list = adjacency_list(triangle_graph_str)
#print(sorted(all_paths(adj_list, 0, 2)))
#print(all_paths(adj_list, 1, 1))

#graph_str = """\
#U 5
#0 2
#1 2
#3 2
#4 2
#1 4
#"""

#adj_list = adjacency_list(graph_str)
#print(sorted(all_paths(adj_list, 0, 1)))

#adj_list_str = """\
#D 2
#0 1
#"""
#adj_list = adjacency_list(adj_list_str)#

#print(all_paths(adj_list, 1, 2))

def distance_matrix(adj_list):
    n = len(adj_list)
    resultant_matrix = [([float('inf')]*n) for i in range(n)]
    for i in range(n):
        resultant_matrix[i][i] = 0
    for i in range(n):
        for vertice, weight in adj_list[i]:
            resultant_matrix[i][vertice] = weight
    return resultant_matrix

def floyd(distance):
    n = len(distance)
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    return distance

#graph_str = """\
#D 3 W
#0 1 1
#1 2 2
#2 0 4
#"""

#adj_list = adjacency_list(graph_str)
#dist_matrix = distance_matrix(adj_list)
#print("Initial distance matrix:", dist_matrix)
#dist_matrix = floyd(dist_matrix)
#print("Shortest path distances:", dist_matrix)

#import pprint

#graph_str = """\
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

#pprint.pprint(floyd(distance_matrix(adjacency_list(graph_str))))

def permutations(s):
    solutions = []
    dfs_backtrack((), s, solutions)
    return solutions


def dfs_backtrack(candidate, input_data, output_data):
    if should_prune(candidate):
        return
    if is_solution(candidate, input_data):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate, input_data):
            dfs_backtrack(child_candidate, input_data, output_data)

    
def add_to_output(candidate, output_data):
    output_data.append(candidate)

    
def should_prune(candidate):
    return False

def is_solution(candidate_path, destination):
    """Returns True if the candidate is complete solution"""
    # Complete the code
    return set(input_data) == set(candidate)


def children(candidate_path, adj_list):
    """Returns a collestion of candidates that are the children of the given
    candidate."""
    
    # Complete the code
    child = []
    for i in input_data:
        if i not in candidate:
            child.append(candidate + (i,))
    return(child)
