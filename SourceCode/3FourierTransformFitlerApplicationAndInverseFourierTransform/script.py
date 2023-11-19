import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

data_file = "../../Datasets/downsampled_sensor_front.csv"
df = pd.read_csv(data_file)

downsampled_sensor_data = df["Sensor_FRONT"].to_numpy()
fft_values = np.fft.fft(downsampled_sensor_data)
cutoff_frequencies = [0.1, 0.2, 0.27]
time = np.arange(len(downsampled_sensor_data)) / 0.06
filtered_signals = []

plt.figure(figsize=(12, 6))
plt.plot(time, downsampled_sensor_data, label="Down-sampled Signal", alpha=0.7)

for cutoff_frequency in cutoff_frequencies:
    fft_values_low_pass = fft_values.copy()
    fft_values_low_pass[np.abs(np.fft.fftfreq(len(downsampled_sensor_data))) > cutoff_frequency] = 0
    filtered_signal_low_pass = np.fft.ifft(fft_values_low_pass)
    label = f"Low-Pass Filter (Cutoff Frequency = {cutoff_frequency})"
    plt.plot(time, filtered_signal_low_pass.real, label=label, alpha=0.7)
    filtered_signals.append(filtered_signal_low_pass.real)

plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Low-Pass Filters with Different Cutoff Frequencies")
plt.legend()
plt.grid(True)
plt.show()

for idx, filtered_signal in enumerate(filtered_signals):
    rmse = np.sqrt(np.mean((downsampled_sensor_data - filtered_signal) ** 2))
    pearson_corr, _ = pearsonr(downsampled_sensor_data, filtered_signal)
    print(f"Cutoff frequency {cutoff_frequencies[idx]}: RMSE = {rmse:.3f}, Pearson Correlation = {pearson_corr:.3f}")
