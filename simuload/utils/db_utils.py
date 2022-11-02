import os
import sqlite3

DEFAULT_PATH = "./db"
DB_NAME = "simuload.db"


def criar_diretorio(default_path=DEFAULT_PATH):
    if not os.path.exists(default_path):
        os.makedirs(default_path)
        print("The new directory is created!")


def db_connect(db_file=DB_NAME):
    """create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """

    criar_diretorio()

    try:
        con = sqlite3.connect(os.path.join(DEFAULT_PATH, db_file))
        return con
    except Exception as e:
        print(e)

    return None


def create_table(con, create_table_sql):
    """create a table from the create_table_sql statement
    :param con: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """

    try:
        cur = con.cursor()
        cur.execute(create_table_sql)
    except Exception as e:
        print(e)


def criar_tabela_equipamentos(con):
    sql_create_equip_table = """CREATE TABLE IF NOT EXISTS Equipamentos (
                                    EquipamentoId INTEGER PRIMARY KEY,
                                    EquipamentoNome TEXT NOT NULL,
                                    EquipamentoPotencia REAL NOT NULL,
                                    EquipamentoFP REAL NOT NULL,
                                    EquipamentoUsoDiario TEXT NOT NULL
                                )"""
    if con is not None:
        create_table(con, sql_create_equip_table)
    else:
        print("Error! cannot create the database connection.")


def criar_tabela_cargas(con):
    sql_create_carga_table = """CREATE TABLE IF NOT EXISTS Cargas (
                                    CargaId integer PRIMARY KEY,
                                    CargaNome text NOT NULL
                                );"""
    if con is not None:
        create_table(con, sql_create_carga_table)
    else:
        print("Error! cannot create the database connection.")


def criar_tabela_carga_equipamento(con):
    sql_create_carga_table = """CREATE TABLE IF NOT EXISTS CargaEquipamento (
                                    CargaEquipamentoId integer PRIMARY KEY,
                                    CargaId INTEGER NOT NULL,
                                    EquipamentoId INTEGER NOT NULL,
                                    EquipamentoQtd INTEGER NOT NULL,
                                    FOREIGN KEY (CargaId) REFERENCES Cargas (CargaId),
                                    FOREIGN KEY (EquipamentoId) REFERENCES Equipamentos (EquipamentoId)
                                );"""
    if con is not None:
        create_table(con, sql_create_carga_table)
    else:
        print("Error! cannot create the database connection.")


def setup_database(con):
    criar_tabela_equipamentos(con)
    criar_tabela_cargas(con)
    criar_tabela_carga_equipamento(con)


if __name__ == "__main__":
    db_connect()
