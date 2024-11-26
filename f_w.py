import graph_data
import global_game_data

def floyd_marshall():
    graph = graph_data.graph_array[global_game_data.current_graph_index]
    # make matrix
    matrix = create_matrix(graph)
    parent = floyd_marshall_helper(matrix)
    path = get_path_from_parent_matrix(parent)

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
    #TODO: implement this function
    path = []
    child = end
    path.append(child)
    while(path[len(path) - 1] != start):
        curr_parent = parent[child]
        path.append(curr_parent)
        child = curr_parent

    path.reverse()
    return path

def create_matrix(graph):
    #TODO: implement this function
    matrix = []
    return matrix
