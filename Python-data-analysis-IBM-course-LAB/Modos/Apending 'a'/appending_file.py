# Append mode 'a' add contend at the end. Do not overscribed

with open ('../notes.txt' 'a') as file:
    file.write('Maria - 7.5\n')


with open("notas.txt", "r") as file:
    print("📖 Conteúdo após append:")
    print(file.read())