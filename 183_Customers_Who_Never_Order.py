# https://leetcode.com/problems/customers-who-never-order/description/
# Easy
# Database
import pandas as pd


data = [[1, "Joe"], [2, "Henry"], [3, "Sam"], [4, "Max"]]
customers = pd.DataFrame(data, columns=["id", "name"]).astype(
    {"id": "Int64", "name": "object"}
)
data = [[1, 3], [2, 1]]
orders = pd.DataFrame(data, columns=["id", "customerId"]).astype(
    {"id": "Int64", "customerId": "Int64"}
)


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # df = orders.merge(customers, left_on="customerId", right_on="id", how="right")
    # mask = df["customerId"].isna()
    # result_df = df[mask]
    # result_df = result_df[["name"]].rename(columns={"name": "Customers"})

    df = customers[~customers["id"].isin(orders["customerId"])]
    df = df[["name"]].rename(columns={"name": "Customers"})

    return df


find_customers(customers, orders)
