# https://leetcode.com/problems/classes-with-at-least-5-students/description/

import pandas as pd

data = [
    ["A", "Math"],
    ["B", "English"],
    ["C", "Math"],
    ["D", "Biology"],
    ["E", "Math"],
    ["F", "Computer"],
    ["G", "Math"],
    ["H", "Math"],
    ["I", "Math"],
]
courses = pd.DataFrame(data, columns=["student", "class"]).astype(
    {"student": "object", "class": "object"}
)


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # Group by class and count the number of students in each class
    class_counts = courses.groupby("class")["student"].count().reset_index()
    # print(courses.groupby('class')['student'].count())
    print(class_counts)

    # Filter classes with at least five students
    result = class_counts[class_counts["student"] >= 5][["class"]]
    # print(class_counts['student'] >= 5)

    return result
