from funcionarios import CrudFuncionario
from clientes import CrudClientes

while True:
    print("============================================================")
    print("                      BIBLIOTECA                               ")
    print("============================================================")

    print("1. Funcionario.")
    print("2. Cliente")
    print("3. sair")
    perg = input("Qual área de trabalho deseja acessar:")
    print("==============================================")

    if perg == "1":
        CrudFuncionario().crud_execute_funcionario()
    elif perg == "2":
        CrudClientes().crud_execute_usuario()
    elif perg == "3":
        break
    else:
        print("opção invalida!")
