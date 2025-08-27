import heapq
import numpy as np
import time

def nguoi_du_lich_tsp_dung_thu_vien(ma_tran_chi_phi):
    """
    Giải bài toán người du lịch (TSP) bằng Branch and Bound sử dụng thư viện numpy.
    """
    thoi_gian_bat_dau = time.time()
    so_thanh_pho = len(ma_tran_chi_phi)
    so_nut_mo_rong = 0
    chi_phi_tot_nhat = float('inf')
    chu_trinh_tot_nhat = []
    
    ma_tran_chi_phi_np = np.array(ma_tran_chi_phi, dtype=float)

    def giam_ma_tran(matrix):
        chi_phi_giam = 0
        min_hang = matrix.min(axis=1, keepdims=True)
        min_hang[min_hang == np.inf] = 0
        matrix -= min_hang
        chi_phi_giam += min_hang.sum()

        min_cot = matrix.min(axis=0, keepdims=True)
        min_cot[min_cot == np.inf] = 0
        matrix -= min_cot
        chi_phi_giam += min_cot.sum()
        
        return matrix, chi_phi_giam

    ma_tran_ban_dau, chi_phi_giam_ban_dau = giam_ma_tran(ma_tran_chi_phi_np.copy())
    hang_doi_uu_tien = [(chi_phi_giam_ban_dau, 0, [0], ma_tran_ban_dau.tolist())]

    while hang_doi_uu_tien:
        so_nut_mo_rong += 1
        can_duoi, level, chu_trinh, ma_tran_list = heapq.heappop(hang_doi_uu_tien)
        ma_tran = np.array(ma_tran_list, dtype=float) # Convert list back to numpy array

        if can_duoi >= chi_phi_tot_nhat:
            continue

        if level == so_thanh_pho - 1:
            thanh_pho_cuoi = chu_trinh[-1]
            thanh_pho_dau = chu_trinh[0]
            if ma_tran_chi_phi_np[thanh_pho_cuoi, thanh_pho_dau] != float('inf'):
                chi_phi_hien_tai = can_duoi + ma_tran_chi_phi_np[thanh_pho_cuoi, thanh_pho_dau]
                if chi_phi_hien_tai < chi_phi_tot_nhat:
                    chi_phi_tot_nhat = chi_phi_hien_tai
                    chu_trinh_tot_nhat = chu_trinh + [thanh_pho_dau]
            continue

        hinh_phat_lon_nhat = -1
        nhanh_i, nhanh_j = -1, -1
        
        zero_cells = np.argwhere(ma_tran == 0)
        for i, j in zero_cells:
            row_min = ma_tran[i].copy()
            row_min[j] = np.inf
            col_min = ma_tran[:, j].copy()
            col_min[i] = np.inf
            
            penalty = np.min(row_min) + np.min(col_min)
            if penalty > hinh_phat_lon_nhat:
                hinh_phat_lon_nhat = penalty
                nhanh_i, nhanh_j = i, j
        
        if nhanh_i == -1 or nhanh_j == -1: continue

        # Nhánh 1: Include (thêm cạnh i -> j)
        ma_tran_moi_them = ma_tran.copy()
        ma_tran_moi_them[nhanh_i, :] = np.inf
        ma_tran_moi_them[:, nhanh_j] = np.inf
        
        if nhanh_j in chu_trinh:
             ma_tran_moi_them[nhanh_j, chu_trinh[0]] = np.inf
        
        chi_phi_nhanh_them = can_duoi + ma_tran[nhanh_i, nhanh_j]
        ma_tran_giam_lai_them, chi_phi_giam_lai_them = giam_ma_tran(ma_tran_moi_them)
        can_duoi_moi_them = chi_phi_nhanh_them + chi_phi_giam_lai_them
        chu_trinh_moi_them = chu_trinh + [nhanh_j]
        
        if can_duoi_moi_them < chi_phi_tot_nhat:
            heapq.heappush(hang_doi_uu_tien, (can_duoi_moi_them, level + 1, chu_trinh_moi_them, ma_tran_giam_lai_them.tolist()))

        # Nhánh 2: Exclude (loại bỏ cạnh i -> j)
        ma_tran_moi_loai_bo = ma_tran.copy()
        ma_tran_moi_loai_bo[nhanh_i, nhanh_j] = np.inf
        
        ma_tran_giam_lai_loai_bo, chi_phi_giam_lai_loai_bo = giam_ma_tran(ma_tran_moi_loai_bo)
        can_duoi_moi_loai_bo = can_duoi + chi_phi_giam_lai_loai_bo

        if can_duoi_moi_loai_bo < chi_phi_tot_nhat:
            heapq.heappush(hang_doi_uu_tien, (can_duoi_moi_loai_bo, level, chu_trinh, ma_tran_giam_lai_loai_bo.tolist()))

    thoi_gian_ket_thuc = time.time()
    return chi_phi_tot_nhat, chu_trinh_tot_nhat, so_nut_mo_rong, thoi_gian_ket_thuc - thoi_gian_bat_dau

if __name__ == "__main__":
    print("--- Bài toán Người du lịch (TSP) ---")

    so_thanh_pho = int(input("Nhập số lượng thành phố: "))
    ma_tran_chi_phi = []
    
    print("Nhập ma trận chi phí (nhập 'inf' cho vô cùng):")
    for i in range(so_thanh_pho):
        row_input = input(f"  Nhập hàng {i+1} (cách nhau bằng dấu cách): ").split()
        row = []
        for val_str in row_input:
            if val_str.lower() == 'inf':
                row.append(float('inf'))
            else:
                try:
                    row.append(float(val_str))
                except ValueError:
                    print("Giá trị không hợp lệ, vui lòng nhập lại số hoặc 'inf'.")
                    exit()
        ma_tran_chi_phi.append(row)

    chi_phi_tot_nhat, chu_trinh, so_nut, thoi_gian = nguoi_du_lich_tsp_dung_thu_vien(ma_tran_chi_phi)
    
    print("\nKết quả:")
    print(f"Chi phí tốt nhất: {chi_phi_tot_nhat}")
    print(f"Chu trình: {chu_trinh}")
    print(f"Số nút đã mở rộng: {so_nut}")
    print(f"Thời gian chạy: {thoi_gian:.6f} giây")
    
