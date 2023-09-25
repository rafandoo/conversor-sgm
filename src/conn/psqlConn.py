import psycopg2


class Postgres():
    def __init__(self, database='', host='localhost', port=5450, user='postgres', password='19983101'):
        self.__database = database
        self.__host = host
        self.__port = port
        self.__user = user
        self.__password = password

    def connect(self):
        self.__conn = psycopg2.connect(
            host=self.__host,
            database=self.__database,
            port=self.__port,
            user=self.__user,
            password=self.__password,
        )

    def cursor(self):
        return self.__conn.cursor()

    def closeConn(self):
        self.__conn.close()
