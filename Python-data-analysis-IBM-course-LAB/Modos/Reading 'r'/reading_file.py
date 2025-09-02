# Reading mode 'r' - default, read the file. 


# Read all content
with open("../notes.txt", "r") as file:
    print("📖 Conteúdo completo:")
    print(file.read())

# Read first line
with open("../notes.txt", "r") as file:
    print("📖 Primeira linha:")
    print(file.readline())

# Read all lines into a list
with open("../notes.txt", "r") as file:
    print("📖 Todas as linhas em lista:")
    print(file.readlines())
