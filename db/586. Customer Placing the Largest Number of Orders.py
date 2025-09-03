# https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/

import pandas as pd

data = [[1, 1], [2, 2], [3, 3], [4, 3]]
orders = pd.DataFrame(data, columns=["order_number", "customer_number"]).astype(
    {"order_number": "Int64", "customer_number": "Int64"}
)


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = (
        orders.groupby("customer_number")
        .count()
        .sort_values("order_number", ascending=False)
        .reset_index()
        .head(1)
    )[["customer_number"]]
    print(df)
    return df


largest_orders(orders)
