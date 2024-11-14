import tkinter as tk
from tkinter import messagebox
from storage.data_storage import(
    read_data,
    create_record,
    read_all_record,
    update_record,
    delete_record)
from cleaning.data_cleaning import(
    normalize_text,
    handle_missing_values)
from visualization.data_visualization import(
    plot_line,
    plot_bar,
    plot_scatter,
    plot_box,
    plot_line_with_margins,
    plot_all_countries_temperature_change)

def main_menu():
    while True:
        print("\n--- Chương trình Theo dõi Biến đổi Khí hậu ---")
        print("1. Thêm bản ghi mới")
        print("2. Hiển thị tất cả bản ghi")
        print("3. Cập nhật bản ghi")
        print("4. Xóa bản ghi")
        print("5. Vẽ biểu đồ thay đổi nhiệt độ theo thời gian")
        print("6. Thoát")

        choice = input("Nhập lựa chọn của bạn (1-6): ")

        if choice == '1':
            dCode = input("Nhập Domain Code: ")
            Domain = input("Nhập Domain: ")
            AreaCode = input("Nhập Area Code: ")
            Area = input("Nhập Area: ")
            eCode = input("Nhập Element Code: ")
            Element = input("Nhập Element: ")
            monthsCode = input("Nhập Months Code: ")
            Months = input("Nhập Months: ")
            yearsCode = input("Nhập Year Code: ")
            Year = input("Nhập Year: ")
            Unit = input("Nhập Unit: ")
            Value = input("Nhập Value: ")
            Flag = input("Nhập Flag: ")
            FlagDes = input("Nhập FlagDes: ")
            create_record(dCode, Domain, AreaCode, Area, eCode, Element, monthsCode, Months, yearsCode, Year, Unit, Value, Flag, FlagDes)
        
        elif choice == '2':
            read_all_record()
        
        elif choice == '3':
            record_id = int(input("Nhập ID bản ghi cần cập nhật: "))
            column = input("Nhập tên cột cần cập nhật: ")
            new_value = input("Nhập giá trị mới: ")
            update_record(record_id, column, new_value)
        
        elif choice == '4':
            record_id = int(input("Nhập ID bản ghi cần xóa: "))
            delete_record(record_id)
        
        elif choice == '5':
            plot_option()
        elif choice == '6':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 6.")

def plot_option():
    data = read_data()

    # Hỏi người dùng tên quốc gia muốn vẽ biểu đồ
    country = input("Nhập tên quốc gia để vẽ biểu đồ thay đổi nhiệt độ (hoặc nhấn Enter để vẽ cho tất cả quốc gia): ").strip()
    
    # Chọn loại biểu đồ
    print("\nChọn loại biểu đồ:")
    print("1. Biểu đồ đường")
    print("2. Biểu đồ cột")
    print("3. Biểu đồ phân tán")
    chart_type = input("Nhập lựa chọn của bạn (1-3): ")

    # Kiểm tra quốc gia cụ thể
    if country:
        # Lọc dữ liệu theo quốc gia và 'Temperature change'
        country_data = data[(data['Area'].str.lower() == country.lower()) & (data['Element'] == 'Temperature change')]
        
        if country_data.empty:
            print(f"Không có dữ liệu cho quốc gia '{country}'.")
        else:
            # Vẽ biểu đồ theo loại được chọn cho quốc gia đã chọn
            if chart_type == '1':
                plot_line_with_margins(
                    country_data,
                    x_column="Year",
                    y_column="Value",
                    title=f"Biểu đồ thay đổi nhiệt độ của {country.capitalize()} theo thời gian",
                    xlabel="Năm",
                    ylabel="Thay đổi nhiệt độ"
                )
            elif chart_type == '2':
                plot_bar(
                    country_data,
                    x_column="Year",
                    y_column="Value",
                    title=f"Biểu đồ cột thay đổi nhiệt độ của {country.capitalize()} theo thời gian",
                    xlabel="Năm",
                    ylabel="Thay đổi nhiệt độ"
                )
            elif chart_type == '3':
                plot_scatter(
                    country_data,
                    x_column="Year",
                    y_column="Value",
                    title=f"Biểu đồ phân tán thay đổi nhiệt độ của {country.capitalize()} theo thời gian",
                    xlabel="Năm",
                    ylabel="Thay đổi nhiệt độ"
                )
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn 1, 2 hoặc 3.")
    else:
        # Nếu không nhập quốc gia, vẽ biểu đồ cho tất cả các quốc gia
        plot_all_countries_temperature_change(
            data,
            title="Biểu đồ thay đổi nhiệt độ theo thời gian cho tất cả các quốc gia",
            xlabel="Năm",
            ylabel="Thay đổi nhiệt độ"
        )

if __name__ == "__main__":
    main_menu()
