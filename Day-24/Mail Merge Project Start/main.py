#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("Day-24/Mail Merge Project Start/Input/Names/invited_names.txt") as fnames:
    names = fnames.read().splitlines()

with open("Day-24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as fletter:
    letter = fletter.read()

for x in names:
    new_letter = letter.replace("[name]", x)
    with open("Day-24/Mail Merge Project Start/Output/ReadyToSend/" + x + ".txt", mode = "w") as file:
        file.write(new_letter)


    
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
        
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp