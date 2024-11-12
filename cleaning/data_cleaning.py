import pandas as pd

def handle_missing_values(data, fill_value=-1, column_fill_values=None):
    """
    Xử lý giá trị bị thiếu trong dữ liệu bằng cách điền giá trị thay thế.

    Parameters:
        data (pd.DataFrame): Dữ liệu cần xử lý.
        fill_value: Giá trị mặc định để thay thế cho tất cả các ô bị thiếu (nếu column_fill_values không được cung cấp).
        column_fill_values (dict): Từ điển với key là tên cột và value là giá trị thay thế cho cột đó.
    
    Returns:
        pd.DataFrame: Dữ liệu sau khi đã thay thế các giá trị thiếu.
    """
    if column_fill_values:
        # Điền các giá trị khác nhau cho từng cột
        return data.fillna(column_fill_values)
    else:
        # Điền cùng một giá trị cho tất cả các ô bị thiếu
        return data.fillna(fill_value)


# Hàm 2: Chuẩn hóa văn bản
def normalize_text(data, columns):
    """
    Chuẩn hóa văn bản trong các cột được chỉ định bằng cách loại bỏ khoảng trắng
    và chuyển thành chữ thường.

    Parameters:
        data (pd.DataFrame): Dữ liệu cần xử lý.
        columns (list): Danh sách các cột cần chuẩn hóa văn bản.
    """
    for col in columns:
        data[col] = data[col].str.strip().str.lower()
    return data

# Hàm 3: Kiểm tra và chuyển đổi kiểu dữ liệu
def convert_data_types(data, columns_types):
    """
    Chuyển đổi kiểu dữ liệu của các cột trong DataFrame.

    Parameters:
        data (pd.DataFrame): Dữ liệu cần xử lý.
        columns_types (dict): Dictionary với key là tên cột và value là kiểu dữ liệu muốn chuyển.
    """
    for column, dtype in columns_types.items():
        data[column] = data[column].astype(dtype)
    return data
