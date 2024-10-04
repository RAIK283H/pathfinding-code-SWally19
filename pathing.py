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


def get_random_path(): 
    # find path from start to target and add path from target to exit
    firstPath = (randomHelper(0, global_game_data.target_node[global_game_data.current_graph_index]))
    secondPath = (randomHelper(global_game_data.target_node[global_game_data.current_graph_index], (len(graph_data.graph_array[global_game_data.current_graph_index]) - 1)))
    return firstPath + secondPath

def randomHelper(start, end):
    path = []
    curr_node = start
    path.append(curr_node)
    while curr_node != end:
        curr_node = random.choice(graph_data.graph_array[global_game_data.current_graph_index][curr_node][1])
        path.append(curr_node)
    return path


def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
