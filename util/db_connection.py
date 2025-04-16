import pyodbc
from util.db_property import PropertyUtil

class DBConnection:
    connection = None

    @staticmethod
    def get_connection():
        if DBConnection.connection is None:
            try:
                props = PropertyUtil.get_property_string("db.properties")
                conn_str = (
                    f"DRIVER={{SQL Server}};"
                    f"SERVER={props['server']};"
                    f"DATABASE={props['database']};"
                    f"UID={props['username']};"
                    f"PWD={props['password']};"
                    f"Trusted_Connection=yes;"
                )
                return pyodbc.connect(conn_str)
            except Exception as e:
                raise ConnectionError(f"Failed to connect to the database: {e}")
