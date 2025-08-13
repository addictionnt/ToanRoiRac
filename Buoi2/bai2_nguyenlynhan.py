def nguyen_ly_nhan():
    ket_qua = 1
    truong_hop = int(input("Nhập trường hợp: "))
    for i in range(1, truong_hop + 1):
        i = int(input(f"Trường hợp {i}: "))
        ket_qua = ket_qua * i
    print(f"Kết quả: {ket_qua}")
if __name__ == "__main__":
    nguyen_ly_nhan()

#Lựa chọn quần áo có 2 cách chọn áo, 3 cách chọn quần