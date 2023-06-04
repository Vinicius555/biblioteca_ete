"""import sqlite3
from datetime import datetime

# Conectando ao banco de dados SQLite
conn = sqlite3.connect("exemplo.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS tabela_exemplo (data_nascimento VARCHAR(8))")

# Obtendo a data de nascimento do usuário
data_nascimento_str = input(
    f"Digite a data de nascimento (formato: {data}/{mes}/{ano}):"
)
dia,mes,ano = 

# Convertendo a string em um objeto datetime
data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")

# Formatando a data no formato aaaa-mm-dd
data_nascimento_sqlite = data_nascimento.strftime("%Y-%m-%d")

# Executando a consulta SQL para inserir a data de nascimento formatada
cursor.execute(
    "INSERT INTO tabela_exemplo (data_nascimento) VALUES (?)", (data_nascimento_sqlite,)
)

# Salvando as alterações no banco de dados
conn.commit()

# Fechando a conexão com o banco de dados
conn.close()"""


print("=-" * ((len("Funcionário cadastrado com sucesso!"))))
frase = "Funcionário cadastrado com sucesso!"
espacos = (80 - len(frase)) // 2
print(" " * espacos + frase)
print("=-" * ((len("Funcionário cadastrado com sucesso!"))))
