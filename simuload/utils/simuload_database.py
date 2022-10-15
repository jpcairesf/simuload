from simuload.utils.db_utils import db_connect, create_table, setup_database

class Database:
    def __init__(self):
        self.con = db_connect()
        self.cur = self.con.cursor()
        setup_database(self.con)      
        
    def inserir_equipamento(self, equipamento):
        """Adiciona uma nova linha na tabela.
        :param equipamento (tuple): Tupla contendo os dados.
        """
        sql = """
        INSERT INTO equipamentos (nome, potencia,fator_potencia,uso_diario)
        VALUES (?, ?, ?, ?)"""
        
        try:
            self.cur.execute(sql,equipamento)
        except Exception as e:
            print('\n[x] Falha ao inserir registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            # rollback reverte/desfaz a operação.
            self.con.rollback()
        else:
            # commit registra a operação/transação no banco.
            self.con.commit()
            print('\n[!] Registro inserido com sucesso [!]\n')
        return self.cur.lastrowid
    
    def consultar_equipamento_pela_id(self, rowid):
        """Consulta registro pela id.
        :param rowid (int): id do usuário que se deseja consultar.
        :return: É retornada uma tupla (tuple) com os dados.
        Caso o registro não seja localizado é retornado ``None``.
        """
        return self.cur.execute('''SELECT * FROM equipamentos WHERE rowid=?''', (rowid,)).fetchone()
    
    def consultar_equipamentos_registros_nome(self,nome, limit=10):
        """Consulta todos os registros da tabela pelo nome.
        Utilizando ``limit`` para evitar consultas longas de mais.
        :param limit (int): Parâmetro que limita a
        quantidade de registros que serão exibidos.
        :return: É retornada uma lista (list) de tuplas (tuple)
        contendo os dados.
        Se não houver dados é retornada uma lista vazia [``[]``].
        """
        return self.cur.execute('''SELECT * FROM equipamentos WHERE nome LIKE ? LIMIT ?''', ('%'+nome+'%', limit)).fetchall()
    
    def modificar_equipamento(self, rowid, equipamento):
        """Alterar uma linha da tabela com base na id.
        A query está configurada para alterar apenas o nome e sexo.
        :param rowid (int): id da linha que se deseja alterar.
        :param equipamento (tuple): Tupla contendo os dados.

        """
        try:
            self.cur.execute(
                '''UPDATE equipamentos SET nome=?, potencia=?,fator_potencia=?, uso_diario=?
        WHERE rowid=?''', (*equipamento, rowid))
        except Exception as e:
            print('\n[x] Falha na alteração do registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            self.con.rollback()
        else:
            self.con.commit()
            print('\n[!] Registro alterado com sucesso [!]\n')
    
    def remover_equipamento(self, rowid):
        """Remove uma linha da tabela com base na id da linha.
        :param rowid (id): id da linha que se deseja remover.
        """
        try:
            self.cur.execute(
                f'''DELETE FROM equipamentos WHERE rowid=?''', (rowid,))
        except Exception as e:
            print('\n[x] Falha ao remover registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            self.con.rollback()
        else:
            self.con.commit()
            print('\n[!] Registro removido com sucesso [!]\n')
    def close_connection(self):
        self.con.close()
if __name__=='__main__':
    
    banco = Database()
    lampada_60 = ('Lampada 60',60,0.95,'18:23')
    geladeira = ('Geladeira', 500, 0.65, '0:23')
    #banco.inserir_equipamento(geladeira)
    #banco.modificar_equipamento(1, lampada_60)
    #res = banco.consultar_equipamento_pela_id()
    res = banco.consultar_equipamentos_registros_nome('')
    print(res)
    banco.remover_equipamento(2)
    res = banco.consultar_equipamentos_registros_nome('')

    
    print(res)
    banco.close_connection()
        
