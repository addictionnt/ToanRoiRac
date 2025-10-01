from graph_thanhchinh.graph import *

nodes = [1 , 2, 3, 4, 5,6,7,8]
edges = [
    (3, 2, -4),
    (4, 5, -3),
    (1, 7, 2),
    (8, 7, 2),
    (1, 3, 3),
    (7, 8, 3),
    (2, 6, 4),
    (1, 5, 5),
    (5, 4, 6),
    (8, 6, 7),
    (4, 6, 8)
]

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            # Path Compression
            self.parent[i] = self.find(self.parent[i])
            return self.parent[i]
        
        # PHẦN CẦN THÊM: Trả về chính i nếu i là gốc
        return i 

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.rank[s1] < self.rank[s2]:
                self.parent[s1] = s2
            elif self.rank[s1] > self.rank[s2]:
                self.parent[s2] = s1
            else:
                self.parent[s2] = s1
                self.rank[s1] += 1
                
from functools import cmp_to_key

def comparator(a, b):
    # So sánh dựa trên trọng số (phần tử thứ 2 của mỗi cạnh)
    return a[2] - b[2]

def kruskals_mst(V, edges):
    # Sắp xếp các cạnh
    # Cạnh được lưu dưới dạng (u, v, w),
    # dùng comparator để sắp xếp theo w (trọng số)
    edges = sorted(edges, key=cmp_to_key(comparator))
    
    # Duyệt các cạnh theo thứ tự đã sắp xếp
    # V là số lượng đỉnh trong đồ thị
    # DSU phải được khởi tạo với số lượng đỉnh V
    dsu = DSU(V) 
    cost = 0
    count = 0
    
    # x, y là các đỉnh, w là trọng số
    for x, y, w in edges:
        # Kiểm tra cạnh không tạo thành chu trình
        # Nếu hai đỉnh x và y không cùng thuộc một tập hợp (component)
        if dsu.find(x) != dsu.find(y):
            # Kết hợp hai tập hợp (thêm cạnh vào MST)
            dsu.union(x, y)
            cost += w
            count += 1
            
            # Nếu đã có V-1 cạnh, tức là đã tìm được MST
            if count == V - 1:
                break
                
    return cost

#---------------------------------------------------------

import sys
class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[parent[i]][i])

    def minKey(self, key, mstSet):
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index
    
    
def primMST(self):
    key = [sys.maxsize] * self.V
    parent = [None] * self.V
    key[0] = 0
    mstSet = [False] * self.V
    parent[0] = -1 # First node is always the root of
    for count in range(self.V):
        u = self.minKey(key, mstSet)
        mstSet[u] = True

        for v in range(self.V):
            if self.graph[u][v] > 0 and mstSet[v] == \
               False and key[v] > self.graph[u][v]:
                key[v] = self.graph[u][v]
                parent[v] = u

    self.printMST(parent)
    
    # Tính toán tổng trọng số và tập cạnh
    total_weight = 0
    mst_edges = []
    # Lặp qua mảng key/parent để tính tổng trọng số và xây dựng tập cạnh
    for i in range(1, self.V):
        # Trọng số của cạnh nối i vào cây
        weight = key[i]
        total_weight += weight
        
        # Cạnh là (đỉnh cha, đỉnh con)
        edge = (parent[i], i)
        mst_edges.append(edge)

    # In ra các cạnh (sử dụng hàm đã có)
    self.printMST(parent)
    
    # TRẢ VỀ: (tổng trọng số, danh sách các cạnh)
    return total_weight, mst_edges

#---------------------------------------

import heapq
import sys

# Hàm xây dựng Danh sách Kề (Adjacency List)
def constructAdj(edges, V):
    # adj[u] = list of (v, wt)
    adj = [[] for _ in range(V)]
    
    for edge in edges:
        u, v, wt = edge
        adj[u].append((v, wt))
        # Vì đồ thị là vô hướng, nên thêm cạnh cho cả hai chiều (v, u)
        adj[v].append((u, wt)) 
    return adj

# Hàm triển khai Thuật toán Dijkstra
def dijkstra(V, edges, src):
    adj = constructAdj(edges, V)
    pq = []
    
    dist = [sys.maxsize] * V
    prev = [None] * V  # Thêm mảng lưu đỉnh liền trước
    
    heapq.heappush(pq, [0, src])
    dist[src] = 0
    # prev[src] giữ nguyên là None

    while pq:
        d_u, u = heapq.heappop(pq) 

        if d_u > dist[u]:
            continue
            
        for v, weight in adj[u]:
            
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                prev[v] = u  # Ghi lại đỉnh u là đỉnh liền trước của v
                heapq.heappush(pq, [dist[v], v])

    return dist, prev

src_char = 'a'

# Danh sách các cạnh: (u, v, trọng số)
edges_char = [
    ('a', 'b', 4), ('a', 'c', 3), 
    ('b', 'c', 2), ('b', 'd', 5), 
    ('c', 'd', 3), ('c', 'e', 6), 
    ('d', 'e', 1), ('d', 'f', 5), 
    ('e', 'g', 5), 
    ('f', 'g', 2), ('f', 'z', 7), 
    ('g', 'z', 4)
]
# --- HÀM TÁI TẠO ĐƯỜNG ĐI (Cần thiết để sử dụng mảng 'prev') ---
def get_path(predecessors, target_node):
    """Tái tạo đường đi từ mảng đỉnh liền trước."""
    path = []
    at = target_node
    while at is not None:
        path.append(at)
        at = predecessors[at]
    path.reverse()
    return path

# --- PHẦN THỰC THI (VIẾT TIẾP) ---

# 1. Tạo ánh xạ từ chữ cái sang số nguyên (0, 1, 2, ...)
all_nodes = set()
for u, v, wt in edges_char:
    all_nodes.add(u)
    all_nodes.add(v)
    
# Sắp xếp các đỉnh để đảm bảo ánh xạ ổn định
sorted_nodes = sorted(list(all_nodes)) 
MAPPING = {node: i for i, node in enumerate(sorted_nodes)}
REVERSE_MAPPING = {i: node for node, i in MAPPING.items()}
V = len(sorted_nodes) # V = 8

# 2. Chuyển đổi dữ liệu đồ thị sang chỉ số số nguyên
src_index = MAPPING[src_char]
edges_index = []
for u, v, wt in edges_char:
    edges_index.append((MAPPING[u], MAPPING[v], wt))

# 3. Chạy thuật toán Dijkstra với chỉ số số nguyên
distances_index, predecessors_index = dijkstra(V, edges_index, src_index)

# 4. Tập hợp và trả về kết quả
results = []
for target_char in sorted_nodes:
    if target_char == src_char:
        continue

    target_index = MAPPING[target_char]
    
    # Lấy khoảng cách (Tổng chi phí)
    total_cost = distances_index[target_index]
    
    # Lấy đường đi (List các chỉ số)
    path_indices = get_path(predecessors_index, target_index)
    
    # Chuyển đường đi từ chỉ số sang chữ cái
    path_chars = [REVERSE_MAPPING[i] for i in path_indices]
    
    # Thêm vào List kết quả
    results.append({
        'đỉnh_đích': target_char,
        'tổng_chi_phí': total_cost,
        'đường_đi': path_chars
    })

# Trả về List kết quả cuối cùng
print("--- KẾT QUẢ DIJKSTRA ---")
for res in results:
    path_str = " -> ".join(res['đường_đi'])
    print(f"Đích: {res['đỉnh_đích']} | Chi phí: {res['tổng_chi_phí']:<2} | Đường đi: {path_str}")






    
    
    
