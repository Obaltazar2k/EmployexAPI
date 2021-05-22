import mysql.connector
from mysql.connector import Error


class DBConnection:
    def __init__(self):
        self.user = "root"
        self.password = "gatodeportivo"
        self.database = "Employex"
        self.host = "localhost"
        #self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()

    def send_query(self, query, values: list = None):
        executed = False
        if self.host is not None:
            parameters: tuple = ()
            if values is not None:
                parameters = tuple(values)
            try:
                self.connect()
                if values is not None:
                    cursor = self.connection.cursor(prepared=True)
                else:
                    cursor = self.connection.cursor()
                cursor.execute(query, parameters)
                self.connection.commit()
                executed = True
            except Error as error:
                print(f"Problem connecting to the database: {error}")
            finally:
                self.close_connection()
        return executed

    def select(self, query, values: list = None):
        results = []
        if self.host is not None:
            parameters: tuple = ()
            if values is not None:
                parameters = tuple(values)
            try:
                self.connect()
                if values is not None:
                    cursor = self.connection.cursor(prepared=True)
                else:
                    cursor = self.connection.cursor()
                cursor.execute(query, parameters)
                results = cursor.fetchall()
            except Error as error:
                print(f"Problem connecting to the database: {error}")
            finally:
                self.close_connection()
        return results