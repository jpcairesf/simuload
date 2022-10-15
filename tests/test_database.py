import pytest

from simuload.utils.simuload_database import Database

# sl_database = None
# def setup_module(module):
#     global sl_database
#     sl_database = Database()

# def test_existencia_tabelas():
#     sql_equipamentos = """SELECT name FROM sqlite_master WHERE name = ?;"""
#     cur = sl_database.con.cursor()  
#     tabelas = ["equipamentos", "cargas"]
#     for tabela in tabelas:
#         res = cur.execute(sql_equipamentos,[tabela])
#         assert res.fetchone() is not None                 