import sqlite3

class Backend:
    def __init__(self):
        self.conexao = sqlite3.connect("estoque.db")
        self.cursor = self.conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                nome TEXT PRIMARY KEY,
                quantidade INTEGER,
                preco REAL
            )
        """)
        self.conexao.commit()

    def listar_produtos(self):
        self.cursor.execute("SELECT * FROM produtos")
        return self.cursor.fetchall()

    def adicionar_produto(self, nome, quantidade, preco):
        self.cursor.execute("""
            INSERT OR REPLACE INTO produtos (nome, quantidade, preco)
            VALUES (?, ?, ?)
        """, (nome, quantidade, preco))
        self.conexao.commit()

    def remover_produto(self, nome):
        self.cursor.execute("DELETE FROM produtos WHERE nome = ?", (nome,))
        self.conexao.commit()

    def buscar_produto(self, nome):
        self.cursor.execute("SELECT quantidade, preco FROM produtos WHERE nome = ?", (nome,))
        return self.cursor.fetchone()

    def atualizar_quantidade(self, nome, nova_qtd):
        self.cursor.execute("UPDATE produtos SET quantidade = ? WHERE nome = ?", (nova_qtd, nome))
        self.conexao.commit()

    def fechar(self):
        self.conexao.close()
