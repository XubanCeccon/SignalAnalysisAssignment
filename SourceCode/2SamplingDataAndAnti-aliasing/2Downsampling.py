import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def downsample_and_generate_graph(file_path, output_dir):
    # Perform down-sampling
    df = pd.read_csv(file_path, header=None)
    sensor_data = df.iloc[:, 0]
    sampling_rate = 0.06
    downsampled_data = sensor_data.iloc[::int(1 / sampling_rate)]
    downsampled_df = pd.DataFrame({"Sensor_FRONT": downsampled_data})
    output_path = f"{output_dir}/downsampled_sensor_front.csv"
    downsampled_df.to_csv(output_path, index=False)

    # Generate and display the graph
    original_data_file = file_path
    original_df = pd.read_csv(original_data_file, header=None)
    original_sensor_data = original_df.iloc[:, 0]
    original_time = np.arange(len(original_sensor_data))

    plt.figure(figsize=(12, 6))
    plt.plot(original_time, original_sensor_data, label="Original Signal", alpha=0.7)
    plt.plot(original_time[::int(1 / 0.06)], downsampled_data, label="Down-sampled Signal", alpha=0.7)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.title("Original vs Down-sampled Signal")
    plt.legend()
    plt.grid(True)
    plt.show()

file_path = "../../Datasets/sensor_readings_2.data"
output_dir = "../../Datasets/"

downsample_and_generate_graph(file_path, output_dir)
