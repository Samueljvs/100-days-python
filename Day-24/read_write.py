# with open("Day-24/my_file.txt") as file:
#     contents = file.read()
#     print(contents)
# w overwrites, a appends

# with open("Day-24/my_file.txt", mode="a") as file:
#     file.write("\nNew Text.")


# if it doesn't exisit it will create a new file, as long as it's in the right mode.

# with open("Day-24/new_file.txt", mode = "w") as file:
#     file.write("new-text")




highscore = 1

with open("Day-24/data.txt", mode = "a") as file:
    file.write("\n" + str(highscore))

with open("Day-24/data.txt") as file:
    contents = file.read().splitlines()

highscore = int(contents[-1])

print(highscore)

