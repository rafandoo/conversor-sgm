class Method():
    def __init__(self, cursor):
        self.__table ={
            'produtos': 'ect001',
            'produtos_barras': 'ect001d',
            'bombas': 'bombas',
            'frota': 'ect002g',
            'grupos': 'ect004',
            'tributos': 'ect010',
            'fornecedores': 'oft003',
            'funcionarios': 'oft006',
            'clientes': 'spt002',
            'tanques': 'tanque',
            'cidade': 'cidade',
        }
        self.__fields = {
            'frota': [
                'clicod',
                'clpplaca',
                'clpmarca',
                'clpultkm',
                'clpativa',
            ],
            'produtos': [
                'procod',
                'prodescric',
                'grucod',
                'proprecusr',
                'proprevist',
                'prounidmed',
                'protipo',
                'tricod',
                'proclafisc',
                'proippt',
                'proiat',
                'proqtdatue',
                'procodanp',
            ],
            'produtos_barras': [
                'procod',
                'pcbsequenc',
                'pcbcodbarr',
            ],
            'grupos': [
                'grucod',
                'grudescric',
            ],
            'bombas': [ 
                'bomcod',
                'tancod',
                'procod',
                'bomcodcomp',
                'bomilhcod',
            ],
            'tributos': [
                'tricod',
                'trides',
                'tbbcod',
                'alicod',
                'natcod',
            ],
            'fornecedores': [
                'forcod',
                'fortippess',
                'fornome',
                'fornomfant',
                'forenderec',
                'forbairro',
                'forcidade',
                'forcep',
                'forcgc',
                'forcpf',
                'forinsesta',
                'fornro1fon',
                'formail',
                'foruf',
                'forendnro',
                'forendcomp'
            ],
            'funcionarios': [
                'funcod',
                'funnome',
                'funativo'
            ],
            'clientes': [
                'spt002.clicod',
                'spt002.clitippess',
                'spt002.cliindativ',
                'spt002.clirazsoci',
                'spt002.clinomfant',
                'spt002.clienderec',
                'spt002.clibairro',
                'spt002.cliuf',
                'spt002.clicep',
                'spt002.clicgc',
                'spt002.cliinsesta',
                'spt002.clinrocpf',
                'spt002.clinroiden',
                'spt002.clinro1fon',
                'spt002.climail',
                'spt002.cliendnro',
                'spt002.cliendcomp',
                'spt002.clicidcod',
            ],
            'tanques': [
                'tancod',
                'taqcaparma',
                'taqativo',
            ],
            'cidade': [
                'cidcod',
                'cidnome',
                'cidcodibge',
            ]
        }
        self.__inserts = {
            'produtos': self.insertProdutos,
            'produtos_barras': self.insertProdutosBarras,
            'bombas': self.insertBombas,
            'frota': self.insertFrota,
            'grupos': self.insertGrupos,
            'tributos': self.insertTributos,
            'fornecedores': self.insertFornecedores,
            'funcionarios': self.insertFuncionarios,
            'clientes': self.insertClientes,
            'tanques': self.insertTanques,
            'cidade': self.insertCidade
        }
        self.__cursor = cursor
        self.__createTables()

    def getListComma(self, key):
        return ', '.join(self.__fields[key])
    
    def getTable(self, key):
        return self.__table[key]
    
    def inserts(self, key, row):
        self.__inserts[key](row)

    def __createTables(self):
        self.__cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                codigo TEXT UNIQUE,
                descricao TEXT,
                codigo_grupo TEXT,
                preco_custo REAL,
                preco_venda REAL,
                unidade_medida TEXT,
                tipo TEXT,
                codigo_tributo TEXT,
                codigo_ncm TEXT,
                ippt TEXT,
                iat TEXT,
                quantidade TEXT,
                anp TEXT
            )
        ''')

        self.__cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos_barras (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                codigo TEXT,
                sequencia TEXT,
                codigo_barras TEXT
            )
        ''')

        self.__cursor.execute('''
            CREATE TABLE IF NOT EXISTS frota (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                codigo_cliente TEXT,
                placa TEXT,
                marca TEXT,
                ultimo_km TEXT,
                ativo TEXT
            )
        ''')

        self.__cursor.execute('''
            CREATE TABLE IF NOT EXISTS bombas (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                codigo TEXT,
                codigo_tanque TEXT,
                codigo_produto TEXT,
                hexa TEXT,
                casa_milhao TEXT
            )
        ''')

        self.__cursor.execute('''
            CREATE TABLE IF NOT EXISTS grupos (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                codigo TEXT,
                descricao TEXT
            )
        ''')

        self.__cursor.execute('''
            CREATE TABLE IF NOT EXISTS tributos (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                codigo TEXT,
                descricao TEXT,
                cst TEXT,
                aliquota REAL,
                cfop TEXT
            )
        ''')

        self.__cursor.execute('''
            CREATE TABLE IF NOT EXISTS fornecedores (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                codigo TEXT,
                tipo TEXT,
                nome TEXT,
                nome_fantasia TEXT,
                endereco TEXT,
                bairro TEXT,
                cidade TEXT,
                cep TEXT,
                cnpj TEXT,
                cpf TEXT,
                inscr_estadual TEXT,
                fone TEXT,
                email TEXT,
                uf TEXT,
                numero TEXT,
                complemento TEXT
            )
        ''')

        self.__cursor.execute('''
            CREATE TABLE IF NOT EXISTS funcionarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                codigo TEXT,
                nome TEXT,
                ativo TEXT
            )
        ''')

        self.__cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                codigo TEXT,
                tipo TEXT,
                ativo TEXT,
                nome TEXT,
                nome_fantasia TEXT,
                endereco TEXT,
                bairro TEXT,
                uf TEXT,
                cep TEXT,
                cnpj TEXT,
                inscr_estadual TEXT,
                cpf TEXT,
                identidade TEXT,
                fone TEXT,
                email TEXT,
                numero TEXT,
                complemento TEXT,
                cidade TEXT
            )
        ''')

        self.__cursor.execute('''
            CREATE TABLE IF NOT EXISTS tanques (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                codigo TEXT,
                capacidade REAL,
                ativo TEXT
            )
        ''')

        self.__cursor.execute('''
            CREATE TABLE IF NOT EXISTS cidade (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                codigo TEXT,
                cidade TEXT,
                codigo_ibge TEXT   
            )
        ''')

    def cleanRows(self, row):
        return [item.rstrip() if isinstance(item, str) else item for item in row]
    
    # def insert(self, key):
    #     tam = len(self.fields[key])
    #     elementos = self.fields[key]
    #     query = 'INSERT INTO ' + key + \
    #         ' (' + ', '.join(elementos) + ')' + \
    #         ' VALUES (' + ', '.join(['?'] * tam) + ')'
    #     return query
    
    def __insertWithPK(self, key):
        query = 'INSERT INTO ' + key + \
            ' VALUES (?, ' + ', '.join(['?'] * len(self.__fields[key])) + ')'
        return query
    
    def insertProdutos(self, row):
        cleaned_row = self.cleanRows(row)
        self.__cursor.execute(
            self.__insertWithPK('produtos'), 
            (
                None,
                cleaned_row[0], 
                cleaned_row[1], 
                row[2], 
                float(row[3]), 
                float(row[4]), 
                cleaned_row[5], 
                cleaned_row[6], 
                cleaned_row[7], 
                cleaned_row[8], 
                cleaned_row[9], 
                cleaned_row[10], 
                float(row[11]), 
                cleaned_row[12]
            )
        )
    
    def insertProdutosBarras(self, row):
        cleaned_row = self.cleanRows(row)
        self.__cursor.execute(
            self.__insertWithPK('produtos_barras'), 
            (
                None, 
                cleaned_row[0], 
                cleaned_row[1], 
                cleaned_row[2]
            )
        )

    def insertBombas(self, row):
        self.__cursor.execute(self.__insertWithPK('bombas'), (None, row[0], row[1], row[2], row[3], row[4]))

    def insertFrota(self, row):
        cleaned_row = self.cleanRows(row)
        self.__cursor.execute(
            self.__insertWithPK('frota'), 
            (
                None, 
                cleaned_row[0], 
                cleaned_row[1], 
                cleaned_row[2], 
                cleaned_row[3], 
                cleaned_row[4]
            )
        )
    
    def insertGrupos(self, row):
        cleaned_row = self.cleanRows(row)
        self.__cursor.execute(
            self.__insertWithPK('grupos'), 
            (
                None, 
                cleaned_row[0], 
                cleaned_row[1]
            )
        )

    def insertTributos(self, row):
        self.__cursor.execute(self.__insertWithPK('tributos'), (None, row[0], row[1], row[2], float(row[3]), row[4]))

    def insertFornecedores(self, row):
        cleaned_row = self.cleanRows(row)
        self.__cursor.execute(
            self.__insertWithPK('fornecedores'), 
            (
                None, 
                cleaned_row[0], 
                cleaned_row[1], 
                cleaned_row[2], 
                cleaned_row[3], 
                cleaned_row[4], 
                cleaned_row[5], 
                cleaned_row[6], 
                cleaned_row[7], 
                cleaned_row[8], 
                cleaned_row[9], 
                cleaned_row[10], 
                cleaned_row[11], 
                cleaned_row[12], 
                cleaned_row[13], 
                cleaned_row[14], 
                cleaned_row[15]
            )
        )

    def insertFuncionarios(self, row):
        cleaned_row = self.cleanRows(row)
        self.__cursor.execute(
            self.__insertWithPK('funcionarios'), 
            (
                None, 
                cleaned_row[0], 
                cleaned_row[1], 
                cleaned_row[2]
            )
        )

    def insertClientes(self, row):
        cleaned_row = self.cleanRows(row)
        self.__cursor.execute(
            self.__insertWithPK('clientes'), 
            (
                None, 
                cleaned_row[0],
                cleaned_row[1], 
                cleaned_row[2], 
                cleaned_row[3],
                cleaned_row[4], 
                cleaned_row[5], 
                cleaned_row[6], 
                cleaned_row[7], 
                cleaned_row[8], 
                cleaned_row[9], 
                cleaned_row[10], 
                cleaned_row[11],
                cleaned_row[12], 
                cleaned_row[13], 
                cleaned_row[14], 
                cleaned_row[15],
                cleaned_row[16],
                cleaned_row[17]
            )
        )

    def insertTanques(self, row):
        self.__cursor.execute(self.__insertWithPK('tanques'), (None, row[0], float(row[1]), row[2]))

    def insertCidade(self, row):
        self.__cursor.execute(self.__insertWithPK('cidade'), (None, row[0], row[1].rstrip(), row[2]))

    # def insertProdutosCompletos(self, cursor, row):
    #     codigo = row[0]
    #     codigo_aliquota = row[1]
    #     descricao = row[2]
    #     chave_grupo = row[3]
    #     codigo_ncm = row[4]
    #     codigo_cest = row[5]
    #     codigo_unidade = row[6]
    #     embalagem = 0 if row[7] is None else float(row[7])
    #     custo = 0 if row[8] is None else float(row[8])
    #     preco_de_venda = 0 if row[9] is None else float(row[9])
    #     quantidade = 0 if row[10] is None else float(row[10])
    #     cst = row[11]

    #     cursor.execute('''
    #         INSERT INTO produtos_completos (codigo, codigo_aliquota, descricao, chave_grupo, codigo_ncm, codigo_cest, codigo_unidade, embalagem, custo, preco_de_venda, quantidade, cst) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    #     ''', (codigo, codigo_aliquota, descricao, chave_grupo, codigo_ncm, codigo_cest, codigo_unidade, embalagem, custo, preco_de_venda, quantidade, cst))
