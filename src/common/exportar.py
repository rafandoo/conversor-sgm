import pandas as pd

class Exportar:
    def __init__(self, conn):
        self.__conn = conn

    def __export(self, query, filename):
        filename = 'export/' + filename + '.xlsx'
        df = pd.read_sql(query, self.__conn)
        df.to_excel(filename, index=False)

    def grupos(self):
        query = 'SELECT * FROM grupos'
        self.__export(query, 'grupos')

    def tanques(self):
        query = 'SELECT * FROM tanques'
        self.__export(query, 'tanques')
    
    def bombas(self):
        query = 'SELECT * FROM bombas'
        self.__export(query, 'bombas')
    
    def clientes(self):
        query = 'SELECT * FROM clientes'
        self.__export(query, 'clientes')

    def fornecedores(self):
        query = 'SELECT * FROM fornecedores'
        self.__export(query, 'fornecedores')

    def produtos(self):
        query = '''
            SELECT p.*, 
                (SELECT GROUP_CONCAT(codigo_barras, ',') 
                FROM produtos_barras pb 
                WHERE pb.codigo = p.codigo 
                GROUP BY pb.codigo) AS codigo_barras
            FROM produtos p
        '''
        self.__export(query, 'produtos')


    def produtosBarras(self):
        query = 'SELECT * FROM produtos_barras'
        self.__export(query, 'produtos_barras')

    def frota(self):
        query = 'SELECT * FROM frota'
        self.__export(query, 'frota')
    
    def tributos(self):
        query = 'SELECT * FROM tributos'
        self.__export(query, 'tributos')

    def funcionarios(self):
        query = 'SELECT * FROM funcionarios'
        self.__export(query, 'funcionarios')

    # def cfgFiscalProdutos(self):
    #     configFiscal = pd.read_sql('SELECT * FROM pg_configuracao_fiscal', self.conn)
    #     produtos = pd.read_sql('SELECT codigo FROM produtos_completos', self.conn)
    #     export = pd.DataFrame(columns=['codigo', 'tipo', 'cod_empresa', 'codigo_fiscal', 'prioridade', 'finalidade'])
    #     for i in produtos['codigo']:
    #         for index, row in configFiscal.iterrows():
    #             export.loc[len(export)] = [i, row['tipo'], row['cod_empresa'], row['codigo_fiscal'], row['prioridade'], row['finalidade']]
    #     export.to_excel('configFiscalProdutos.xlsx', index=False)
