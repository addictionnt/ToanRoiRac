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

cost = kruskals_mst(9, edges)

print(cost)



mport sys
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
