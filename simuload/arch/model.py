from simuload.utils.simuload_database import Database


class Model:
    def __init__(self):
        super().__init__()
        self.start_database()

    def start_database(self):
        self.database = Database()

    def inserir_equipamento(self, equipamento):
        """Adiciona uma nova linha na tabela.
        :param equipamento (tuple): Tupla contendo os dados.
        """
        sql = """
        INSERT INTO equipamentos (nome, potencia,fator_potencia,uso_diario)
        VALUES (?, ?, ?, ?)"""

        try:
            self.database.cur.execute(sql, equipamento)
        except Exception as e:
            print("\n[x] Falha ao inserir registro [x]\n")
            print(f"[x] Revertendo operação (rollback) [x]: {e}\n")
            # rollback reverte/desfaz a operação.
            self.database.con.rollback()
        else:
            # commit registra a operação/transação no banco.
            self.database.con.commit()
            print("\n[!] Registro inserido com sucesso [!]\n")
        return self.database.cur.lastrowid

    def consultar_equipamento_pela_id(self, rowid):
        """Consulta registro pela id.
        :param rowid (int): id do usuário que se deseja consultar.
        :return: É retornada uma tupla (tuple) com os dados.
        Caso o registro não seja localizado é retornado ``None``.
        """
        return self.database.cur.execute(
            """SELECT * FROM equipamentos WHERE rowid=?""", (rowid,)
        ).fetchone()

    def consultar_equipamentos_registros_nome(self, nome):
        """Consulta todos os registros da tabela pelo nome.
        :return: É retornada uma lista (list) de tuplas (tuple)
        contendo os dados.
        Se não houver dados é retornada uma lista vazia [``[]``].
        """
        return self.database.cur.execute(
            """SELECT * FROM equipamentos WHERE nome LIKE ?""", ("%" + nome + "%",)
        ).fetchall()

    def modificar_equipamento(self, rowid, equipamento):
        """Alterar uma linha da tabela com base na id.
        A query está configurada para alterar apenas o nome e sexo.
        :param rowid (int): id da linha que se deseja alterar.
        :param equipamento (tuple): Tupla contendo os dados.

        """
        try:
            self.database.cur.execute(
                """UPDATE equipamentos SET nome=?, potencia=?,fator_potencia=?, uso_diario=?
        WHERE rowid=?""",
                (*equipamento, rowid),
            )
        except Exception as e:
            print("\n[x] Falha na alteração do registro [x]\n")
            print(f"[x] Revertendo operação (rollback) [x]: {e}\n")
            self.database.con.rollback()
        else:
            self.database.con.commit()
            print("\n[!] Registro alterado com sucesso [!]\n")

    def remover_equipamento(self, rowid):
        """Remove uma linha da tabela com base na id da linha.
        :param rowid (id): id da linha que se deseja remover.
        """
        try:
            self.database.cur.execute(
                f"""DELETE FROM equipamentos WHERE rowid=?""", (rowid,)
            )
        except Exception as e:
            print("\n[x] Falha ao remover registro [x]\n")
            print(f"[x] Revertendo operação (rollback) [x]: {e}\n")
            self.con.rollback()
        else:
            self.database.con.commit()
            print("\n[!] Registro removido com sucesso [!]\n")

    def inserir_carga(self, carga):
        """Adiciona uma nova linha na tabela.
        :param cargas (tuple): Tupla contendo os dados.
        """
        sql = """
        INSERT INTO cargas (nome)
        VALUES (?)"""

        try:
            self.database.cur.execute(sql, (carga,))
        except Exception as e:
            print("\n[x] Falha ao inserir registro [x]\n")
            print(f"[x] Revertendo operação (rollback) [x]: {e}\n")
            # rollback reverte/desfaz a operação.
            self.database.con.rollback()
        else:
            # commit registra a operação/transação no banco.
            self.database.con.commit()
            print("\n[!] Registro inserido com sucesso [!]\n")
        return self.database.cur.lastrowid

    def consultar_carga_pela_id(self, rowid):
        """Consulta registro pela id.
        :param rowid (int): id do usuário que se deseja consultar.
        :return: É retornada uma tupla (tuple) com os dados.
        Caso o registro não seja localizado é retornado ``None``.
        """
        return self.database.cur.execute(
            """SELECT * FROM cargas WHERE rowid=?""", (rowid,)
        ).fetchone()

    def consultar_cargas_registros_nome(self, nome):
        """Consulta todos os registros da tabela pelo nome.
        :return: É retornada uma lista (list) de tuplas (tuple)
        contendo os dados.
        Se não houver dados é retornada uma lista vazia [``[]``].
        """
        return self.database.cur.execute(
            """SELECT * FROM cargas WHERE nome LIKE ?""", ("%" + nome + "%",)
        ).fetchall()

    def modificar_carga(self, rowid, carga):
        """Alterar uma linha da tabela com base na id.
        A query está configurada para alterar apenas o nome e sexo.
        :param rowid (int): id da linha que se deseja alterar.
        :param equipamento (tuple): Tupla contendo os dados.

        """
        try:
            self.database.cur.execute(
                """UPDATE cargas SET nome=?
                WHERE rowid=?""",
                (carga, rowid),
            )
        except Exception as e:
            print("\n[x] Falha na alteração do registro [x]\n")
            print(f"[x] Revertendo operação (rollback) [x]: {e}\n")
            self.database.con.rollback()
        else:
            self.database.con.commit()
            print("\n[!] Registro alterado com sucesso [!]\n")

    def remover_carga(self, rowid):
        """Remove uma linha da tabela com base na id da linha.
        :param rowid (id): id da linha que se deseja remover.
        """
        try:
            self.database.cur.execute(f"""DELETE FROM cargas WHERE rowid=?""", (rowid,))
        except Exception as e:
            print("\n[x] Falha ao remover registro [x]\n")
            print(f"[x] Revertendo operação (rollback) [x]: {e}\n")
            self.con.rollback()
        else:
            self.database.con.commit()
            print("\n[!] Registro removido com sucesso [!]\n")

    def consultar_carga_equipamentos(self, carga_id):
        return self.database.cur.execute(
            """SELECT * FROM cargas
            WHERE rowid=?
            INNER JOIN carga_equipamento ON carga.id = carga_equipamento.carga_id
            INNER JOIN equipamentos ON carga_equipamento.equipamento_id = equipamento.id;
            """,
            (carga_id,),
        ).fetchone()

    def inserir_equipamento_na_carga(self, carga_id, equip_id, qtd):
        """Adiciona uma nova linha na tabela.
        :param cargas (tuple): Tupla contendo os dados.
        """
        sql = """
        INSERT INTO carga_equipamento (carga_id, equipamento_id, equipamento_qtd)
        VALUES (?, ?, ?)"""

        try:
            self.database.cur.execute(
                sql,
                (
                    carga_id,
                    equip_id,
                    qtd,
                ),
            )
        except Exception as e:
            print("\n[x] Falha ao inserir registro [x]\n")
            print(f"[x] Revertendo operação (rollback) [x]: {e}\n")
            # rollback reverte/desfaz a operação.
            self.database.con.rollback()
        else:
            # commit registra a operação/transação no banco.
            self.database.con.commit()
            print("\n[!] Registro inserido com sucesso [!]\n")
        return self.database.cur.lastrowid

    def remover_equip_na_carga(self,carga_id):
        """Remove uma linha da tabela com base na id da linha.
        :param rowid (id): id da linha que se deseja remover.
        """
        try:
            self.database.cur.execute(f"""DELETE FROM carga_equipamento WHERE carga_id=?""", (carga_id,))
        except Exception as e:
            print("\n[x] Falha ao remover registro [x]\n")
            print(f"[x] Revertendo operação (rollback) [x]: {e}\n")
            self.con.rollback()
        else:
            self.database.con.commit()
            print("\n[!] Registro removido com sucesso [!]\n")
        
    def last_id_table(self, table):
        try:
            cursor = self.database.cur.execute("SELECT max(id) FROM carga_equipamento")
            return cursor.fetchone()[0]
        except Exception as e:
            print("\n[x] Falha ao detectar id [x]\n")
            print(f"[x] Revertendo operação (rollback) [x]: {e}\n")
            # rollback reverte/desfaz a operação.
            self.database.con.rollback()
        else:
            # commit registra a operação/transação no banco.
            self.database.con.commit()

    def close_connection(self):
        self.database.con.close()
