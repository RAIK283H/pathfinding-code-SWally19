import math
import graph_data
import global_game_data

def floyd_marshall():
    graph = graph_data.graph_array[global_game_data.current_graph_index]
    # make matrix
    matrix = create_matrix(graph)
    parent = floyd_marshall_helper(matrix)
    path = get_path_from_parent_matrix(parent)
    return path

def floyd_marshall_helper(matrix):
    parent = []
    for k in range(len(matrix) - 1):
        for i in range(len(matrix) - 1):
            for j in range(len(matrix) - 1):
                if (matrix[i][k] + matrix[k][j]) < matrix[i][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
                    parent[i][j] = k
    return parent

def get_path_from_parent_matrix(parent, start, end):
    #TODO: test this function
    path = []
    child = end
    path.append(child)
    # I don't think this while loop will work as intended
    while(path[len(path) - 1] != start):
        curr_parent = parent[start][child]
        path.append(curr_parent)
        child = curr_parent

    path.reverse()
    return path

def create_matrix(graph):
    #TODO: test this function
    matrix = [[-1 for col in range(len(graph))] for row in range(len(graph))]
    for node in range(len(graph)):
        for connection in graph[node][1]:
            matrix[node][connection] = math.sqrt(math.pow(graph[node][0][0] - graph[connection][0][0], 2) + math.pow(graph[node][0][1] - graph[connection][0][1], 2))
    return matrix
