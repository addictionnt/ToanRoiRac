def nguyen_ly_cong():
    ket_qua = 0
    truong_hop = int(input("Nhập trường hợp: "))
    for i in range(1, truong_hop + 1):
        i = int(input(f"Trường hợp {i}: "))
        ket_qua = ket_qua + i
    print(f"Kết quả: {ket_qua}")
if __name__ == "__main__":
    nguyen_ly_cong()
    
#Đi từ bắc vào Nam có thể đi tàu hoặc máy bay, tàu có 2 hãng máy bay có 3 hãng
