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
            print("=-" * len("Funcionário cadastrado com sucesso!"))
            frase = "Funcionário cadastrado com sucesso!"
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
    def ler_funcionario(id):
        try:
            id = int(id)
            conexao.cursor.execute(f"SELECT * FROM funcionarios WHERE id={id}")
            ler = conexao.cursor.fetchall()
            return ler
        except ValueError:
            print("Erro: ID inválido.")
        except conexao.error as ex:
            print(ex)

    def crud_execute(self):
        while True:
            print("1. Cadastrar Funcionário.")
            print("2. Listar Funcionários.")
            print("3. Lista Um Funcionário.")
            print("4. Sair")
            perg = input("Selecione a opção:")

            if perg == "1":
                self.criar_Funcionario()
            elif perg == "2":
                print("Esse são os funcionarios Cadastrados no Sitema.")
                self.ler_funcionarios()
            elif perg == "3":
                id = input("Digite o ID do funcionário:")
                funcionario = self.ler_funcionario(id)
                if funcionario:
                    funcionario = funcionario[0]
                    print("==" * len("Funcionário não encontrado."))
                    print("Dados do funcionário:")
                    print("ID:", funcionario[0])
                    print("Nome:", funcionario[1])
                    print("CPF:", funcionario[2])
                    print("Email:", funcionario[3])
                    print("Fone:", funcionario[4])
                    print("UF:", funcionario[5])
                    print("==" * len("Funcionário não encontrado."))
                else:
                    print("==" * len("Funcionário não encontrado."))
                    print("Funcionário não encontrado.")
                    print("==" * len("Funcionário não encontrado."))
            elif perg == "4":
                break
            elif not perg.isdigit() or int(perg) > 3 or int(perg) < 0:
                print("Opção Inválida")
                print("=-" * len("Selecione a opção"))


crud = CrudFuncionario()
crud.crud_execute()
