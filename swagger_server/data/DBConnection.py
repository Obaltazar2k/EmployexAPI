import mysql.connector
from mysql.connector import Error


class DBConnection:
    def __init__(self):
        self.user = "root"
        self.password = "Jinchuriki2k"
        self.database = "employex"
        self.host = "localhost"
        self.connection = None

    def connect(self, include_params: bool = False):
        self.connection = mysql.connector.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )
        return self.connection.cursor(prepared=include_params)

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()

    def send_query(self, query, values: list = None):
        executed = False
        if self.host is not None:
            parameters: tuple = ()
            try:
                if values is not None:
                    cursor = self.connect(True)
                    parameters = tuple(values)
                else:
                    cursor = self.connect()
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
                tmp_results = cursor.fetchall()
                for row in tmp_results:
                    results.append(dict(zip(cursor.column_names, row)))
            except Error as error:
                print(f"Problem connecting to the database: {error}")
            finally:
                self.close_connection()
        return results

    def selectObject(self, query, values: list = None, one=False):
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
                #results = cursor.fetchall()
                r = [dict((cursor.description[i][0], value)
                    for i, value in enumerate(row)) for row in cursor.fetchall()]
                return (r[0] if r else None) if one else r
            except Error as error:
                print(f"Problem connecting to the database: {error}")
            finally:
                self.close_connection()
        return results