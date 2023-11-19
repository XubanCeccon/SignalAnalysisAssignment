# The goal of this script is to explore correlations between the sensors in the robot and also between the sensors and the labels


import pandas as pd

file_info = [
    ("../../Datasets/sensor_readings_2.data", 2, "2 sensors dataset"),
    ("../../Datasets/sensor_readings_4.data", 4, "4 sensors dataset"),
    ("../../Datasets/sensor_readings_24.data", 24, "24 sensors dataset")
]

for file_path, sensor_count, label in file_info:
    print(f"Correlation Analysis for {label}:")
    data = pd.read_csv(file_path, header=None)
    sensors = data.iloc[:, :sensor_count]
    if data.shape[1] > sensor_count:
        label_column = data.iloc[:, sensor_count]
        if pd.api.types.is_numeric_dtype(label_column):
            correlation_with_label = sensors.apply(lambda x: x.corr(label_column)).round(2)
            print("\nCorrelation with Label:")
            print(correlation_with_label)
        else:
            print(" ")
    sensor_correlation = sensors.corr().round(2)
    print("\nSensor Correlation Matrix:")
    print(sensor_correlation)

    print("\n")
