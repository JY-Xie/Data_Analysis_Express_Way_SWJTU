import pandas as pd
import numpy as np
import datetime

raw_data = pd.read_csv(
    r"C:\Users\XieJiYe\Desktop\作业\trajectory.csv", 
    encoding="UTF8", 
    header=None, 
    usecols=[0, 1, 2, 3, 4, 7, 8, 9]
    )
raw_data.columns = ["id", "time", "veh_type", "speed", "lane", "distance", "eh_length", "detect_flag"]
print(raw_data.head())
raw_data["time"] = pd.to_datetime(raw_data["time"], format="%H%M%S%f").dt.time
print(raw_data.head())
print(raw_data.loc[0, "time"])
print(type(raw_data.loc[0, "time"]))
time_group = raw_data.groupby("time")
test_data = time_group.get_group(datetime.datetime.strptime("10:00:00.500000", "%H:%M:%S.%f").time())
print(test_data)
