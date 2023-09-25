import logging
import time

class Converter:
    def __init__(self, cursor, queryMaker, sgm, internalDatabase):
        self.__cursor = cursor
        self.__qm = queryMaker
        self.__sgm = sgm
        self.__idb = internalDatabase

    def __convert(self, rows, table):
        start = time.time()
        count = 0
        for row in rows:
            try:
                self.__sgm.inserts(table, row)
                self.__idb.commit()
                count += 1
            except Exception as e:
                logging.error('Erro ao inserir *{}*: {} | {}'.format(table, str(e), str(row)))
        end = time.time()
        logging.info('Inserido: {} registros - tabela: *{}*'.format(str(count), table))
        logging.info('Tempo de execução: {:.2f} segundos'.format(end - start))


    def produtos(self):
        self.__cursor.execute(self.__qm.simple(table=self.__sgm.getTable('produtos'), order='procod', cols=self.__sgm.getListComma('produtos')))
        self.__convert(self.__cursor.fetchall(), 'produtos')

    def produtosBarras(self):
        self.__cursor.execute(self.__qm.simple(table=self.__sgm.getTable('produtos_barras'), order='procod', cols=self.__sgm.getListComma('produtos_barras')))
        self.__convert(self.__cursor.fetchall(), 'produtos_barras')

    def bombas(self):
        self.__cursor.execute(self.__qm.simple(table=self.__sgm.getTable('bombas'), order='bomcod', cols=self.__sgm.getListComma('bombas')))
        self.__convert(self.__cursor.fetchall(), 'bombas')

    def frota(self):
        self.__cursor.execute(self.__qm.simple(table=self.__sgm.getTable('frota'), order='clicod', cols=self.__sgm.getListComma('frota')))
        self.__convert(self.__cursor.fetchall(), 'frota')

    def grupos(self):
        self.__cursor.execute(self.__qm.simple(table=self.__sgm.getTable('grupos'), order='grucod', cols=self.__sgm.getListComma('grupos')))
        self.__convert(self.__cursor.fetchall(), 'grupos')

    def tributos(self):
        self.__cursor.execute(self.__qm.simple(table=self.__sgm.getTable('tributos'), order='tricod', cols=self.__sgm.getListComma('tributos')))
        self.__convert(self.__cursor.fetchall(), 'tributos')

    def fornecedores(self):
        self.__cursor.execute(self.__qm.simple(table=self.__sgm.getTable('fornecedores'), order='forcod', cols=self.__sgm.getListComma('fornecedores')))
        self.__convert(self.__cursor.fetchall(), 'fornecedores')

    def funcionarios(self):
        self.__cursor.execute(self.__qm.simple(table=self.__sgm.getTable('funcionarios'), order='funcod', cols=self.__sgm.getListComma('funcionarios')))
        self.__convert(self.__cursor.fetchall(), 'funcionarios')

    def clientes(self):
        self.__cursor.execute(self.__qm.simple(table=self.__sgm.getTable('clientes'), order='clicod', cols=self.__sgm.getListComma('clientes')))
        self.__convert(self.__cursor.fetchall(), 'clientes')

    def tanques(self):
        self.__cursor.execute(self.__qm.simple(table=self.__sgm.getTable('tanques'), order='tancod', cols=self.__sgm.getListComma('tanques')))
        self.__convert(self.__cursor.fetchall(), 'tanques')

    def cidade(self):
        self.__cursor.execute(self.__qm.simple(table=self.__sgm.getTable('cidade'), order='cidcod', cols=self.__sgm.getListComma('cidade')))
        self.__convert(self.__cursor.fetchall(), 'cidade')