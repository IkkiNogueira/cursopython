from aula6_conexoes import Conexoes

def main():

    dbfile = r"C:\Users\Usuario\Documents\Python\Database\clientes.db"

    sql_insert_clientes = {
        "Nome":"Teste1",
        "CPF":"123789456",
        "Email":"teste@tste.com.br",
        "Fone":"987654321",
        "UF":"SP"
    }

    oConexoes = Conexoes(dbfile)
    conn = oConexoes.create_connection()

    if conn is not None:
        oConexoes.insert_data(sql_insert_clientes)
    else:
        print("Erro ao excluir o banco de dados")

if __name__ == '__main__':
    main()