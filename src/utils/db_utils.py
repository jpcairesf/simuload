import os
import sqlite3

DEFAULT_PATH = './db'
DB_NAME = 'simuload.db'


def criar_diretorio(default_path=DEFAULT_PATH):
    if not os.path.exists(default_path):
        os.makedirs(default_path)
        print("The new directory is created!")
    



def db_connect(db_file=DB_NAME):
    """ create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    
    criar_diretorio()

    try:
        con = sqlite3.connect(os.path.join(DEFAULT_PATH,db_file))
        return con
    except Error as e:
        print(e)

    return None

def create_table(con, create_table_sql):
    """ create a table from the create_table_sql statement
    :param con: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    
    try:
        cur = con.cursor()
        cur.execute(create_table_sql)
    except Exception as e:
        print(e)
    

if __name__=='__main__' :
    db_connect()