# list comp
numbers = [1,2,3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

name = "Samuel"
new_name = [letter for letter in name]
print(new_name)


new_range = [number * 2 for number in range(0,5)]
print(new_range)


# condtional list comphrehsion

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)


long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)


# Dict Comphrension
#
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_scores = {student:random.randint(30,100) for student in names}
print(student_scores)

# loop through dictionary

passed_students = {key:value for (key,value) in student_scores.items() if value >= 60}
print(passed_students)

## Iterate over a pandas dataframe

import pandas as pd

student_dict = {
    "student":["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"],
    "score":[56,76,43,87,45,65]
}

student_df = pd.DataFrame(student_dict)
print(student_df)

## Loop through datafrmae

for (key,value) in student_df.items():
    print(key)
    print(value)

    #pandas has an in-built loop called iterrows
for (index, row) in student_df.iterrows():
    print(row.student)
    if row.student == "Dave":
        print(row.score)
