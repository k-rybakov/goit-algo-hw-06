import networkx as nx
import matplotlib.pyplot as plt
from city_network_graph import create_graph

G = create_graph()

plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_color='lightgreen', node_size=2000, font_size=12, font_weight='bold')
plt.title("Транспортна мережа міст України")
plt.show()

print("Кількість вершин (міст):", G.number_of_nodes())
print("Кількість ребер (доріг):", G.number_of_edges())
print("Ступінь вершин:")
for city in cities:
    print(city, ":", G.degree[city])
