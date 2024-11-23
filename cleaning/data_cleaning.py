def handle_missing_values(data, fill_value=0, column_fill_values=None):
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
