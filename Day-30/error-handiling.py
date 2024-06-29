# FileNotFound tryCatch code - need to put ni the except filenotfound.

# try:
#     file = open("Day-30/a_file.txt")
#     a_ddiction = {"key" : "value"}
#     print(a_ddiction["key"])
# except FileNotFoundError:
#     file = open("Day-30/a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:  # this gets hold of error message
#     print(f"there is a key error: {error_message}")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("file was closed")
#     raise TypeError("error i made up")

# height = float(input("height: "))
# weight = float(input("weight: "))

# if height > 3:
#     raise ValueError("Height shoud not be over 3 meters")

# bmi = weight / height ** 2

# print(bmi)


diction_df = {
    "happy": {
        "email": "sam.john.vs@gmail.com",
        "password": "olc35J&r*nL(nP"
    },
    "test": {
        "email": "sam.john.vs@gmail.com",
        "password": "Q4%)*O3x&3EtpbM"
    }
}


print(diction_df["happy"])
