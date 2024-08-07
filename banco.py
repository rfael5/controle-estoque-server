import sqlite3

caminho_bd = './estoque.db'

def create_sqlite_database(filename):
    #Cria conexão com banco de dados SQLite
    conn = None
    try:
        conn = sqlite3.connect(filename)
        criar_tabela()
        add_produto()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def criar_tabela():
    query = [
        """
            CREATE TABLE IF NOT EXISTS ctrl_estoque (
                id INTEGER PRIMARY KEY,
                descricao text NOT NULL,
                saldo int NOT NULL,
                unidade text NOT NULL,
                dataMov text NOT NULL,
                tipoMov text NOT NULL,
                solicitante text NOT NULL,
                motivo text NOT NULL
            );
        """
    ]
    
    try:
        with sqlite3.connect(caminho_bd) as conn:
            cursor = conn.cursor()
            for statement in query:
                cursor.execute(statement)
            conn.commit()
        print("Tabela 'ctrl_estoque' criada.")
    except sqlite3.Error as e:
        print(e)


def adicionarEstoque(att):
    query = '''
        INSERT INTO ctrl_estoque (descricao, saldo, unidade, dataMov, tipoMov,solicitante, motivo) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
    '''
    
    try:
        with sqlite3.connect(caminho_bd) as conn:
            cursor = conn.cursor()
            cursor.execute(query, (att['descricao'], att['saldo'], att['unidade'], att['dataMov'],
                                   att['tipoMov'], att['solicitante'], att['motivo']))
            conn.commit()
            print("Acerto adicionado com sucesso.")
    except sqlite3.Error as e:
        print(e)


def add_produto():
    sql = '''INSERT INTO ctrl_estoque (descricao, saldo, unidade, dataMov, tipoMov,solicitante, motivo) 
        VALUES (?, ?, ?, ?, ?, ?, ?)'''
    
    try:
        with sqlite3.connect(caminho_bd) as conn:
            #produto = ('Coxinha de Frango com Catupiry', 3500, '2024-06-10')
            lst_produtos = [
                ('Coxinha de Frango com Catupiry', 3000, 'UN', '25/06/2024', 'soma', '', ''),
                ('Empada de Frango', 3000, 'UN', '25/06/2024', 'soma', '', ''),
                ('Brigadeiro', 3000, 'UN', '25/06/2024', 'soma', '', '')
            ]
            cursor = conn.cursor()
            for p in lst_produtos:
                cursor.execute(sql, p)
                conn.commit()
        print('Produto criado')
    except sqlite3.Error as e:
        print(e)  


def getEstoqueCompleto():
    try:
        with sqlite3.connect(caminho_bd) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM ctrl_estoque')
            rows = cursor.fetchall()
            produtos = [dict(row) for row in rows]
            print(produtos)
            return produtos
    except sqlite3.Error as e:
        print(e)


def buscarProdutoId(produto_id):
    try:
        with sqlite3.connect(caminho_bd) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM ctrl_estoque WHERE pkProduto = {produto_id}')
            row = cursor.fetchone()
            produto = dict(row)
            return produto
    except sqlite3.Error as e:
        print(e)


def buscarProdutosPorData(dt_inicio, dt_fim):
    try:
        with sqlite3.connect(caminho_bd) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM ctrl_estoque WHERE tipoMov="subtracao" AND dataMov BETWEEN {dt_inicio} AND {dt_fim}')
            rows = cursor.fetchall()
            produtos = [dict(row) for row in rows]
            return produtos
    except sqlite3.Error as e:
        print(e)


def buscarSAPorData(dt_inicio, dt_fim):
    try:
        with sqlite3.connect(caminho_bd) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM ctrl_semi_acabados WHERE tipoMov="subtracao" AND dataMov BETWEEN {dt_inicio} AND {dt_fim}')
            rows = cursor.fetchall()
            produtos = [dict(row) for row in rows]
            return produtos
    except sqlite3.Error as e:
        print(e)


def atualizarSaldoEstoque(produto_id, qtd):
    try:
        with sqlite3.connect(caminho_bd) as conn:
            cursor = conn.cursor()
            query = f'''
                UPDATE ctrl_estoque SET saldo={qtd} WHERE pkProduto = {produto_id} 
            '''
            cursor.execute(query)
            conn.commit()
    except sqlite3.Error as e:
        print(e)

def excluirLinha(id_linha):
    try:
        with sqlite3.connect(caminho_bd) as conn:
            cursor = conn.cursor()
            query = f'''
                DELETE FROM ctrl_estoque WHERE id = {id_linha}
            '''
            cursor.execute(query)
            conn.commit()
    except sqlite3.Error as e:
        print(e)


def excluirTabela(nome_tabela):
    try:
        with sqlite3.connect(caminho_bd) as conn:
            cursor = conn.cursor()
            query = f'''
                DROP TABLE IF EXISTS {nome_tabela}
            '''
            cursor.execute(query)
            conn.commit()
    except sqlite3.Error as e:
        print(e)


def criarTabelaProdutos():
    query = [
        """
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY,
                nomeProduto text NOT NULL,
                saldoTotal int NOT NULL,
                unidade text NOT NULL
            );
        """
    ]
    
    try:
        with sqlite3.connect(caminho_bd) as conn:
            cursor = conn.cursor()
            for statement in query:
                cursor.execute(statement)
            conn.commit()
        print("Tabela 'produtos' criada.")
    except sqlite3.Error as e:
        print(e)


def cadastrarProduto():
    sql = '''INSERT INTO produtos (nomeProduto, saldoTotal, unidade) 
        VALUES (?, ?, ?)'''
    
    try:
        with sqlite3.connect(caminho_bd) as conn:
            #produto = ('Coxinha de Frango com Catupiry', 3500, '2024-06-10')
            lst_produtos = [
                ('Coxinha de Frango com Catupiry', 3000, 'UN'),
                ('Empada de Frango', 3000, 'UN'),
                ('Brigadeiro', 3000, 'UN')
            ]
            cursor = conn.cursor()
            for p in lst_produtos:
                cursor.execute(sql, p)
                conn.commit()
        print('Produtos criados')
    except sqlite3.Error as e:
        print(e)


def verEstoque():
    query = """SELECT * FROM produtos"""

    try:
        with sqlite3.connect(caminho_bd) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            rows = cursor.execute(query)
            produtos = [dict(row) for row in rows]
            return produtos
    except sqlite3.Error as e:
        print(e)



def getProdutoUnico(id_produto):
    query = f"""
        SELECT * FROM produtos WHERE id = {id_produto}
    """

    try:
        with sqlite3.connect(caminho_bd) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            produto = cursor.fetchone()
            return produto
    except sqlite3.Error as e:
        print(e)


def atualizarSaldo(req):
    print(req)
    produto = getProdutoUnico(req['id'])
    valor_atualizado = produto[2] + req['movimentacao']

    query = f"""
        UPDATE produtos SET saldoTotal = {valor_atualizado} WHERE id = {req['id']}
    """
    try:
        with sqlite3.connect(caminho_bd) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
    except sqlite3.Error as e:
        print(e)
    
    teste = getProdutoUnico(req['id'])
    print(f"=D  {teste}")



