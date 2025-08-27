import heapq
import time

def cai_tui_01_dung_thu_vien(W_suc_chua, danh_sach_trong_luong, danh_sach_gia_tri):
    thoi_gian_bat_dau = time.time()
    so_vat_pham = len(danh_sach_trong_luong)
    so_nut_mo_rong = 0
    gia_tri_tot_nhat = 0
    lua_chon_tot_nhat = []

    vat_phams = sorted(zip(danh_sach_gia_tri, danh_sach_trong_luong, range(so_vat_pham)), key=lambda x: x[0] / x[1], reverse=True)

    def tinh_can_tren(level, trong_luong_hien_tai, gia_tri_hien_tai):
        can_tren = gia_tri_hien_tai
        trong_luong_tam_thoi = trong_luong_hien_tai
        for i in range(level, so_vat_pham):
            if trong_luong_tam_thoi + vat_phams[i][1] <= W_suc_chua:
                trong_luong_tam_thoi += vat_phams[i][1]
                can_tren += vat_phams[i][0]
            else:
                trong_luong_con_lai = W_suc_chua - trong_luong_tam_thoi
                can_tren += (vat_phams[i][0] / vat_phams[i][1]) * trong_luong_con_lai
                break
        return can_tren

    hang_doi_uu_tien = [(-tinh_can_tren(0, 0, 0), 0, 0, 0, [])]

    while hang_doi_uu_tien:
        so_nut_mo_rong += 1
        can_tren_am, level, gia_tri, trong_luong, da_chon = heapq.heappop(hang_doi_uu_tien)
        can_tren = -can_tren_am

        if can_tren <= gia_tri_tot_nhat:
            continue

        if level == so_vat_pham:
            if gia_tri > gia_tri_tot_nhat:
                gia_tri_tot_nhat = gia_tri
                lua_chon_tot_nhat = da_chon
            continue

        gia_tri_mon_do, trong_luong_mon_do, chi_so_goc = vat_phams[level]
        
        if trong_luong + trong_luong_mon_do <= W_suc_chua:
            trong_luong_moi = trong_luong + trong_luong_mon_do
            gia_tri_moi = gia_tri + gia_tri_mon_do
            lua_chon_moi = da_chon + [chi_so_goc]
            
            if gia_tri_moi > gia_tri_tot_nhat:
                gia_tri_tot_nhat = gia_tri_moi
                lua_chon_tot_nhat = lua_chon_moi

            can_tren_moi = tinh_can_tren(level + 1, trong_luong_moi, gia_tri_moi)
            heapq.heappush(hang_doi_uu_tien, (-can_tren_moi, level + 1, gia_tri_moi, trong_luong_moi, lua_chon_moi))

        can_tren_moi = tinh_can_tren(level + 1, trong_luong, gia_tri)
        if can_tren_moi > gia_tri_tot_nhat:
            heapq.heappush(hang_doi_uu_tien, (-can_tren_moi, level + 1, gia_tri, trong_luong, da_chon))

    thoi_gian_ket_thuc = time.time()
    return gia_tri_tot_nhat, lua_chon_tot_nhat, so_nut_mo_rong, thoi_gian_ket_thuc - thoi_gian_bat_dau

if __name__ == "__main__":
    print("--- Bài toán Cái túi 0/1 ---")
    
    W_suc_chua = int(input("Nhập sức chứa của cái túi (W): "))
    so_vat_pham = int(input("Nhập số lượng vật phẩm: "))
    
    danh_sach_trong_luong = []
    danh_sach_gia_tri = []
    
    print("Nhập trọng lượng và giá trị cho từng vật phẩm:")
    for i in range(so_vat_pham):
        try:
            trong_luong = int(input(f"  Vật phẩm {i+1} - Trọng lượng: "))
            gia_tri = int(input(f"  Vật phẩm {i+1} - Giá trị: "))
            danh_sach_trong_luong.append(trong_luong)
            danh_sach_gia_tri.append(gia_tri)
        except ValueError:
            print("Giá trị không hợp lệ, vui lòng nhập lại số nguyên.")
            exit()
            
    gia_tri_tot_nhat, vat_pham_chon, so_nut, thoi_gian = cai_tui_01_dung_thu_vien(W_suc_chua, danh_sach_trong_luong, danh_sach_gia_tri)

    print("\nKết quả:")
    print(f"Giá trị tốt nhất: {gia_tri_tot_nhat}")
    print(f"Các vật phẩm đã chọn (chỉ số gốc): {vat_pham_chon}")
    print(f"Số nút đã mở rộng: {so_nut}")
    print(f"Thời gian chạy: {thoi_gian:.6f} giây")
