def bu_tru_2_th():
    a = int(input("Nhập số lượng tập đầu tiên: "))
    b = int(input("Nhập số lượng tập thứ 2: "))
    c = int(input("Nhập số lượng chung của 2 tập hợp : "))
    ket_qua = a + b -c
    print(f"Kết quả: {ket_qua}")
    
def bu_tru_3_th():
    a = int(input("Nhập số lượng tập đầu tiên: "))
    b = int(input("Nhập số lượng tập thứ 2: "))
    c = int(input("Nhập số lượng tập thứ 3: "))
    ab = int(input("Nhập số lượng chung của 2 tập hợp 1,2: "))
    ac = int(input("Nhập số lượng chung của 2 tập hợp 1,3: "))
    bc = int(input("Nhập số lượng chung của 2 tập hợp 2,3: "))
    abc = int(input("Nhập số lượng chung của 3 tập hợp 1,2,3: "))
    ket_qua = a + b + c - ab - ac - bc + abc
    print(f"Kết quả: {ket_qua}")
    
if __name__ == "__main__":
    so_luong = int(input("Nhập số tập hợp: "))
    if so_luong == 2:
        bu_tru_2_th()
    elif so_luong == 3:
        bu_tru_3_th()
        
#Có 2 môn thể thao bóng đá, bóng chuyền có 15 người bóng đá, 20 người bóng chuyền có 5 người
#chơi cả 2 hỏi có bn người chơi ít nhất 1 môn