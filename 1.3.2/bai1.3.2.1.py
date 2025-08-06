S = {(2*x + 1) for x in range(10)}
# Thay 2 * x bằng 2 * x + 1. Tập S mới đại diện cho tập các số lẻ từ 1 - > 19
print(len(S))
# In len(S) – số phần tử là 10. Không có phần tử nào trùng.

# Các phép toán
A = {1, 2, 3, 5}
B = {2, 3, 4}
print(A.union(B))        # {1, 2, 3, 4, 5}
# Gán thêm vào A phần tử 5. Sự thay đổi sau union là có thêm phần tử 5
print(A - B) # {1, 5}
print(B - A) # {4}
# B - A khác A - B vì B - A là chỉ lấy những phần tử thuộc B nhưng không thuộc A còn A - B thì ngược lại. 

