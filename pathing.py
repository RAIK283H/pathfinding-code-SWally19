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
    global_game_data.not_hit_target = True
    # find path from start to target and add path from target to exit
    firstPath = (random_helper(0, global_game_data.target_node[global_game_data.current_graph_index]))
    global_game_data.not_hit_target = False
    secondPath = (random_helper(global_game_data.target_node[global_game_data.current_graph_index], (len(graph_data.graph_array[global_game_data.current_graph_index]) - 1)))
    assert firstPath is not None
    assert secondPath is not None
    return firstPath + secondPath

def random_helper(start, end):
    # precondition: start and end exist
    assert start is not None
    assert end is not None
    assert start != end
    path = []
    curr_node = start
    path.append(curr_node)
    while curr_node != end:
        curr_node = random.choice(graph_data.graph_array[global_game_data.current_graph_index][curr_node][1])
        path.append(curr_node)
    # postcondition: path is not empty
    assert len(path) > 0
    return path


def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
