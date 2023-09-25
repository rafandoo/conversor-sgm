import sqlite3


class Database:
    def __init__(self, database):
        self.__database = 'db/' + database + '.db'
        self.__conn = None

    def connect(self):
        self.__conn = sqlite3.connect(self.__database)

    def cursor(self):
        return self.__conn.cursor()

    def closeConn(self):
        self.__conn.close()

    def commit(self):
        self.__conn.commit()
