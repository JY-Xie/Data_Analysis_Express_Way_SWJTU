import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = r".\data\trajectory.csv"

dtype = {
    'vehicle_id': np.int16,
    'datetime': 'string',
    'vehicle_type': np.int8,
    'velocity': np.float32,
    'traffic_lane': np.int8,
    'longitude': np.float32,
    'latitude': np.float32,
    'kilopost': np.float32,
    'vehicle_length': np.float16,
    'detected_flag': np.int8
}
df = pd.read_csv(
    path,
    names=[
        'vehicle_id', 'datetime', 'vehicle_type',
        'velocity', 'traffic_lane', 'longitude',
        'latitude', 'kilopost', 'vehicle_length',
        'detected_flag'],
    dtype=dtype
)

df['datetime'] = pd.to_datetime(df['datetime'], format='%H%M%S%f')

vehicle_id = df['vehicle_id'].unique()
datetime_array = np.array([]).astype(np.float32)
for id in vehicle_id:
    df_id = df[df['vehicle_id'] == id]
    datetime = (df_id['datetime'].values - df_id['datetime'].values[0]).astype(np.timedelta64(1, 'ms')).astype(np.float32) / 1000
    datetime_array = np.append(datetime_array, datetime)
print(datetime_array)
df['new_datetime'] = datetime_array
df.to_csv("ddd.csv")
print(df)

# df_value_count = df['datetime'].value_counts()
# print(df_value_count)