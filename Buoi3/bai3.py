def generate_permutations_iterative(n):
    print("--- Hoán vị bằng phương pháp sinh (không đệ quy) ---")
    
    a = list(range(1, n + 1))
    
    while True:
        print("".join(map(str, a)))
        
        i = n - 1
        while i > 0 and a[i-1] >= a[i]:
            i -= 1
        
        if i <= 0:
            break
        
        j = n - 1
        while a[j] <= a[i-1]:
            j -= 1
            
        a[i-1], a[j] = a[j], a[i-1]
        
        left, right = i, n - 1
        while left < right:
            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1
            
            
def generate_permutations_recursive(n):
    print("\n--- Hoán vị bằng phương pháp quay lui (đệ quy) ---")
    
    a = [0] * n 
    used = [False] * (n + 1) 
    
    def backtrack(k):
        if k == n:
            print("".join(map(str, a)))
            return
        
        for i in range(1, n + 1):
            if not used[i]:
                a[k] = i
                used[i] = True
                backtrack(k + 1) 
                used[i] = False 
    backtrack(0)
    
def main():
    try:
        n = int(input("Nhập n: "))
        
        if n <= 8:
            generate_permutations_iterative(n)
            generate_permutations_recursive(n)
        else:
            print("Đầu vào không hợp lệ. Vui lòng đảm bảo n <= 8.")
            
    except ValueError:
        print("Đầu vào không hợp lệ. Vui lòng nhập số nguyên.")

if __name__ == "__main__":
    main()