import pandas as pd
import numpy as np
import datetime
from tqdm import tqdm


def calc_spacing(df_data: pd.DataFrame, lane_num: int) -> int:
    df_data = df_data[df_data["lane"] == lane_num]
    time_group = df_data.groupby("time")

    result_df = pd.DataFrame()
    temp_list = []
    for each_group_time, group_data in tqdm(time_group):
        group_data.sort_values("distance", inplace=True)
        group_data["temp"] = group_data["distance"].shift(1)
        group_data["behind_car"] = group_data["id"].shift(1)
        group_data['distance_diff'] = group_data['distance'] - group_data['temp']
        temp_list.append(group_data)
    result_df = pd.concat(temp_list, ignore_index=True)
    result_df.dropna(inplace=True)
    result_df["behind_car"] = result_df["behind_car"].astype(int).astype(str)
    result_df.drop(columns=["veh_type", "speed", "lane", "distance", "eh_length", "detect_flag", "temp"], inplace=True)
    result_df = result_df.reindex(columns=["id", "behind_car", "distance_diff", "time"])
    result_df.to_csv(f"lane_{lane_num}_spacing.csv", encoding="UTF8", index=False)
    return 0


if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    raw_data = pd.read_csv(
        r".\data\trajectory.csv",
        encoding="UTF8",
        header=None,
        usecols=[0, 1, 2, 3, 4, 7, 8, 9],
        dtype={
            "id": str
        }
    )

    raw_data.columns = ["id", "time", "veh_type", "speed", "lane", "distance", "eh_length", "detect_flag"]
    raw_data["time"] = pd.to_datetime(raw_data["time"], format="%H%M%S%f").dt.time
    calc_spacing(df_data=raw_data, lane_num=1)
    calc_spacing(df_data=raw_data, lane_num=2)
