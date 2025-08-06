A = {1, 2, 3}
B = {2, 3, 4}
C = {2, 3}

print(C.issubset(A)) # True
print(C.issubset(B)) # True
# C là tập con của cả A và B

print(A.issuperset(C)) # True
print(B.issuperset(C)) # True

print(set() == set([]) ) # True
# Đúng vì cả 2 đều tạo tập rỗng

D = set()
print(D.issubset(A)) # True
print(A.issuperset(D)) # True
# Đúng vì tập rỗng là con mọi tập hợp, mọi tập hợp là cha tập rỗng 
