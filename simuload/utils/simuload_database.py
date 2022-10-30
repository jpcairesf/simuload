from simuload.utils.db_utils import db_connect, setup_database


class Database:
    def __init__(self):
        self.con = db_connect()
        self.cur = self.con.cursor()
        setup_database(self.con)

    def close_connection(self):
        self.con.close()


if __name__ == "__main__":

    banco = Database()
    res = banco.consultar_equipamentos_registros_nome("")
    print(res)
    banco.close_connection()
