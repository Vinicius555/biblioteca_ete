import conexao
import re
from clientes import CrudClientes
from livros import CrudLivros
from unidecode import unidecode

nome_padrao = r"^[a-zA-Z]+( [a-zA-Z]+)*$"

validar_email = r"^[\w\.-]+@[\w]+\.[a-zA-Z]{2,}$"


class Funcionario:
    def __init__(self, nome, cpf, email, fone, uf):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.fone = fone
        self.uf = uf


class CrudFuncionario:
    @staticmethod
    def criar_Funcionario():
        try:
            while True:
                nome = input("NOME:")
                nomes = nome.split()

                if len(nomes) >= 1:
                    nome_completo = " ".join(nomes)
                    nome_sem_acentos = unidecode(nome_completo)
                    if re.match(nome_padrao, nome_sem_acentos):
                        break

            while True:
                cpf = input("CPF: ")
                if not cpf.isdigit():
                    print("Erro: O CPF deve conter apenas números.")
                elif len(cpf) != 11:
                    print(
                        "Erro: Tamanho do CPF inválido. Verifique se digitou corretamente."
                    )
                else:
                    break

            while True:
                email = input("Email: ")
                if re.match(validar_email, email):
                    break
                else:
                    print("Email inválido!")

            while True:
                fone = input("Fone: ")
                if not fone.isdigit():
                    print("Erro: O Fone deve conter apenas números.")
                elif len(fone) != 11:
                    print(
                        "Erro: Número de telefone incorreto. Verifique se digitou corretamente."
                    )
                else:
                    break

            while True:
                uf = input("UF: ")
                if not uf.isalpha():
                    print("Erro: Só deve conter letras.")
                elif len(uf) != 2:
                    print("Erro: UF inválida. Verifique se digitou corretamente.")
                else:
                    break

        except conexao.error as ex:
            print(ex)
        else:
            conexao.cursor.execute(
                f"INSERT INTO funcionarios VALUES (NULL, '{nome}', '{cpf}', '{email}', '{fone}', '{uf}')"
            )
            conexao.banco.commit()
            print("=-" * len("Funcionário cadastrado com sucesso!"))
            print("Funcionário cadastrado com sucesso!")
            print("=-" * len("Funcionário cadastrado com sucesso!"))

    @staticmethod
    def ler_funcionarios():
        try:
            conexao.cursor.execute("SELECT * FROM funcionarios")
            funcionarios = conexao.cursor.fetchall()

            for funcionario in funcionarios:
                print("ID:", funcionario[0])
                print("Nome:", funcionario[1])
                print("CPF:", funcionario[2])
                print("Email:", funcionario[3])
                print("Fone:", funcionario[4])
                print("UF:", funcionario[5])
                print("========================")

        except conexao.error as ex:
            print(ex)

    @staticmethod
    def ler_funcionario():
        try:
            while True:
                nome = input("Informe o Nome:")
                conexao.cursor.execute(
                    f"SELECT * FROM funcionarios WHERE Nome='{nome}'"
                )
                funcionarios = conexao.cursor.fetchall()
                if funcionarios:
                    for funcionario in funcionarios:
                        print("Dados atuais do funcionário:")
                        print("ID:", funcionario[0])
                        print("Nome:", funcionario[1])
                        print("CPF:", funcionario[2])
                        print("Email:", funcionario[3])
                        print("Fone:", funcionario[4])
                        print("UF:", funcionario[5])
                        print("========================")
                    break
                else:
                    print("Funcionario não encontrado!")
                    print("1. Ler Funcionarios Cadastrados")
                    print("2. Procurar Funcionario.")
                    print("3. sair")
                    perg = input("Oque Deseja Fazer:")
                    if perg == "1":
                        CrudFuncionario().ler_funcionarios()
                    elif perg == "2":
                        pass
                    elif perg == "3":
                        break
                    else:
                        print("Opção Inválida.")

        except conexao.error as ex:
            print(ex)

    @staticmethod
    def atualizar_funcionario():
        try:
            while True:
                nome = input("Informe o Nome:")
                conexao.cursor.execute(
                    f"SELECT * FROM funcionarios WHERE Nome='{nome}'"
                )
                Funcionarios = conexao.cursor.fetchall()
                if Funcionarios:
                    for funcionario in Funcionarios:
                        print("Dados atuais do funcionário:")
                        print("ID:", funcionario[0])
                        print("Nome:", funcionario[1])
                        print("CPF:", funcionario[2])
                        print("Email:", funcionario[3])
                        print("Fone:", funcionario[4])
                        print("UF:", funcionario[5])
                        print("========================")

                    break
                else:
                    print("Funcionário não encontrado.")
                    print("1. Pesquisar de novo.")
                    print("2. Verificar funcionários registrados.")
                    print("3. Sair")
                    perg = input("O que deseja fazer:")
                    if perg == "1":
                        pass
                    elif perg == "2":
                        CrudFuncionario().ler_funcionarios()
                    elif perg == "3":
                        return
                    else:
                        print("Opção inválida.")
            while True:
                print(
                    "Digite os novos dados do funcionário (ou deixe em branco para manter o valor atual):"
                )
                novo_nome = input(f"Novo nome ({funcionario[1]}): ")
                novo_cpf = input(f"Novo CPF ({funcionario[2]}): ")
                novo_email = input(f"Novo email ({funcionario[3]}): ")
                novo_fone = input(f"Novo telefone ({funcionario[4]}): ")
                nova_uf = input(f"Nova UF ({funcionario[5]}): ")

                novo_nome = novo_nome if novo_nome else funcionario[1]
                novo_cpf = novo_cpf if novo_cpf else funcionario[2]
                novo_email = novo_email if novo_email else funcionario[3]
                novo_fone = novo_fone if novo_fone else funcionario[4]
                nova_uf = nova_uf if nova_uf else funcionario[5]

                if not novo_nome.isspace() and re.match(nome_padrao, novo_nome):
                    if not novo_cpf.isdigit() or len(novo_cpf) != 11:
                        print("Erro: CPF inválido.")
                    elif not re.match(validar_email, novo_email):
                        print("Erro: Email inválido.")
                    elif not novo_fone.isdigit() or len(novo_fone) != 11:
                        print("Erro: Número de telefone inválido.")
                    elif not nova_uf.isalpha() or len(nova_uf) != 2:
                        print("Erro: UF inválida.")
                    else:
                        conexao.cursor.execute(
                            f"UPDATE funcionarios SET nome='{novo_nome}', cpf={novo_cpf}, email='{novo_email}', fone={novo_fone}, uf='{nova_uf}' WHERE Nome='{nome}'"
                        )
                        conexao.banco.commit()
                        print("Funcionário atualizado com sucesso!")
                        break
                else:
                    print("Erro: Formato de nome inválido.")
        except ValueError:
            print("Erro: Nome inválido.")

    @staticmethod
    def deletar_funcionario():
        try:
            while True:
                id = int(input("Informe o ID:"))
                conexao.cursor.execute(f"SELECT * FROM funcionarios WHERE id={id}")
                funcionario = conexao.cursor.fetchall()

                if funcionario:
                    for funcionario in funcionario:
                        print("Dados do funcionário:")
                        print("ID:", funcionario[0])
                        print("Nome:", funcionario[1])
                        print("CPF:", funcionario[2])
                        print("Email:", funcionario[3])
                        print("Fone:", funcionario[4])
                        print("UF:", funcionario[5])
                        print("========================")
                        break
                    perg = str(
                        input(f"Deseja Deletar o cadastro do funcionario (S/N):")
                    ).lower()
                    if perg == "s":
                        conexao.cursor.execute(
                            f"DELETE FROM funcionarios WHERE id={id}"
                        )
                        conexao.banco.commit()
                        print("Funcionario Deletado com Sucesso.")
                        break
                else:
                    print("============================")
                    print("Funcionário não encontrado.")
                    print("Oque deseja fazer:")
                    print("1. Tentar De novo.")
                    print("2. Lista Funcionarios.")
                    print("3. Sair")
                    perg = input("Selecione a opção.")
                    print("============================")
                    if perg == "1":
                        pass
                    elif perg == "2":
                        CrudFuncionario().ler_funcionarios()
                    elif perg == "3":
                        print("============================")
                        break
                    else:
                        print("Opção inválida.")
        except ValueError:
            print("Erro: ID inválido.")

    @staticmethod
    def crud_execute_funcionario():
        while True:
            print("==============================")
            print("1.  Cadastrar Funcionário.")
            print("2.  Listar Funcionários.")
            print("3.  Procurar Funcionário.")
            print("4.  Alterar Funcionário.")
            print("5.  Deleta Funcionário")
            print("6.  Lista Cliente.")
            print("7.  Alterar Cliente.")
            print("8.  Procurar Cliente.")
            print("9.  Deleta Cliente.")
            print("10. Cadastrar Livro.")
            print("11. Alterar livro.")
            print("12. Lista Livros.")
            print("13. Procurar Livro.")
            print("14. Deletar Livro")
            print("0.  Sair")
            perg = input("Selecione a opção:")
            print("=============================")

            if perg == "1":
                CrudFuncionario().criar_Funcionario()
            elif perg == "2":
                print("Esse são os funcionarios Cadastrados no Sistema.")
                CrudFuncionario().ler_funcionarios()
            elif perg == "3":
                CrudFuncionario().ler_funcionario()
            elif perg == "4":
                CrudFuncionario().atualizar_funcionario()
            elif perg == "5":
                CrudFuncionario.deletar_funcionario()
            elif perg == "6":
                CrudClientes().ler_clientes()
            elif perg == "7":
                CrudClientes().atualizar_cliente()
            elif perg == "8":
                CrudClientes().ler_cliente()
            elif perg == "9":
                CrudClientes().deleta_cliente()
            elif perg == "10":
                CrudLivros.criar_livros()
            elif perg == "11":
                CrudLivros().atualizar_livro()
            elif perg == "12":
                CrudLivros().ler_livros()
            elif perg == "13":
                CrudLivros().ler_livro()
            elif perg == "14":
                CrudLivros.deleta_livro()
            elif perg == "0":
                break
            else:
                print("======================================================")
                print("Opção inválida. Por favor, selecione uma opção válida.")
                print("======================================================")
