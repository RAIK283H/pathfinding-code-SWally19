# Pathfinding Starter Code
Requirements:
- The Random player shall have a randomly assigned path which begins with the start node, ends with the exit node, and hits the target along the path. The path shall be a valid traversal such that each sequential pair of nodes in the path are connected by an edge.
- Add another statistic to the scoreboard (up to interpretation)

My random path algorithm uses the choices funtion in the random library to randomly choose an adjacent node to travel to next, it loops once to hit the target and then loops again to hit the exit. With this implementation, the player can reach the exit before hitting the target in some cases but will not be able to move on without hitting the target first. It can also return to the start as many times as it randomly chooses.

My statistic is simply listing the player's color to make it more accessible to color blind users.

Each player, besides test, is compared to the minimum distance calculated from comparing the distance from each path to determine whether or not they are a "winner".

Dijkstra's algorithm has a boolean parameter called a_star to determine whether or not a heuristic approach is used. (extra credit)