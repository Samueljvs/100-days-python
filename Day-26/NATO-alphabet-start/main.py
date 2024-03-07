student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:

nato_df = pandas.read_csv("Day-26/NATO-alphabet-start/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("What is the name you with to spell?: ").upper()

# dictionary
listp = {k:phonetic_dict[k] for k in user_input}

# list
listp = [phonetic_dict[k] for k in user_input]
print(listp)