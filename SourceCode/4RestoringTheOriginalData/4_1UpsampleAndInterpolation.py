import numpy as np
import pandas as pd
from scipy.interpolate import interp1d

data_file = "../../Datasets/filtered_sensor_front.csv"
df = pd.read_csv(data_file)
filtered_data = df["Filtered_Sensor_FRONT"].to_numpy()

downsampling_factor = 1 / 0.06
original_length = int(len(filtered_data) * downsampling_factor)

upsampled_time = np.linspace(0, len(filtered_data), original_length)

interpolate = interp1d(np.arange(len(filtered_data)), filtered_data, kind='linear')
interpolated_data = interpolate(np.linspace(0, len(filtered_data) - 1, original_length))

restored_df = pd.DataFrame({'Restored_Sensor_FRONT': interpolated_data})
output_file = "../../Datasets/restored_sensor_front.csv"
restored_df.to_csv(output_file, index=False)
