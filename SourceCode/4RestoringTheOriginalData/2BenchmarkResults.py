import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

original_file = "../../Datasets/sensor_readings_2.data"
restored_file = "../../Datasets/restored_sensor_front.csv"

original_df = pd.read_csv(original_file, header=None)
restored_df = pd.read_csv(restored_file)

original_data = original_df.iloc[:, 0].values
restored_data = restored_df['Restored_Sensor_FRONT'].values

original_time_scale = np.linspace(0, 1, len(original_data))
restored_time_scale = np.linspace(0, 1, len(restored_data))

interpolator = interp1d(restored_time_scale, restored_data, kind='linear')
rescaled_restored_data = interpolator(original_time_scale)

plt.figure(figsize=(14, 7))
plt.plot(original_data, label='Original Data')
plt.plot(rescaled_restored_data, label='Rescaled Restored Data', alpha=0.75)
plt.title('Comparison of Original and Rescaled Restored Data')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
