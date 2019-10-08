import sqlite3

from sqlite3 import Error
from aula6_conexoes import Conexoes

def main():

    dbfile = r"C:\Users\Usuario\Documents\Python\Database\clientes.db"

    sql_drop_table_clientes = """ DROP TABLE clientes"""
    oConexoes = Conexoes(dbfile)
    conn = oConexoes.create_connection()

    if conn is not None:
        oConexoes.drop_table(sql_drop_table_clientes)
    else:
        print("Erro ao excluir o banco de dados")

if __name__ == '__main__':
    main()