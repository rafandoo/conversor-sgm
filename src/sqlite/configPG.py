import sqlite3
import logging

class ConfigPG():
    def __init__(self, database='config', cursor=None):
        self.__database = 'db/' + database + '.db'
        self.__conn = None
        self.__cursor = cursor

    def connect(self):
        self.__conn = sqlite3.connect(self.__database)

    def cursor(self):
        return self.__conn.cursor()
    
    def closeConn(self):
        self.__conn.close()

    def commit(self):
        self.__conn.commit()

    def createTables(self):
        self.__cursor.execute('''
            CREATE TABLE IF NOT EXISTS pg_configuracao_fiscal (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                descricao TEXT,
                tipo CHAR(1),
                cod_empresa INTEGER,
                codigo_fiscal TEXT,
                prioridade INTEGER,
                finalidade CHAR(1),
                cod_aliquota TEXT,
                cst CHAR(3)
            )
        ''')

        self.__cursor.execute('''
            CREATE TABLE IF NOT EXISTS pg_configuracao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chave TEXT UNIQUE,  
                valor TEXT
            )
        ''')

    def insertConfig(self):
        configs = {
            'CLIENTE_PAIS': 'BRASIL',
            'CLIENTE_ESTADO': 'SC',
            'TIPO_LANCAMENTO_FINANCEIRO': '65-1',
            'ESPECIE_LANCAMENTO_FINANCEIRO': '3-1',
            'PLANO_DE_CONTAS_DEBITO': '54-1',
            'PLANO_DE_CONTAS_CREDITO': '150-1',
        }
        for chave, valor in configs.items():
            try:
                self.__cursor.execute('INSERT INTO pg_configuracao (chave, valor) VALUES (?, ?)', (chave, valor))
            except Exception as e:
                logging.error(e)
    
        config_fiscal = {
            1: [
                1,
                'PROPRIAS - TRIBUTADO - ICMS 12% CST 000',
                'G',
                '1',
                '35-1',
                '1',
                'P',
                '02', # 12% ICMS
                '000'
            ],
            2: [
                2,
                'PROPRIAS - TRIBUTADO - ICMS 17% CST 000',
                'G',
                '1',
                '13-1',
                '1',
                'P',
                '03', # 17% ICMS
                '000'
            ],
            3: [
                3,
                'PROPRIAS - TRIBUTADO - ICMS 25% CST 000',
                'G',
                '1',
                '36-1',
                '1',
                'P',
                '04', # 25% ICMS
                '000'
            ],
            4: [
                4,
                'PROPRIAS - SUB. TRIB. - MERCADORIAS - ICMS 0% CST 060',
                'G',
                '1',
                '15-1',
                '1',
                'P',
                '06', # ICMS ST
                '060'
            ],
            5: [
                5,
                'PROPRIAS - TRIBUTADO - ICMS I CST 040',
                'G',
                '1',
                '21-1',
                '1',
                'P',    
                '05', # ICMS I
                '040'
            ],
            6: [
                6,
                'PROPRIAS - TRIBUTADO - ISSQN 5% CST 000',
                'G',
                '1',
                '37-1',
                '1',
                'P',
                '07', # ISSQN 5%
                '000'
            ],
            7: [
                7,
                'PROPRIAS - NÃO TRIBUTADA - ICMS 0% CST 041',
                'G',
                '1',
                '39-1',
                '1',
                'P',
                '08', # ICMS NT
                '041'
            ],
            8: [
                8,
                'PROPRIAS - TRIBUTADO - ICMS 10% CST 000',
                'G',
                '1',
                '40-1',
                '1',
                'P',
                '11', # ICMS 10%
                '000'
            ],
            9: [
                9,
                'PROPRIAS - TRIBUTADO - ICMS 7% CST 000',
                'G',
                '1',
                '41-1',
                '1',
                'P',
                '01', # ICMS 7%
                '000'
            ],
            10: [
                10,
                'PROPRIAS - TRIBUTADO - ICMS 4% CST 000',
                'G',
                '1',
                '42-1',
                '1',
                'P',
                '12', # ICMS 4%
                '000'
            ],
            100: [
                100,
                'PROPRIAS - PIS 0,65% CST 01 - COFINS 3% CST 01 - CUMULATIVO - LUCRO PRESUMIDO',
                'G',
                '1',
                '14-1',
                '2',
                'P',
                '00', # PIS/COFINS
                '000'
            ],
            101: [
                101,
                'PROPRIAS - PIS 0,65% CST 01 - COFINS 3% CST 01 - CUMULATIVO - LUCRO PRESUMIDO',
                'G',
                '1',
                '14-1',
                '2',
                'P',
                '00', # PIS/COFINS
                '060'
            ],
            200: [
                200,
                'TERCEIROS - ICMS CST 060',
                'G',
                '1',
                '1-1',
                '1',
                'T',
                '00', # NORMAL
                '060'
            ],
            201: [
                201,
                'TERCEIROS - ICMS CST 000',
                'G',
                '1',
                '4-1',
                '1',
                'T',
                '00', # NORMAL
                '000'
            ],
            202: [
                202,
                'TERCEIROS - COFINS 3% CST 50 - PIS 0,65% CST 50 - CUMULATIVO - LUCRO PRESUMIDO',
                'G',
                '1',
                '3-1',
                '2',
                'T',
                '00', # NORMAL
                '000'
            ]
        }

        for chave, valor in config_fiscal.items():
            try:
                self.__cursor.execute('INSERT INTO pg_configuracao_fiscal (id ,descricao, tipo, cod_empresa, codigo_fiscal, prioridade, finalidade, cod_aliquota, cst) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (valor[0], valor[1], valor[2], valor[3], valor[4], valor[5], valor[6], valor[7], valor[8]))
            except Exception as e:
                logging.error(e)
