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

    def ler_funcionario(self, id):
        try:
            id = int(id)
            conexao.cursor.execute(f"SELECT * FROM funcionarios WHERE id={id}")
            funcionarios = conexao.cursor.fetchall()

            return funcionarios

        except conexao.error as ex:
            print(ex)

    @staticmethod
    def atualizar_funcionario(id):
        try:
            id = int(input("Informe o ID:"))
            conexao.cursor.execute(f"SELECT * FROM funcionarios WHERE id={id}")
            funcionario = conexao.cursor.fetchone()

            if funcionario:
                print("Dados atuais do funcionário:")
                print("ID:", funcionario[0])
                print("Nome:", funcionario[1])
                print("CPF:", funcionario[2])
                print("Email:", funcionario[3])
                print("Fone:", funcionario[4])
                print("UF:", funcionario[5])
                print("========================")

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

                    if not novo_nome.isalpha():
                        print("Erro: O nome deve conter apenas letras.")
                    elif not novo_cpf.isdigit() or len(novo_cpf) != 11:
                        print("Erro: CPF inválido.")
                    elif not re.match(validar_email, novo_email):
                        print("Erro: Email inválido.")
                    elif not novo_fone.isdigit() or len(novo_fone) != 11:
                        print("Erro: Número de telefone inválido.")
                    elif not nova_uf.isalpha() or len(nova_uf) != 2:
                        print("Erro: UF inválida.")
                    else:
                        conexao.cursor.execute(
                            f"UPDATE funcionarios SET nome='{novo_nome}', cpf='{novo_cpf}', email='{novo_email}', fone='{novo_fone}', uf='{nova_uf}' WHERE id={id}"
                        )
                        conexao.banco.commit()
                        print("Funcionário atualizado com sucesso!")
                        break

            else:
                print("Funcionário não encontrado.")

        except ValueError:
            print("Erro: ID inválido.")

    def deletar_funcionario(self):
        try:
            id = int(input("Informe o ID:"))
            funcionario = self.ler_funcionario(id)

            if funcionario and len(funcionario) > 0:
                print("Dados do funcionário:")
                print("ID:", funcionario[0])
                print("Nome:", funcionario[1])
                print("CPF:", funcionario[2])
                print("Email:", funcionario[3])
                print("Fone:", funcionario[4])
                print("UF:", funcionario[5])
                print("========================")
            else:
                print("Funcionário não encontrado.")
            perg = str(
                input(f"Deseja Deletar o cadastro do funcionario (S/N):")
            ).lower()
            if perg == "s":
                conexao.cursor.execute(f"DELETE FROM funcionarios WHERE id={id}")
                conexao.banco.commit()
                print("Funcionario Deletado com Sucesso.")
            else:
                pass

        except ValueError:
            print("Erro: ID inválido.")

    def crud_execute(self):
        while True:
            print("1. Cadastrar Funcionário.")
            print("2. Listar Funcionários.")
            print("3. Lista Um Funcionário.")
            print("4. Sair")
            perg = input("Selecione a opção:")
            print("==" * len("Cadastrar Funcionário."))

            if perg == "1":
                self.criar_Funcionario()
            elif perg == "2":
                print("Esse são os funcionarios Cadastrados no Sistema.")
                self.ler_funcionarios()
            elif perg == "3":
                id = input("Digite o ID do funcionário:")
                funcionarios = self.ler_funcionario(id)
                if funcionarios:
                    funcionario = funcionarios[0]
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
