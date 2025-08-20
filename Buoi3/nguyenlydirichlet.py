import math

def min_player_per_map(n_player, n_map):
    return math.ceil(n_player / n_map)

def check(min_player_per_map):
    if(min_player_per_map > 20):
        return "Cần tăng số lượng bản đồ!"
    else:
        return f"Min là {min_player_per_map} người / bản đồ"
    
if __name__ == '__main__':
    n_player = int(input("Nhập số lượng người chơi: "))
    n_map = int(input("Nhập số lượng bản đồ: "))
    min_player_per_map = min_player_per_map(n_player, n_map)
    print(check(min_player_per_map))