# https://leetcode.com/problems/triangle-judgement/description/

import pandas as pd
import numpy as np

data = [[13, 15, 30], [10, 20, 15]]
triangle = pd.DataFrame(data, columns=["x", "y", "z"]).astype(
    {"x": "Int64", "y": "Int64", "z": "Int64"}
)


def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    df = triangle
    # df["triangle"] = np.where(
    #     (
    #         (df["x"] + df["y"] > df["z"])
    #         & (df["x"] + df["z"] > df["y"])
    #         & (df["z"] + df["y"] > df["x"])
    #     ),
    #     "Yes",
    #     "No",
    # )
    df["triangle"] = (
        (df["x"] + df["y"] > df["z"])
        & (df["x"] + df["z"] > df["y"])
        & (df["z"] + df["y"] > df["x"])
    ).map({True: "Yes", False: "No"})
    print(df)
    return df


triangle_judgement(triangle)
