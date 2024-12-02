import math
import sys
import graph_data
import global_game_data

def floyd_warshall():
    graph = graph_data.graph_array[global_game_data.current_graph_index]
    
    return floyd_warshall_helper(graph)

def floyd_warshall_helper(start, end, graph):
    matrix = create_matrix(graph)
    parent = get_parents(matrix, len(graph))
    path = get_path_from_parent_matrix(parent, start, end)
    return path

def get_parents(matrix, size):
    parent = [[-1 for col in range(size)] for row in range(size)]
    for k in range(len(matrix) - 1):
        for i in range(len(matrix) - 1):
            for j in range(len(matrix) - 1):
                if (matrix[i][k] + matrix[k][j]) < matrix[i][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
                    if k != -1:
                        parent[i][j] = k
    return parent

def get_path_from_parent_matrix(parent, start, end):
    path = []
    child = end
    path.append(child)

    while child != -1:
        curr_parent = parent[start][child]
        if (curr_parent != -1):
            path.append(curr_parent)
        child = curr_parent
   
    path.append(start)
    path.reverse()
    return path

def create_matrix(graph):
    matrix = [[sys.maxsize for col in range(len(graph))] for row in range(len(graph))]
    for node in range(len(graph)):
        for connection in graph[node][1]:
            matrix[node][connection] = math.sqrt(math.pow(graph[node][0][0] - graph[connection][0][0], 2) + math.pow(graph[node][0][1] - graph[connection][0][1], 2))
    return matrix
