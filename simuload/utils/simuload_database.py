from simuload.utils.db_utils import db_connect, create_table

class Database:
    def __init__(self):
        self.con = db_connect()
        self.criar_tabela_equipamentos()        
        
    def criar_tabela_equipamentos(self):
        sql_create_equip_table = """CREATE TABLE IF NOT EXISTS equipamentos (
                                    id integer PRIMARY KEY,
                                    nome text NOT NULL,
                                    potencia float NOT NULL,
                                    fator_potencia float NOT NULL,
                                    uso_diario text NOT NULL,
                                );"""
        if self.con is not None:
            create_table(self.con,sql_create_equip_table)
        else:
            print("Error! cannot create the database connection.")

    def criar_equipamento(self, nome, potencia, fator_potencia, uso_diario):
        sql = """
        INSERT INTO equipamentos (nome, potencia,fator_potencia,uso_diario)
        VALUES (?, ?, ?, ?)"""
        cur = self.con.cursor()
        cur.execute(sql, (nome, potencia, fator_potencia, uso_diario))
        return cur.lastrowid
    
