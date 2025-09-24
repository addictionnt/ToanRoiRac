import networkx as nx
import matplotlib.pyplot as plt
node = ["A", "B", "C", "D" , "E", "F", "G", "H", "J","I"]
edge = [("A", "B"), ("A", "C"), ("B", "C"), ("B", "E"), ("B", "D"), ("C", "I"),
        ("C", "E"), ("D", "E"), ("D", "F"), ("D", "G"), ("J", "I"), ("J", "H"), ("H", "F"), ("H", "I"), ("F", "G"), ("E", "F"), ("G", "H"), ("G", "I")]

G = nx.Graph(edge)
pos = {
    "A":(1,0.5),
    "B":(1.2,1),
    "C":(1.2,0),
    "D":(1.4,1),
    "E":(1.4,0.5),
    "F":(1.6,1),
    "G":(1.6,0.5),
    "H":(1.8,1),
    "J":(2,0.5),
    "I":(1.8,0)
}

nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=800)
plt.show()

from collections import defaultdict

def find_eulerian_cycle(graph):
    # graph: dict {u:[v1,v2,...]}
    g = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            g[u].append(v)

    stack = [next(iter(graph))]  # bắt đầu từ 1 đỉnh bất kỳ
    path = []

    while stack:
        u = stack[-1]
        if g[u]:
            v = g[u].pop()
            g[v].remove(u)   # xóa cạnh đối xứng
            stack.append(v)
        else:
            path.append(stack.pop())
    return path[::-1]

graph_dict = {n: list(G.neighbors(n)) for n in G.nodes()}

# Kiểm tra điều kiện Euler
if nx.is_eulerian(G):
    cycle = find_eulerian_cycle(graph_dict)
    print("Chu trình Euler:", cycle)
else:
    print("no")