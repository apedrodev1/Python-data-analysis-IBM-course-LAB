# Read and write at the same file/code block


# Ler e alterar a nota do primeiro aluno
with open("../notes.txt", "r") as file:
    linhas = file.readlines()

linhas[0] = "Pedro - 10.0\n"  # alterando a primeira linha

with open("../notes.txt", "w") as file:
    file.writelines(linhas)

# Conferindo alteração
with open("../notes.txt", "r") as file:
    print("📖 Após modificação:")
    print(file.read())





#   "a" (append) → só escreve no final, sem apagar o conteúdo existente.

#   "r+" (read/write) → abre o arquivo para leitura e escrita, mas sobrescreve a partir do começo do arquivo