from cleaning.data_cleaning import handle_missing_values
import pandas as pd

file_path = "D:/UTE/Nhập môn lập trình Python/Myself/data/biendoikhihau.csv"

# Hàm đọc dữ liệu từ file
def read_data():
    data = pd.read_csv(file_path, low_memory = False)
    data = handle_missing_values(data, fill_value=0) #làm sạch dữ liệu
    print("Dữ liệu đã được tải lên")
    return data
# Hàm lưu dữ liệu trở lại file
def save_data(data):
    data.to_csv(file_path, index=False)
    print("Dữ liệu đã được lưu lại.")

# Thêm bản ghi mới
def create_record(dCode, Domain, AreaCode, Area, eCode, Element, monthsCode, Months, yearsCode, Year, Unit, Value, Flag, FlagDes):
    """
    Thêm một bản ghi mới vào tệp dữ liệu CSV.

    Args:
        dCode (str): Mã miền.
        Domain (str): Tên miền.
        AreaCode (str): Mã khu vực (M49).
        Area (str): Tên khu vực/quốc gia.
        eCode (str): Mã yếu tố.
        Element (str): Yếu tố (ví dụ: thay đổi nhiệt độ).
        monthsCode (str): Mã tháng.
        Months (str): Tên tháng.
        yearsCode (str): Mã năm.
        Year (str): Năm.
        Unit (str): Đơn vị đo lường.
        Value (float): Giá trị đo lường.
        Flag (str): Cờ trạng thái.
        FlagDes (str): Mô tả cờ trạng thái.

    Returns:
        None
    """
    data = read_data()
    new_record = {
        'Domain Code': dCode,
        'Domain': Domain,
        'Area Code (M49)': AreaCode,
        'Area': Area,
        'Element Code': eCode,
        'Element': Element,
        'Months Code': monthsCode,
        'Months': Months,
        'Year Code': yearsCode,
        'Year': Year,
        'Unit': Unit,
        'Value': Value,
        'Flag': Flag,
        'Flag Description': FlagDes
    }
    # Sử dụng .loc[] để thêm bản ghi mới vào cuối DataFrame
    data.loc[len(data)] = new_record
    save_data(data)
    print("Đã thêm bản ghi mới!")

# Hiển thị tất cả các bản ghi
def read_all_record():
    """
    Đọc và hiển thị tất cả các bản ghi trong tệp CSV.

    Yêu cầu người dùng chọn cột hiển thị và thực hiện phân trang dữ liệu.

    Returns:
        None
    """
    data = read_data()
    # Hỏi người dùng chọn các cột muốn xem
    print("Các cột có sẵn:", list(data.columns))
    # Lọc cột nếu cần
    selected_columns = input("Nhập tên các cột muốn hiển thị, cách nhau bởi dấu phẩy (hoặc để trống để hiển thị tất cả): ")
    selected_columns = [col.strip() for col in selected_columns.split(",") if col.strip()] or list(data.columns)
    data = data[selected_columns]
    
    # Gọi hàm phân trang với số dòng mỗi trang là 60
    paginate_data(data, rows_per_page=60)

# Hàm phân trang
def paginate_data(data, rows_per_page=60):
    """
    Thực hiện phân trang dữ liệu, hiển thị một số lượng hàng nhất định trên mỗi trang.

    Args:
        data (DataFrame): Dữ liệu cần phân trang.
        rows_per_page (int, optional): Số lượng hàng hiển thị trên mỗi trang. 
                                       Mặc định là 60.

    Returns:
        None: Kết quả được in trực tiếp ra màn hình theo từng trang.
    
    Lưu ý:
        Người dùng có thể nhập số trang để điều hướng qua các trang hoặc nhập 0 để thoát.
    """
    pd.set_option('display.max_columns', None)  # Hiển thị tất cả các cột
    pd.set_option('display.width', 1000)  # Đặt chiều rộng cho dễ đọc
    
    total_rows = len(data)
    total_pages = (total_rows + rows_per_page - 1) // rows_per_page  # Tính tổng số trang
    
    print(f"Tổng số trang: {total_pages}")
    
    while True:
        try:
            page_number = int(input(f"Nhập số trang (1 - {total_pages}) hoặc 0 để thoát: "))
            if page_number == 0:
                print("Đã thoát khỏi phân trang.")
                break
            elif 1 <= page_number <= total_pages:
                # Tính chỉ số hàng đầu và hàng cuối của trang
                start_row = (page_number - 1) * rows_per_page + 1
                end_row = min(start_row + rows_per_page, total_rows)
                
                # Hiển thị dữ liệu của trang
                print(f"\nTrang {page_number} (dòng {start_row} đến {end_row - 1}):")
                print(data.iloc[start_row:end_row])
            else:
                print(f"Vui lòng nhập số trang trong khoảng từ 1 đến {total_pages}.")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")
    
    # Khôi phục cài đặt mặc định của Pandas
    pd.reset_option('display.max_columns')
    pd.reset_option('display.width')

def update_record(record_id, column_name, new_value):
    """
    Cập nhật một giá trị trong tệp CSV dựa trên chỉ số bản ghi và tên cột.

    Args:
        record_id (int): Chỉ số của bản ghi cần cập nhật.
        column_name (str): Tên cột cần cập nhật.
        new_value (str): Giá trị mới để thay thế.

    Returns:
        None
    """
    # Đọc dữ liệu từ file CSV
    data = read_data()
    
    # Kiểm tra nếu ID hợp lệ trong phạm vi của data
    if 0 <= record_id < len(data):
        # Cập nhật giá trị mới cho cột cụ thể của bản ghi
        data.at[record_id, column_name] = new_value
        # Lưu dữ liệu sau khi cập nhật
        save_data(data)
        print(f"Đã cập nhật bản ghi {record_id}, cột '{column_name}' với giá trị mới: {new_value}")
    else:
        print("ID bản ghi không tồn tại. Vui lòng thử lại với ID hợp lệ.")


# Xóa bản ghi (dựa trên index của bản ghi)
def delete_record(record_id):
    data = read_data()
    if 0 <= record_id < len(data):
        data = data.drop(record_id)
        save_data(data)
        print(f"Đã xóa bản ghi {record_id}")
    else:
        print("Bản ghi không tồn tại")
