import graph_data
import permutation

for i in range(len(graph_data.graph_array)):
    graph = graph_data.graph_array[i]
    print("Graph ", (i + 1))
    print(permutation.get_cycles(graph))