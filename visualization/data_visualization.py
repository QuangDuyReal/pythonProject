import matplotlib.pyplot as plt
import numpy as np
from storage.data_storage import read_data
from sklearn.linear_model import LinearRegression

def plot_all_countries_temperature_change(data, title, xlabel, ylabel):
    plt.figure(figsize=(14, 8))

    # Lọc dữ liệu chỉ cho "Temperature change"
    temp_data = data[data['Element'] == 'Temperature change']
    
    # Vẽ mỗi quốc gia trên một đường riêng, không hiển thị chú thích từng quốc gia
    for country in temp_data['Area'].unique():
        country_data = temp_data[temp_data['Area'] == country]
        plt.plot(country_data['Year'], country_data['Value'], linewidth=1)

    # Thiết lập tiêu đề, nhãn trục và lưới
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)  # Thêm lưới cho biểu đồ
    
    # Dự đoán xu hướng tương lai
    predict_temperature_trend(temp_data)
    
    # Hiển thị biểu đồ
    plt.tight_layout()
    plt.show()

def predict_temperature_trend(data):
    # Tính nhiệt độ trung bình theo năm
    years = data['Year'].unique()
    avg_temp_by_year = data.groupby('Year')['Value'].mean()

    # Hồi quy tuyến tính để dự đoán xu hướng
    X = np.array(years).reshape(-1, 1)
    y = avg_temp_by_year.values

    model = LinearRegression()
    model.fit(X, y)

    # Dự đoán cho năm hiện tại đến năm trong tương lai
    future_years = np.array(range(years.min(), years.max() + 20)).reshape(-1, 1)
    future_temps = model.predict(future_years)

    # Vẽ đường hồi quy
    plt.plot(future_years, future_temps, color='red', linestyle='--', label='Dự đoán xu hướng nhiệt độ')
    plt.legend()
    plt.grid(True)  # Thêm lưới cho biểu đồ dự đoán

def predict_temperature_trend(data, country_name=None):
    if country_name:
        data = data[(data['Area'].str.lower() == country_name.lower()) & (data['Element'] == 'Temperature change')]
        if data.empty:
            print(f"Không có dữ liệu cho quốc gia '{country_name}'.")
            return
        title = f"Dự đoán xu hướng nhiệt độ của {country_name.capitalize()} theo thời gian"
    else:
        data = data[data['Element'] == 'Temperature change']
        title = "Dự đoán xu hướng nhiệt độ trung bình toàn cầu theo thời gian"

    # Tính nhiệt độ trung bình theo năm cho dữ liệu đã chọn
    years = data['Year'].unique()
    avg_temp_by_year = data.groupby('Year')['Value'].mean()

    # Hồi quy tuyến tính để dự đoán xu hướng
    X = np.array(years).reshape(-1, 1)
    y = avg_temp_by_year.values

    model = LinearRegression()
    model.fit(X, y)

    # Dự đoán cho năm hiện tại đến một số năm trong tương lai
    future_years = np.array(range(years.min(), years.max() + 20)).reshape(-1, 1)
    future_temps = model.predict(future_years)

    # Vẽ biểu đồ
    plt.plot(years, avg_temp_by_year, label="Nhiệt độ trung bình (thực tế)", color="blue")
    plt.plot(future_years, future_temps, color='red', linestyle='--', label='Dự đoán xu hướng nhiệt độ')
    plt.xlabel("Năm")
    plt.ylabel("Nhiệt độ trung bình")
    plt.title(title)
    plt.legend()
    plt.grid(True)  # Thêm lưới cho biểu đồ dự đoán
    plt.show()

def plot_option():
    data = read_data()
    
    country = input("Nhập tên quốc gia để vẽ biểu đồ thay đổi nhiệt độ (hoặc nhấn Enter để vẽ cho tất cả quốc gia): ").strip()
    
    if country:
        predict_temperature_trend(data, country_name=country)
    else:
        plot_all_countries_temperature_change(
            data,
            title="Biểu đồ thay đổi nhiệt độ theo thời gian cho tất cả các quốc gia",
            xlabel="Năm",
            ylabel="Thay đổi nhiệt độ"
        )
