import pandas as pd

data = [[8], [8], [3], [3]]
my_numbers = pd.DataFrame(data, columns=["num"]).astype({"num": "Int64"})


def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    df = my_numbers.groupby("num")["num"].count().reset_index(name="count")
    df = df[df["count"] == 1].max()["num"]
    return pd.DataFrame({"num": [df]})


biggest_single_number(my_numbers)
