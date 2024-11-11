import sys
import graph_data
import global_game_data
from numpy import random

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]

def assert_path_connected(path, graph):
    for i in range(len(path) - 1):
        node = path[i]
        next_node = path[i + 1]
        
        # Check if next_node is in the adjacency list of node
        if next_node not in graph[node][1]:
            AssertionError
        
def get_random_path(): 
    # find path from start to target and add path from target to exit
    firstPath = (random_helper(0, global_game_data.target_node[global_game_data.current_graph_index]))
    secondPath = (random_helper(global_game_data.target_node[global_game_data.current_graph_index], (len(graph_data.graph_array[global_game_data.current_graph_index]) - 1)))
    assert firstPath is not None
    assert secondPath is not None
    path = firstPath + secondPath[1:len(secondPath)]
    assert global_game_data.target_node[global_game_data.current_graph_index] in path
    assert path[len(path) - 1] == (len(graph_data.graph_array[global_game_data.current_graph_index]) - 1)
    assert_path_connected(path, graph_data.graph_array[global_game_data.current_graph_index])
    return path

def random_helper(start, end):
    # precondition: start and end exist
    assert start is not None
    assert end is not None
    path = []
    curr_node = start
    path.append(curr_node)
    while curr_node != end:
        curr_node = int(random.choice(graph_data.graph_array[global_game_data.current_graph_index][curr_node][1]))
        path.append(curr_node)
    # postcondition: path is not empty
    assert len(path) > 0
    return path


def get_dfs_path():
    firstPath = dfs_helper(0, global_game_data.target_node[global_game_data.current_graph_index], graph_data.graph_array[global_game_data.current_graph_index])
    secondPath = dfs_helper(global_game_data.target_node[global_game_data.current_graph_index], (len(graph_data.graph_array[global_game_data.current_graph_index]) - 1), graph_data.graph_array[global_game_data.current_graph_index])
    path = firstPath + secondPath[1:len(secondPath)]
    assert global_game_data.target_node[global_game_data.current_graph_index] in path
    assert path[len(path) - 1] == (len(graph_data.graph_array[global_game_data.current_graph_index]) - 1)
    assert_path_connected(path, graph_data.graph_array[global_game_data.current_graph_index])
    return path

def dfs_helper(start, end, graph):
    # precondition: start and end exist
    assert start is not None
    assert end is not None
    visited = [False] * len(graph)
    parents = [-1] * len(graph)
    curr_node = start
    visited[curr_node] = True
    path = [start]
    stack = []
    stack.append(curr_node)
    while len(stack) != 0:
        curr_node = stack.pop()

        if curr_node == end:
            break
        
        # find unvisited adjacent node
        for node in graph[curr_node][1]:
            if visited[node] == False:
                stack.append(node)
                visited[node] = True
                parents[node] = curr_node
    # Reconstruct path from end to start using the parent array
    path = []
    step = end
    while step != -1:
        path.append(step)
        step = parents[step]
    # Reverse to get the path from start to end
    path.reverse()
    return path
    

def get_bfs_path():
    firstPath = bfs_helper(0, global_game_data.target_node[global_game_data.current_graph_index], graph_data.graph_array[global_game_data.current_graph_index])
    secondPath = bfs_helper(global_game_data.target_node[global_game_data.current_graph_index], (len(graph_data.graph_array[global_game_data.current_graph_index]) - 1), graph_data.graph_array[global_game_data.current_graph_index])
    path = firstPath + secondPath[1:len(secondPath)]
    assert global_game_data.target_node[global_game_data.current_graph_index] in path
    assert path[len(path) - 1] == (len(graph_data.graph_array[global_game_data.current_graph_index]) - 1)
    assert_path_connected(path, graph_data.graph_array[global_game_data.current_graph_index])
    return path

def bfs_helper(start, end, graph):
    # precondition: start and end exist
    assert start is not None
    assert end is not None
    visited = [False] * len(graph)
    parents = [-1] * len(graph)
    curr_node = start
    visited[curr_node] = True
    queue = []
    queue.append(curr_node)
    while len(queue) != 0:
        curr_node = queue.pop(0)

        if curr_node == end:
            break
        
        # find unvisited adjacent node
        for node in graph[curr_node][1]:
            if visited[node] == False:
                queue.append(node)
                visited[node] = True
                parents[node] = curr_node
    # Reconstruct path from end to start using the parent array
    path = []
    step = end
    while step != -1:
        path.append(step)
        step = parents[step]
    # Reverse to get the path from start to end
    path.reverse()
    return path


def get_dijkstra_path():
    firstPath = dijkstra_helper(0, global_game_data.target_node[global_game_data.current_graph_index], graph_data.graph_array[global_game_data.current_graph_index])
    secondPath = dijkstra_helper(global_game_data.target_node[global_game_data.current_graph_index], (len(graph_data.graph_array[global_game_data.current_graph_index]) - 1), graph_data.graph_array[global_game_data.current_graph_index])
    path = firstPath + secondPath[1:len(secondPath)]
    assert global_game_data.target_node[global_game_data.current_graph_index] in path
    assert path[len(path) - 1] == (len(graph_data.graph_array[global_game_data.current_graph_index]) - 1)
    assert_path_connected(path, graph_data.graph_array[global_game_data.current_graph_index])
    return path

def dijkstra_helper(start, end, graph):
    distance = []
    parent = []
    solved = []
    queue = []
    for i in range(len(graph)):
        # give all nodes cost infinity
        distance.append(sys.maxsize)
        # initialize solved to false
        solved.append(False)
        # initialize parent to the start, this will be overwritten
        parent.append(start)
    distance[start] = 0
    queue.append(start)

    # loop until the queue is empty
    while len(queue) != 0:
        curr_node = find_min(distance, solved)
        queue.remove(curr_node)
        solved[curr_node] = True
        if solved[end] == True:
            break
        # loop through neighbors
        for neighbor in graph[curr_node][1]:
            alt = distance[curr_node] + 1
            if (solved[neighbor] == False) and (alt < distance[neighbor]):
                distance[neighbor] = alt
                parent[neighbor] = curr_node
                queue.append(neighbor)
    # find path to end based on parent queue
    return get_path_from_parents(parent, start, end)

def find_min(list, solved):
    min = sys.maxsize
    index = -1
    for i in range(len(list)):
        if list[i] < min and solved[i] == False:
            min = list[i]
            index = i
    return index

def get_path_from_parents(parent, start, end):
    path = []
    child = end
    path.append(child)
    while(path[len(path) - 1] != start):
        curr_parent = parent[child]
        path.append(curr_parent)
        child = curr_parent

    path.reverse()
    return path
