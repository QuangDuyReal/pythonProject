from storage.data_storage import(
    create_record,
    read_all_record,
    update_record,
    delete_record)
from visualization.data_visualization import plot_option
from processing.data_processing import search_data
#Thư viện để làm đẹp giao diện console
from rich.console import Console

def main_menu():
    console = Console()
    while True:
        console.print("\n[bold magenta]--- Chương trình Theo dõi Biến đổi Khí hậu ---[/bold magenta]")
        print("1. Thêm bản ghi mới")
        print("2. Hiển thị tất cả bản ghi")
        print("3. Cập nhật bản ghi")
        print("4. Xóa bản ghi")
        print("5. Vẽ biểu đồ thay đổi nhiệt độ theo thời gian")
        print("6. Tìm kiếm dữ liệu")
        print("7. Thoát")

        choice = input("Nhập lựa chọn của bạn (1-7): ")
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
            area_name = input("Nhập tên quốc gia để tìm kiếm: ")
            search_data(area_name)
        elif choice == '7':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 7.")

if __name__ == "__main__":
    main_menu()
