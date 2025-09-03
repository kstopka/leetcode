# https://leetcode.com/problems/duplicate-emails/
# Easy
# Database
import pandas as pd

data = [[1, "a@b.com"], [2, "c@d.com"], [3, "a@b.com"]]
person = pd.DataFrame(data, columns=["id", "email"]).astype(
    {"id": "Int64", "email": "object"}
)


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df = person.groupby("email")["id"].count().reset_index()
    return df[df["id"] > 1][["email"]]


print(duplicate_emails(person))
