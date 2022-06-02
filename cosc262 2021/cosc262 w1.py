def concat_list(strings):
    if len(strings) == 0:
        return " "
    else:
        return strings[0] + str(concat_list(strings[1:]))

def concat_list(strings):
    if len(strings) == 0:
        return " "
    else:
        return strings[0] + str(concat_list(strings[1:])

#ans = concat_list(['a', 'hot', 'day'])
#print(ans)
#ans = concat_list(['x', 'y', 'z'])
#print(ans)
#print(concat_list([]))

def product(data):
    if len(data) == 0:
        return 1
    else:
        return data[0] * product(data[1:])

#print(product([1, 13, 9, -11]))

def backwards(s):
    if len(s) == 0:
        return " "
    else:
        return s[-1] + str(backwards(s[:-1]))
    
#print(backwards("Hi there!"))

def odds(data):
    if len(data) == 0:
        return []
    else:
        if data[0] % 2 == 1:
            return [data[0]] + odds(data[1:])
    return odds(data[1:])

print(odds([0, 1, 12, 13, 14, 9, -11, -20]))
            
def find(data, value):
    if data == [] or value not in data:
        return -1
    elif data[0] == value:
        return 0
    else:
        return 1 + find(data[1:], value)
    
#print(find(["hi", "there", "you", "there"], "there"))
#print(find([10, 20, 30], 0))
#print(find(list(range(0,51)), 50))

def squares(data):
    if len(data) == 0:
        return []
    else:
        return [data[0] * data[0]] + squares(data[1:])
    return squares(data[1:])
                   
#print(squares([1, 13, 9, -11]))

def almost_all(numbers): 
    result = []
    total = sum(numbers)
    for x in numbers:
        first = int(total - x)
        result.append(first)
    return result

#print(almost_all([1,2,3]))
#almost_all(list(range(10**5)))
#print("OK")

def sort_of(numbers): 
    for i in range(1, len(numbers)):
        value = numbers[i]
        index = i-1
        while index >= 0:
            if value < numbers[index]:
                numbers[index] = value
                index -= 1
            else:
                break
    return numbers
def sort_of(numbers):
    for i in range(1, len(numbers)):
        value = numbers[i]
        index = i-1
        while index >= 0:
            if value < numbers[index]:
                numbers[index] = value
                index -= 1
            else:
                break
    return numbers
#print(sort_of([1, 2, 3, 3]))
#sort_of(list(range(10**5)))
#print("OK")
#print(sort_of([8, 7]))

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

def all_paths(adj_list, source, destination):
    paths = []
    dfs_backtrack((source,), adj_list, paths)


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
    return len(candidate) == len(input_data)


def children(candidate, input_data):
    result = []
    for i in input_data.difference(set(candidate)):
        result.append(candidate + (i,))
    return result

#triangle_graph_str = """\
#U 3
#0 1
#1 2
#2 0
#"""

#adj_list = adjacency_list(triangle_graph_str)
#print(sorted(all_paths(adj_list, 0, 2)))
#print(all_paths(adj_list, 1, 1))


