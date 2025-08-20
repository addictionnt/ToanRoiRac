def generate_combinations(n, k):
    a = list(range(1, k + 1))
    
    while True:
        print("".join(map(str, a)))
        
        i = k - 1
        while i >= 0 and a[i] == n - k + i + 1:
            i -= 1
        
        if i < 0:
            break
        
        a[i] += 1
        
        for j in range(i + 1, k):
            a[j] = a[j - 1] + 1

def main():
    try:
        n = int(input("Nhập n: "))
        k = int(input("Nhập k (1 <= k <= n): "))
        
        if 1 <= k <= n:
            print(f"Các tổ hợp chập {k} của {n} phần tử là:")
            generate_combinations(n, k)
        else:
            print("Đầu vào không hợp lệ. Vui lòng đảm bảo 1 <= k <= n.")
            
    except ValueError:
        print("Đầu vào không hợp lệ. Vui lòng nhập số nguyên.")

if __name__ == "__main__":
    main()