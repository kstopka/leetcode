# https://leetcode.com/problems/rising-temperature/description/

import pandas as pd

data = [
    [1, "2015-01-01", 10],
    [2, "2015-01-02", 25],
    [3, "2015-01-03", 20],
    [4, "2015-01-04", 30],
]
weather = pd.DataFrame(data, columns=["id", "recordDate", "temperature"]).astype(
    {"id": "Int64", "recordDate": "datetime64[ns]", "temperature": "Int64"}
)


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather["key"] = 1
    df = weather.merge(weather, on="key", suffixes=("_left", "_right")).drop(
        "key", axis=1
    )
    df = df[df["recordDate_right"] == df["recordDate_left"] - pd.Timedelta(days=1)]
    df = df[df["temperature_left"] > df["temperature_right"]]
    df = df.rename(columns={"id_left": "id"}).reset_index()[["id"]]
    return df


rising_temperature(weather)
