import sqlite3

# Define a classe Backend que gerencia o banco de dados
class Backend:
    def __init__(self):
        # Cria uma conexão com o banco de dados 'estoque.db'
        self.conexao = sqlite3.connect("estoque.db")
        # Cria um cursor para executar comandos SQL
        self.cursor = self.conexao.cursor()
        # Chama o método para criar a tabela, se ainda não existir
        self.criar_tabela()

    # Cria a tabela 'produtos' com os campos nome, quantidade e preço
    def criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                nome TEXT PRIMARY KEY,      -- Nome do produto (chave primária)
                quantidade INTEGER,         -- Quantidade em estoque
                preco REAL                  -- Preço do produto
            )
        """)
        # Salva as alterações no banco de dados
        self.conexao.commit()

    # Retorna todos os produtos cadastrados no banco
    def listar_produtos(self):
        self.cursor.execute("SELECT * FROM produtos")
        return self.cursor.fetchall()

    # Adiciona um novo produto ou atualiza se o nome já existir
    def adicionar_produto(self, nome, quantidade, preco):
        self.cursor.execute("""
            INSERT OR REPLACE INTO produtos (nome, quantidade, preco)
            VALUES (?, ?, ?)
        """, (nome, quantidade, preco))
        self.conexao.commit()

    # Remove um produto do banco com base no nome
    def remover_produto(self, nome):
        self.cursor.execute("DELETE FROM produtos WHERE nome = ?", (nome,))
        self.conexao.commit()

    # Busca um produto pelo nome e retorna sua quantidade e preço
    def buscar_produto(self, nome):
        self.cursor.execute("SELECT quantidade, preco FROM produtos WHERE nome = ?", (nome,))
        return self.cursor.fetchone()

    # Atualiza apenas a quantidade de um produto específico
    def atualizar_quantidade(self, nome, nova_qtd):
        self.cursor.execute("UPDATE produtos SET quantidade = ? WHERE nome = ?", (nova_qtd, nome))
        self.conexao.commit()

    # Fecha a conexão com o banco de dados
    def fechar(self):
        self.conexao.close()
