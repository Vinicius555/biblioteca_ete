import sqlite3
from sqlite3 import Error

error = Error

banco = sqlite3.connect("blibioteca.db")

cursor = banco.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS funcionarios ( id INTEGER PRIMARY KEY AUTOINCREMENT,Nome VARCHAR(100),CPF VARCHAR(11),Email TEXT NOT NULL,Fone VARCHAR(20),UF VARCHAR(2) NOT NULL)"
)
cursor.execute(
    "CREATE TABLE IF NOT EXISTS livros (id INTEGER PRIMARY KEY AUTOINCREMENT,NomeLivro VARCHAR(100) NOT NULL,NomeAutor VARCHAR(100) NOT NULL,AnoLivro VARCHAR(4),Categoria VARCHAR(100))"
)
cursor.execute(
    "CREATE TABLE IF NOT EXISTS clientes ( id INTEGER PRIMARY KEY AUTOINCREMENT,Nome VARCHAR(100) NOT NULL,CPF VARCHAR(11),Fone VARCHAR(20))"
)
