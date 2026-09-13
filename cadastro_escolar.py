class cadastro_escolar:
    matricula = 0
    nome = ""
    curso = ""


def main():

    cadastro = cadastro_escolar()
    resposta = ""

    while True:

        print("Digite a Matricula.:    ")
        cadastro.matricula = int(input())

        print("Digite o nome do aluno.: ")
        cadastro.nome = input()

        print("Deseja cadastrar um curso ? (S/N): ")
        resposta = input()

        if resposta == "S" or resposta == "s":

            print("Digite o curso do aluno: ")
            cadastro.curso = input()

        else:

            cadastro.curso = "Não Informado"

        print("\n=== RESUMO DO CADASTRO ===\n")

        print("Matricula: ", cadastro.matricula)
        print("Nome:   ", cadastro.nome)
        print("Curso:  ", cadastro.curso)

        resposta = input("\nDeseja cadastrar outro aluno? (S/N): ")

        if resposta == "N" or resposta == "n":
            break

    print("\n=== FINAL DO RESUMO ===")

main()