# Reading mode
with open("notes.txt", "r") as file1:
    file_stuff = file1.readline()
    # file_stuff = file1.readline(7)
    print(file_stuff)