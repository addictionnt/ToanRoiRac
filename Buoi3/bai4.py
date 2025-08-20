def solve_n_queens(n):
    board = [-1] * n 
    solutions = []  
    
    def is_safe(row, col):
        for prev_row in range(row):
            if board[prev_row] == col or \
               board[prev_row] - prev_row == col - row or \
               board[prev_row] + prev_row == col + row:
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(list(board))
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row] = col  
                backtrack(row + 1)

    backtrack(0)
    
    print(f"Tổng số phương án tìm được: {len(solutions)}\n")
    for idx, sol in enumerate(solutions):
        print(f"Phương án {idx + 1}:")
        for r in range(n):
            row_str = ""
            for c in range(n):
                if sol[r] == c:
                    row_str += "Q "
                else:
                    row_str += ". "
            print(row_str)
        print("-" * (2 * n - 1))

def main():
    try:
        n = int(input("Nhập kích thước bàn cờ N (N <= 10): "))
        if 1 <= n <= 10:
            solve_n_queens(n)
        else:
            print("Đầu vào không hợp lệ. Vui lòng nhập 1 <= N <= 10.")
    except ValueError:
        print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")

if __name__ == "__main__":
    main()