def generate_binary_sequences(n):
    a = [0] * n    
    print("".join(map(str, a)))

    while True:
        i = n - 1
        while i >= 0 and a[i] == 1:
            i -= 1

        if i < 0:
            break

        a[i] = 1
        for j in range(i + 1, n):
            a[j] = 0

        print("".join(map(str, a)))

def main():

    try:
        n = int(input("Nhập độ dài n: "))
        if n <= 0:
            print("Độ dài n phải là số nguyên dương.")
        else:
            print(f"Tất cả các dãy nhị phân độ dài {n} là:")
            generate_binary_sequences(n)
    except ValueError:
        print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")

if __name__ == "__main__":
    main()