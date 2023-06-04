import conexao


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
                elif cpf != 11:
                    print("ERROR!Tamanaho do CPF inválido.")
                else:
                    break
            while True:
                fone = input("FONE:")
                if not fone.isdigit():
                    print("ERROR!Digite apenas Números.")
                elif fone != 11:
                    print("ERROR!Esse número não existi.")
                else:
                    break
        except conexao.error as ex:
            print(ex)
        else:
            conexao.cursor.execute(
                f"INSERT INTO clientes VALUES (NULL,'{nome}',{cpf},{fone})"
            )

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

    def ler_cliente(self, id):
        try:
            id = int(id)
            conexao.cursor.execute(f"SELECT * FROM clientes WHERE id={id}")
            cliente = conexao.cursor.fetchall()

            return cliente

        except conexao.error as ex:
            print(ex)

    @staticmethod
    def atualizar_cliente(id):
        try:
            id = int(input("Informe o ID:"))
            cliente = conexao.cursor.execute(f"SELECT * FROM clientes WHERE id={id}")

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
                        print("ERROR!O nome deve conter apenas letras.")
                    elif not novo_cpf.isdigit():
                        print("ERROR!O CPF deve conter apenas Números.")
                    elif novo_cpf != 11:
                        print("ERROR!CPF Inválido.")
                    elif not novo_fone.isdigit():
                        print("ERROR!O Telefone deve conter apenas númereos.")
                    elif novo_fone != 11:
                        print("ERROR!Telefone inválido.")
                    else:
                        conexao.cursor.execute(
                            f"UPDDATE clientes SET Nome='{novo_nome}' , CPF={novo_cpf},Fone={novo_fone} WHERE id={id}"
                        )
                        conexao.banco.commit()
                        print("Cliente Atualizado com sucesso!")
                        break
        except conexao.error as ex:
            print(ex)
        except ValueError:
            print("Erro: ID Inválido.")

    def deleta_cliente(self, id):
        try:
            id = int(input("Informe o ID:"))
            cliente = self.ler_cliente(id)

            if cliente and len(cliente) > 0:
                print("======================")
                print("ID:", cliente[0])
                print("NOME:", cliente[1])
                print("CPF:", cliente[2])
                print("FONE:", cliente[3])
                print("======================")
            else:
                print("Cliente não encontrado")
            perg = str(input(f"Deseja Deletar o cadastro do cliente (S/N):")).lower()
            if perg == "s":
                conexao.cursor.execute(f"DELETE FROM clientes WHERE id={id}")
                conexao.banco.commit()
                print("Cliente Deletado com Sucesso.")
            else:
                pass

        except ValueError:
            print("Erro: ID inválido.")
