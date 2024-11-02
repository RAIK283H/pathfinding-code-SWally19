def get_permutations(num):
    permutations = []
    # implement SJT
    # initialize list of ordered elements poitning left (negative)
    current_sequence = initialize(num)
    permutations.append(sequence_to_store(current_sequence))
    mobile = find_largest_mobile(current_sequence)

    # repeat until there are no mobile integers
    while mobile != 0:
        # swap largest mobile with the neightbor it is pointing to
        current_sequence = swap_elements(current_sequence, current_sequence.index(mobile))
        # swap direction of all integers with value greater than the mobile
        current_sequence = swap_direction(current_sequence, mobile)
        # store permutation in the permutations array
        permutations.append(sequence_to_store(current_sequence))
        # find largest mobile integer
        mobile = find_largest_mobile(current_sequence)

    return permutations

def initialize(num):
    elements = []
    for i in range(1, num + 1):
        elements.append(0 - i)
    return elements

# negative = left
# positive = right
# integer is mobile if greater than neighbor it points to
# returns 0 if no mobiles are present
def find_largest_mobile(sequence):
    mobiles = []
    for i in range(len(sequence)):
        if sequence[i] < 0 and i != 0:
            if abs(sequence[i]) > abs(sequence[i - 1]):
                mobiles.append(sequence[i])
        if sequence[i] > 0 and i != len(sequence) - 1:
            if abs(sequence[i]) > abs(sequence[i + 1]):
                mobiles.append(sequence[i])
    if not mobiles:
        return 0
    mobiles.sort()
    if abs(mobiles[0]) > abs(mobiles[len(mobiles) - 1]):
        return mobiles[0]
    else:
        return mobiles[len(mobiles) - 1]
    
# swpas element at index one within the given sequence with the neighbor it is pointing to
def swap_elements(sequence, mobile_index):
    temp = sequence[mobile_index]
    if (sequence[mobile_index] > 0 and mobile_index != len(sequence) - 1):
        sequence[mobile_index] = sequence[mobile_index + 1]
        sequence[mobile_index + 1] = temp
    elif (sequence[mobile_index] < 0 and mobile_index != 0):
        sequence[mobile_index] = sequence[mobile_index - 1]
        sequence[mobile_index - 1] = temp
    return sequence

# swaps direction of every element larger than the given value in the sequence
def swap_direction(sequence, num):
    for i in range(len(sequence)):
        if abs(sequence[i]) > abs(num):
            sequence[i] = sequence[i] * -1
    return sequence

#copies an absolute value version of the sequence into another array
def sequence_to_store(sequence):
    copy = []
    for i in range(len(sequence)):
        copy.append(abs(sequence[i]))
    return copy

# finds Hamiltonian cycles
def get_cycles(graph):
    cycles = []
    permutations = get_permutations(len(graph) - 2)
    for path in permutations:
        if is_valid_path(path, graph) and is_connected_node(graph, path[0], path[len(path) - 1]) :
            cycles.append(path)
    if not cycles:
        return False
    else:
        return cycles


def is_valid_path(path, graph):
    for i in range(len(path) - 1):
        node = path[i]
        next_node = path[i + 1]
        # Check if next_node is in the adjacency list of node
        if (is_connected_node(graph, node, next_node) is False):
            return False
    return True

def is_connected_node(graph, node, next_node):
    if next_node not in graph[node][1]:
        return False
    else:
        return True