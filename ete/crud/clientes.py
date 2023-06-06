import conexao
import re
from livros import CrudLivros


class Clientes:
    def __init__(self, nome, cpf, fone):
        self.nome = nome
        self.cpf = cpf
        self.fone = fone


class CrudClientes:
    @staticmethod
    def criar_clientes():
        try:
            while True:
                nome = input("NOME:")
                if not nome.isalpha():
                    print("ERROR!Digite apenas Letras")
                else:
                    break
            while True:
                cpf = input("CPF:")
                if not cpf.isdigit():
                    print("ERROR!Digite apenas números.")
                elif len(cpf) != 11:
                    print("ERROR!Tamanaho do CPF inválido.")
                else:
                    break
            while True:
                fone = input("FONE:")
                if not fone.isdigit():
                    print("ERROR!Digite apenas Números.")
                elif len(fone) != 11:
                    print("ERROR!Esse número não existi.")
                else:
                    break
        except conexao.error as ex:
            print(ex)
        else:
            conexao.cursor.execute(
                f"INSERT INTO clientes VALUES (NULL,'{nome}',{cpf},{fone})"
            )
            conexao.banco.commit()
            print("Usuário cadastrado com sucesso!")
            print("==" * len("Usuário cadastrado com sucesso!"))

    @staticmethod
    def ler_clientes():
        try:
            conexao.cursor.execute("SELECT * FROM clientes")
            clientes = conexao.cursor.fetchall()

            for cliente in clientes:
                print("======================")
                print("ID:", cliente[0])
                print("NOME:", cliente[1])
                print("CPF:", cliente[2])
                print("FONE:", cliente[3])
                print("======================")

        except conexao.error as ex:
            print(ex)

    @staticmethod
    def ler_cliente():
        try:
            while True:
                nome = input("Informe o Nome:")
                conexao.cursor.execute(f"SELECT * FROM clientes WHERE Nome='{nome}'")
                cliente = conexao.cursor.fetchall()
                if cliente:
                    for cliente in cliente:
                        print("======================")
                        print("ID:", cliente[0])
                        print("NOME:", cliente[1])
                        print("CPF:", cliente[2])
                        print("FONE:", cliente[3])
                        print("======================")
                    break
                else:
                    print("cliente não encontrado!")
                    print("1. Ler clientes Cadastrados")
                    print("2. Procurar cliente.")
                    print("3. sair")
                    perg = input("Oque Deseja Fazer:")
                    if perg == "1":
                        CrudClientes().ler_clientes()
                    elif perg == "2":
                        pass
                    elif perg == "3":
                        break
                    else:
                        print("Opção Inválida.")
        except conexao.error as ex:
            print(ex)

    @staticmethod
    def atualizar_cliente():
        try:
            while True:
                nome = str(input("Informe o Nome:"))
                cliente = conexao.cursor.execute(
                    f"SELECT * FROM clientes WHERE Nome='{nome}'"
                ).fetchone()
                if cliente:
                    break
                else:
                    print("Usuário não encontrado.")

            if cliente:
                print("======================")
                print("ID:", cliente[0])
                print("NOME:", cliente[1])
                print("CPF:", cliente[2])
                print("FONE:", cliente[3])
                print("======================")

                while True:
                    print(
                        "Digite os novos DADOS de cliente (ou deixe em branco para manter o valor atual):"
                    )
                    novo_nome = input(f"Novo Nome ({cliente[1]})")
                    novo_cpf = input(f"Novo CPF ({cliente[2]})")
                    novo_fone = input(f"Novo Telefone ({cliente[3]})")

                    novo_nome = novo_nome if novo_nome else cliente[1]
                    novo_cpf = novo_cpf if novo_cpf else cliente[2]
                    novo_fone = novo_fone if novo_fone else cliente[3]

                    if not novo_nome.isalpha():
                        if novo_nome.strip():
                            pass
                        print("ERROR!O nome deve conter apenas letras.")
                    elif not novo_cpf.isdigit():
                        if novo_cpf.strip():
                            pass
                        print("ERROR!O CPF deve conter apenas Números.")
                    elif len(novo_cpf) != 11:
                        print("ERROR!CPF Inválido.")
                    elif not novo_fone.isdigit():
                        if novo_fone.strip():
                            pass
                        print("ERROR!O Telefone deve conter apenas númereos.")
                    elif len(novo_fone) != 11:
                        print("ERROR!Telefone inválido.")
                    else:
                        conexao.cursor.execute(
                            f"UPDATE clientes SET Nome='{novo_nome}' , CPF={novo_cpf},Fone={novo_fone} WHERE Nome='{nome}'"
                        )
                        conexao.banco.commit()
                        print("Cliente Atualizado com sucesso!")
                        break
        except conexao.error as ex:
            print(ex)
        except ValueError:
            print("Erro: ID Inválido.")

    @staticmethod
    def deleta_cliente():
        try:
            while True:
                id = input("Informe o ID:")
                conexao.cursor.execute(f"SELECT * FROM clientes WHERE id={id}")
                cliente = conexao.cursor.fetchall()

                if cliente:
                    for cliente in cliente:
                        print("======================")
                        print("ID:", cliente[0])
                        print("NOME:", cliente[1])
                        print("CPF:", cliente[2])
                        print("FONE:", cliente[3])
                        print("======================")
                        break
                    perg = str(
                        input(f"Deseja Deletar o cadastro do cliente (S/N):")
                    ).lower()
                    if perg == "s":
                        conexao.cursor.execute(f"DELETE FROM clientes WHERE id={id}")
                        conexao.banco.commit()
                        print("Cliente Deletado com Sucesso.")
                    break
                else:
                    print("Cliente não encontrado")
                    print("Oque deseja fazer:")
                    print("1. Tentar De novo.")
                    print("2. Lista Clientes.")
                    print("3. Sair")
                    perg = input("Selecione a opção.")
                    if perg == "1":
                        pass
                    elif perg == "2":
                        CrudClientes().ler_clientes()
                    elif perg == "3":
                        print("============================")
                        break
                    else:
                        print("Opção inválida.")

        except ValueError:
            print("Erro: ID inválido.")

    def crud_execute_usuario(self):
        while True:
            print("1. Cadastrar Novo Cliente.")
            print("2. Alterar Dados do CLiente.")
            print("3. Lista Livros")
            print("4. Pesquisar Livro")
            print("5. Sair")
            perg = input("Selecione a opção:")
            print("==" * len("Cadastrar Novo Cliente."))

            if perg == "1":
                self.criar_clientes()
            elif perg == "2":
                self.atualizar_cliente()
            elif perg == "3":
                CrudLivros().ler_livros()
            elif perg == "4":
                CrudLivros().ler_livro()
            elif perg == "5":
                break
