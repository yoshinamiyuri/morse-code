import pandas
## 2021/4/17 ZIPの方法がある　！要復習

student_dict = {
    "student": ["Angle", "James", "Lily"],
    "score": [56, 76, 98]
}

print(student_dict["student"]["James"])

# Looping through dictionaries
# for (key, value) in student_dict.items():
#     print(value)
#
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# # Looping through  a data frame
# for (key, value) in student_data_frame.items():
    # print(key)
    # print(value)

# Looping through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    # print(row.student)
    # print(row.score)
    # print(row.index)

student_score = {
    key: value
    for key, value in zip(student_dict["student"], student_dict["score"])
    if value >= 70
}

print(student_score)
