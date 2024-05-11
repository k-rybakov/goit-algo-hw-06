from city_network_graph import create_graph

G = create_graph()

def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            yield from dfs_paths(graph, neighbor, goal, path + [neighbor])

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph.neighbors(vertex):
            if next not in path:
                if next == goal:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))

# Пошук шляхів за допомогою DFS
print("Шляхи з Києва до Чернівців за допомогою DFS:")
for path in dfs_paths(G, "Київ", "Чернівці"):
    print(path)

# Пошук шляхів за допомогою BFS
print("\nШляхи з Києва до Чернівців за допомогою BFS:")
for path in bfs_paths(G, "Київ", "Чернівці"):
    print(path)
