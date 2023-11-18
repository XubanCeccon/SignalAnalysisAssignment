import pandas as pd
import matplotlib.pyplot as plt

file_info = [
    ("../../Datasets/sensor_readings_2.data", 2, "2 sensors dataset"),
    ("../../Datasets/sensor_readings_4.data", 4, "4 sensors dataset"),
    ("../../Datasets/sensor_readings_24.data", 24, "24 sensors dataset")
]

for file_path, sensor_count, label in file_info:
    data = pd.read_csv(file_path, header=None)
    sensors = data.iloc[:, :sensor_count]
    time = sensors.index / 9  
    
    if sensor_count == 24:
        selected_sensors = [1, 5, 9, 13, 17, 21]
        selected_sensor_labels = [f'Sensor: {i+1}' for i in selected_sensors]
        selected_sensor_data = sensors[selected_sensors]
        
        plt.figure(figsize=(12, 4))
        
        for i in range(len(selected_sensors)):
            plt.scatter(time, selected_sensor_data.iloc[:, i], s=10, label=selected_sensor_labels[i])
    else:
        plt.figure(figsize=(12, 4))
        
        for i in range(sensor_count):
            plt.scatter(time, sensors[i], s=10, label=f'Sensor: {i+1}')
    
    plt.xlabel('Time (seconds)')
    plt.ylabel('Sensor Readings')
    plt.title(f'Sensor Readings from {label}')
    plt.legend()
    plt.show()
