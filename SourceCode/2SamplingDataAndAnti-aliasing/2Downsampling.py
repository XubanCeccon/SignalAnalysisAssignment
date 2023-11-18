import pandas as pd

def downsample_and_save(file_path, output_dir):
    df = pd.read_csv(file_path, header=None)
    sensor_data = df.iloc[:, 0]
    sampling_rate = 0.06
    downsampled_data = sensor_data.iloc[::int(1 / sampling_rate)]
    downsampled_df = pd.DataFrame({"Sensor_FRONT": downsampled_data})
    output_path = f"{output_dir}/downsampled_sensor_front.csv"
    downsampled_df.to_csv(output_path, index=False)

file_path = "../../Datasets/sensor_readings_2.data"
output_dir = "../../Datasets/"

downsample_and_save(file_path, output_dir)
