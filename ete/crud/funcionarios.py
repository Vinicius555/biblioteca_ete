import conexao
import re

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
                nome = input("Nome: ")
                if not nome.isalpha():
                    print("Erro: O nome deve conter apenas letras.")
                else:
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
            print("Funcionário cadastrado com sucesso!")

    @staticmethod
    def ler_funcionario(self):
        try:
            while True:
                print("1. Verificar Funcionários")
                print("2. Pesquisar Funcionário")
                print("3. Sair")
                perg = int(input("Selecione a opção: "))

                if perg == 1:
                    conexao.cursor.execute("SELECT * FROM funcionarios")
                    read = conexao.cursor.fetchall()
                    return read
                elif perg == 2:
                    self.id = id_pesquisa
                    id_pesquisa = input("ID: ")
                    conexao.cursor.execute(
                        f"SELECT * FROM funcionarios WHERE id = {id_pesquisa}"
                    )
                    read = conexao.cursor.fetchall()
                    return read
                else:
                    break
        except conexao.error as ex:
            print(ex)

    def crud_execute(self):
        while True:
            perg = int(input("Selecione a opção:"))
            print("1. Cadastra Funcionario.")
            print("2. Lista Funciionario.")
            print("3. sair")

            if perg == 1:
                self.criar_Funcionario
            if perg == 2:
                self.ler_funcionario
            elif perg == 3:
                break
            else:
                print("Opção Inválida")


CrudFuncionario.crud_execute()
