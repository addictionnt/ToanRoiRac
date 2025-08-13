import math
def de_quy(n, k):
    if k == 0 or k == n:
        return 1
    if k < 0 or k > n:
        return 0
    return de_quy(n - 1, k - 1) + de_quy(n - 1, k)


if __name__ == "__main__":
    n = int(input("Nhập n: "))
    k = int(input("Nhập k: "))
    ket_qua = de_quy(n, k)
    print(f"Kết quả: {ket_qua}")
    
#Tính C(9,5)
    

