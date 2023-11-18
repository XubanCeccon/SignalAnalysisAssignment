import numpy as np
import pandas as pd

file_paths = [
    "../../Datasets/sensor_readings_2.data",
    "../../Datasets/sensor_readings_4.data",
    "../../Datasets/sensor_readings_24.data"
]

for file_path in file_paths:
    print(f"Analysis for {file_path}:")

    df = pd.read_csv(file_path, header=None)

    num_sensors = df.shape[1]
    for sensor_num in range(num_sensors):
        sensor_data = df.iloc[:, sensor_num]

        try:
            fft_values = np.fft.fft(sensor_data)
        except ValueError as e:
            continue

        frequencies = np.fft.fftfreq(len(sensor_data), d=1/9)
        amplitudes = np.abs(fft_values)

        threshold = 0.1 * max(amplitudes)
        significant_freqs = frequencies[amplitudes > threshold]
        highest_significant_freq = max(significant_freqs)

        suggested_sampling_rate = 2 * highest_significant_freq

        print(f"\nSensor {sensor_num + 1}:")
        print("Highest Significant Frequency:", highest_significant_freq)
        print("Suggested New Sampling Rate:", suggested_sampling_rate)
