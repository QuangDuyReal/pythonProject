from storage.data_storage import read_data

# Hàm tìm kiếm dữ liệu
def search_data(area_name, page_size=60):
    """
    Tìm kiếm dữ liệu dựa trên tên quốc gia hoặc khu vực và hiển thị kết quả theo từng trang.

    Args:
        area_name (str): Tên quốc gia hoặc khu vực cần tìm kiếm.
        page_size (int, optional): Số lượng kết quả hiển thị trên mỗi trang. 
                                   Mặc định là 60.

    Returns:
        None: Kết quả tìm kiếm được hiển thị trực tiếp ra màn hình.

    Chức năng:
        - Lọc dữ liệu theo tên quốc gia hoặc khu vực (không phân biệt chữ hoa/thường).
        - Tính toán số trang cần thiết để hiển thị kết quả.
        - Hỗ trợ người dùng điều hướng giữa các trang hoặc thoát tìm kiếm.
    """
    data = read_data()
    result = data[data['Area'].str.contains(area_name, case=False, na=False)][['Area', 'Months', 'Year', 'Value']]

    if result.empty:
        print(f"Không tìm thấy kết quả cho quốc gia '{area_name}'")
        return
    total_records = len(result)
    total_pages = (total_records + page_size - 1) // page_size

    print(f"Đã tìm thấy {total_records} kết quả cho quốc gia '{area_name}'. Có {total_pages} trang.")
    while True:
        try:
            page_num = int(input(f"Nhập số trang (1-{total_pages}, hoặc 0 để thoát): "))
            if page_num == 0:
                print("Thoát tìm kiếm.")
                break
            elif 1 <= page_num <= total_pages:
                # Tính toán chỉ số bắt đầu và kết thúc của bản ghi cho trang hiện tại
                start_idx = (page_num - 1) * page_size
                end_idx = min(start_idx + page_size, total_records)

                # Hiển thị kết quả trong trang hiện tại, chỉ các cột được chọn
                print(f"\nHiển thị trang {page_num}/{total_pages}")
                print(result.iloc[start_idx:end_idx].to_string(index=False))

            else:
                print(f"Vui lòng nhập số trang trong khoảng 1-{total_pages} hoặc 0 để thoát.")
        except ValueError:
            print("Vui lòng nhập số hợp lệ.")
        