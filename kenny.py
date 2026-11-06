Boxes = [
    {"boxno": "1", "depth_m": 37, "grade": 0.5},
    {"boxno": "2", "depth_m": 40, "grade": 0.45},
    {"boxno": "3", "depth_m": 45, "grade": 0.65},
    {"boxno": "4", "depth_m": 67, "grade": 0.70},
    {"boxno": "5", "depth_m": 76, "grade": 0.34},
    {"boxno": "6", "depth_m": 34, "grade": 0.46},
    {"boxno": "7", "depth_m": 78, "grade": 0.49},
    {"boxno": "8", "depth_m": 34, "grade": 0.56},
    {"boxno": "9", "depth_m": 65, "grade": 0.58},
    {"boxno": "10", "depth_m": 37, "grade": 0.567}
        ]

cutoff_grade = 0.5

for pen in Boxes:
    grade = pen["grade"]
    if grade > cutoff_grade:
        print(f'Box {pen["boxno"]} is above cutoff: {grade}%')
    else:
        print(f'Box {pen["boxno"]} is not acceptable with grade {grade}')

average_grade = sum(pen["grade"]* pen["depth_m"] for pen in Boxes) / sum(pen)