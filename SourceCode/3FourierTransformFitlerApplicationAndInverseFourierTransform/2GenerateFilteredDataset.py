import numpy as np
import pandas as pd

data_file = "../../Datasets/downsampled_sensor_front.csv"
df = pd.read_csv(data_file)
downsampled_sensor_data = df["Sensor_FRONT"].to_numpy()

fft_values = np.fft.fft(downsampled_sensor_data)

cutoff_frequency = 0.27
fft_values_low_pass = fft_values.copy()
fft_values_low_pass[np.abs(np.fft.fftfreq(len(downsampled_sensor_data))) > cutoff_frequency] = 0

filtered_signal_low_pass = np.fft.ifft(fft_values_low_pass).real

df["Filtered_Sensor_FRONT"] = filtered_signal_low_pass
output_file = "../../Datasets/filtered_sensor_front.csv"
df.to_csv(output_file, index=False)
