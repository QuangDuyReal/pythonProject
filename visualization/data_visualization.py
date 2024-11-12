# data_visualization.py

import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
import numpy as np
from sklearn.linear_model import LinearRegression

def plot_line(data, x_column, y_column, title="Line Plot", xlabel="X-axis", ylabel="Y-axis"):
    """
    Vẽ biểu đồ đường cho dữ liệu.

    Parameters:
        data (pd.DataFrame): Dữ liệu cần vẽ.
        x_column (str): Tên cột để làm trục X.
        y_column (str): Tên cột để làm trục Y.
        title (str): Tiêu đề của biểu đồ.
        xlabel (str): Nhãn của trục X.
        ylabel (str): Nhãn của trục Y.
    """
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x=x_column, y=y_column)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

def plot_bar(data, x_column, y_column, title="Bar Plot", xlabel="X-axis", ylabel="Y-axis"):
    """
    Vẽ biểu đồ cột cho dữ liệu.

    Parameters:
        data (pd.DataFrame): Dữ liệu cần vẽ.
        x_column (str): Tên cột để làm trục X.
        y_column (str): Tên cột để làm trục Y.
        title (str): Tiêu đề của biểu đồ.
        xlabel (str): Nhãn của trục X.
        ylabel (str): Nhãn của trục Y.
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(data=data, x=x_column, y=y_column)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

def plot_scatter(data, x_column, y_column, title="Scatter Plot", xlabel="X-axis", ylabel="Y-axis"):
    """
    Vẽ biểu đồ phân tán cho dữ liệu.

    Parameters:
        data (pd.DataFrame): Dữ liệu cần vẽ.
        x_column (str): Tên cột để làm trục X.
        y_column (str): Tên cột để làm trục Y.
        title (str): Tiêu đề của biểu đồ.
        xlabel (str): Nhãn của trục X.
        ylabel (str): Nhãn của trục Y.
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x=x_column, y=y_column)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

def plot_box(data, y_column, title="Box Plot", ylabel="Y-axis"):
    """
    Vẽ biểu đồ hộp cho dữ liệu.

    Parameters:
        data (pd.DataFrame): Dữ liệu cần vẽ.
        y_column (str): Tên cột để làm trục Y.
        title (str): Tiêu đề của biểu đồ.
        ylabel (str): Nhãn của trục Y.
    """
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data, y=y_column)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()


def plot_line_with_margins(data, x_column, y_column, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    
    # Vẽ biểu đồ đường
    plt.plot(data[x_column], data[y_column], marker='o', color='b', linestyle='-', linewidth=2)
    
    # Thêm tiêu đề, nhãn trục và lưới
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)  # Thêm lưới cho biểu đồ

    # Thêm lề cho biểu đồ
    plt.margins(x=0.05, y=0.1)

    # Định dạng chia độ trục X theo các năm
    years = data[x_column].unique()
    plt.xticks(years, rotation=45)

    # Hiển thị biểu đồ
    plt.tight_layout()
    plt.show()

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