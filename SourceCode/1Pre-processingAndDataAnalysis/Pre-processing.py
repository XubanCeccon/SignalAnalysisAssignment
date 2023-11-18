# The purpose of this code is to know if the data is pre-processed or not.
import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path, num_sensors):
    column_names = [f"sensor_{i+1}" for i in range(num_sensors)] + ['label']
    try:
        return pd.read_csv(file_path, header=None, names=column_names)
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None

def get_min_max_values(df):
    min_values = df.iloc[:, :-1].min().min()
    max_values = df.iloc[:, :-1].max().max()
    return min_values, max_values

def check_missing_values(df):
    return df.isnull().sum().sum()

def check_labels(df):
    return df['label'].isnull().sum()

def check_data_format(df, num_sensors):
    return len(df.columns) == num_sensors + 1

def plot_sensor_values(min_values, max_values, num_sensors, file_path):
    sensors = [f"sensor_{i+1}" for i in range(num_sensors)]
    plt.figure(figsize=(10, 6))
    for i in range(num_sensors):
        plt.plot([sensors[i], sensors[i]], [min_values, max_values], marker='o')
    plt.title(f'Min and Max Sensor Values for {file_path}')
    plt.xlabel('Sensor')
    plt.ylabel('Value')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()

def process_database(file_path, num_sensors):
    print(f"\nProcessing {file_path}")
    df = load_data(file_path, num_sensors)

    if df is None:
        return

    num_rows = len(df)
    print(f"Total rows: {num_rows}")
    missing_values = check_missing_values(df)
    print(f"Missing values: {missing_values}")
    missing_labels = check_labels(df)
    print(f"Rows without labels: {missing_labels}")
    if check_data_format(df, num_sensors):
        print("Data format is correct.")
    else:
        print("Data format is incorrect.")

    overall_min_value, overall_max_value = get_min_max_values(df)
    print(f"Overall minimum value across all sensors: {overall_min_value}")
    print(f"Overall maximum value across all sensors: {overall_max_value}")

    plot_sensor_values(overall_min_value, overall_max_value, num_sensors, file_path)

database_files = [
    ("../../Datasets/sensor_readings_2.data", 2),
    ("../../Datasets/sensor_readings_4.data", 4),
    ("../../Datasets/sensor_readings_24.data", 24)
]

for file_path, num_sensors in database_files:
    process_database(file_path, num_sensors)
