import sqlite3
import json
import requests

from sqlite3 import Error
from aula6_conexoes import Conexoes

def main():

    dbfile = r"C:\Users\Usuario\Documents\Python\Database\clientes.db"

    sql_create_table_clientes = """ CREATE TABLE clientes(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    Nome VARCHAR(100) NOT NULL,
                                    CPF VARCHAR(11) NOT NULL,
                                    Email VARCHAR(20) NOT NULL,
                                    Fone VARCHAR(20),
                                    UF VARCHAR(2) NOT NULL
                                    );"""
    oConexoes = Conexoes(dbfile)

    conn = oConexoes.create_connection()

    if conn is not None:
        oConexoes.create_table(sql_create_table_clientes)
    else:
        print("Erro ao criar o banco de dados")

if __name__ == '__main__':
    main()
