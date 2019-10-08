import sqlite3
from sqlite3 import Error

class Conexoes:

    def __init__(self, dbfile):
        self.dbfile = dbfile
        self.conn = ""
        self.listKey = []
        self.listValue = []
        self.success = True

    def create_connection(self):
        """ create a database connection to the SQLite database
            specified by dbfile
        :param dbfile: database file
        :return: Connection object or None
        """
        try:
            self.conn = sqlite3.connect(self.dbfile)
            return self.conn
        except Error as e:
            print(e)
        return self.conn

    def create_table(self, create_table_sql):
        """" create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def drop_table(self, drop_table_sql):
        try:
            c = self.conn.cursor()
            c.execute(drop_table_sql)
        except Error as e:
            print(e)

    def insert_data(self, data):

        self.mapper(data)
        key_len = len(self.listKey)
        value_len = len(self.listValue)

        insert = "INSERT INTO clientes ("
        for x in self.listKey:
            if self.listKey.index(x) == key_len:
                insert += self.listKey,")"
            else:
                insert += self.listKey,","
        insert += "values ("
        for x in self.listValue:
            if self.listValue.index(x) == value_len:
                insert += self.listKey,")"
            else:
                insert += self.listValue,","
        print(insert)
        try:
            c = self.conn.cursor()
            c.execute(insert)
        except Error as e:
            print(e)

    def mapper(self, data):

        for key,value in data.items():
            self.listKey.append(key)
            self.listValue.append(value)
        if self.listKey == '' and self.listValue == '':
            print("Erro ao mapear campos")
