from city_network_graph import create_weight_graph

G = create_weight_graph()

def deykstra(graph, start):
    shortest_paths = {node: float('inf') for node in graph.nodes()}  # Словник найкоротших шляхів
    shortest_paths[start] = 0  # Відстань від початкової вершини до себе = 0
    visited = set()  # Множина відвіданих вершин

    while len(visited) < len(graph.nodes()):  # Поки не відвідали всі вершини графа
        current_node = None
        min_distance = float('inf')
        for node in graph.nodes():  # Найменша відстань серед невідвіданих вершин
            if node not in visited and shortest_paths[node] < min_distance:
                current_node = node
                min_distance = shortest_paths[node]
        visited.add(current_node)  # Додаємо поточну вершину до відвіданих

        # Оновлюємо відстані до сусідніх вершин через поточну вершину
        for neighbor, edge_data in graph[current_node].items():
            distance = shortest_paths[current_node] + edge_data['weight']
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance

    return shortest_paths

shortest_paths_from_kyiv = deykstra(G, "Київ")

# Виведення найкоротших шляхів
for city, distance in shortest_paths_from_kyiv.items():
    print(f"Найкоротший шлях з Києва до {city}: {distance} км")