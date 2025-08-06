def kiemtra_nuocsoi(nhiet_do):
    if nhiet_do < 100 and nhiet_do >= 50:
        return "Nước chưa sôi"
    elif nhiet_do < 50:
        return "Nước lạnh"
    else:
        return "Nước đã sôi"

def kiemtra(nhiet_do):
    return "Nước đã sôi" if nhiet_do > 100 else("Nước chưa sôi" if nhiet_do > 50 else "Nước lạnh")

if __name__ == '__main__':
    print(kiemtra_nuocsoi(-10))
    
# Với giá trị -10 thì hảm trả về kết quả nước lạnh
# Cách hoạt động khi nhận giá trị -10 sẽ kiểm tra điều điều kiện đầu tiên do không đúng vì -10 không < 100 và >= 50
# Kiểm tra tới elif < 50 điều kiện đúng trả về nước lạnh
    