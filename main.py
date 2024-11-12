import tkinter as tk
from tkinter import messagebox
from storage.data_storage import read_data, create_record, read_all_record, update_record, delete_record
from cleaning.data_cleaning import normalize_text, handle_missing_values
from visualization.data_visualization import plot_line, plot_bar, plot_scatter, plot_box, plot_line_with_margins, plot_all_countries_temperature_change

def main():
    # Bước 1: Đọc và làm sạch dữ liệu
    data = read_data()
    data = normalize_text(data, columns=["Domain", "Area"])
    data = handle_missing_values(data, fill_value=0)
    data['Area'] = data['Area'].str.lower()
    
    # Menu chính
    while True:
        print("\n--- Menu chính ---")
        print("1. Thêm bản ghi mới")
        print("2. Hiển thị tất cả bản ghi")
        print("3. Cập nhật bản ghi")
        print("4. Xóa bản ghi")
        print("5. Vẽ biểu đồ tùy chọn")
        print("6. Vẽ biểu đồ thay đổi nhiệt độ của một quốc gia theo thời gian")
        print("7. Vẽ biểu đồ thay đổi nhiệt độ theo thời gian cho tất cả quốc gia")
        print("8. Thoát")

        choice = input("Nhập lựa chọn của bạn (1-8): ")
        
        if choice == "1":
            dCode = input("Nhập mã miền: ")
            Domain = input("Nhập miền: ")
            AreaCode = input("Nhập mã vùng: ")
            Area = input("Nhập vùng: ")
            eCode = input("Nhập mã yếu tố: ")
            Element = input("Nhập yếu tố: ")
            monthsCode = input("Nhập mã tháng: ")
            Months = input("Nhập tháng: ")
            yearsCode = input("Nhập mã năm: ")
            Year = int(input("Nhập năm: "))
            Unit = input("Nhập đơn vị: ")
            Value = float(input("Nhập giá trị: "))
            Flag = input("Nhập cờ: ")
            FlagDes = input("Nhập mô tả cờ: ")
            
            create_record(dCode, Domain, AreaCode, Area, eCode, Element, monthsCode, Months, yearsCode, Year, Unit, Value, Flag, FlagDes)
        
        elif choice == "2":
            read_all_record()
        
        elif choice == "3":
            update_record()
        
        elif choice == "4":
            delete_record()
        
        elif choice == "5":
            # Menu chọn loại biểu đồ
            print("\n--- Chọn loại biểu đồ ---")
            print("1. Biểu đồ đường")
            print("2. Biểu đồ cột")
            print("3. Biểu đồ phân tán")
            print("4. Biểu đồ hộp")
            
            chart_choice = input("Nhập lựa chọn của bạn (1-4): ")
            if chart_choice in ["1", "2", "3", "4"]:
                # Xác định cột X và Y cho biểu đồ
                x_column = input("Nhập tên cột cho trục X: ")
                y_column = input("Nhập tên cột cho trục Y: ")
                title = input("Nhập tiêu đề biểu đồ: ")
                xlabel = input("Nhập nhãn cho trục X: ")
                ylabel = input("Nhập nhãn cho trục Y: ")

                if chart_choice == "1":
                    plot_line(data, x_column=x_column, y_column=y_column, title=title, xlabel=xlabel, ylabel=ylabel)
                elif chart_choice == "2":
                    plot_bar(data, x_column=x_column, y_column=y_column, title=title, xlabel=xlabel, ylabel=ylabel)
                elif chart_choice == "3":
                    plot_scatter(data, x_column=x_column, y_column=y_column, title=title, xlabel=xlabel, ylabel=ylabel)
                elif chart_choice == "4":
                    plot_box(data, y_column=y_column, title=title, ylabel=ylabel)
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4.")
        
        if choice == "6":
            # Vẽ biểu đồ thay đổi nhiệt độ theo thời gian của một quốc gia
            country = input("Nhập tên quốc gia: ").lower()  # Chuyển tên quốc gia nhập vào về chữ thường
            country_data = data[data['Area'].str.contains(country) & (data['Element'] == 'Temperature change')]

            if country_data.empty:
                print(f"Không có dữ liệu nhiệt độ cho quốc gia '{country}'.")
            else:
                title = f"Biểu đồ thay đổi nhiệt độ của {country.capitalize()} theo thời gian"
                plot_line_with_margins(country_data, x_column="Year", y_column="Value", title=title, xlabel="Năm", ylabel="Nhiệt độ")

        elif choice == "7":
            # Vẽ biểu đồ thay đổi nhiệt độ theo thời gian cho tất cả quốc gia
            title = "Biểu đồ thay đổi nhiệt độ theo thời gian cho tất cả các quốc gia"
            plot_all_countries_temperature_change(data, title=title, xlabel="Năm", ylabel="Nhiệt độ")

        elif choice == "8":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 8.")

if __name__ == "__main__":
    main()
