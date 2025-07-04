
🗃️ Gerenciador de Estoque com Caixa Integrado (Python + Tkinter)
Este projeto é um sistema simples de gerenciamento de estoque com uma interface gráfica feita em Tkinter e suporte a operações de compra via caixa. O projeto utiliza SQLite para persistência dos dados.

📁 Estrutura de Arquivos
📦 Projeto ├── backend.py # Manipulação direta do banco de dados SQLite 
           ├── caixa.py # Lógica de compra (caixa) 
           ├── interface.py # Interface gráfica Tkinter 
           ├── main.py # Arquivo principal para iniciar a aplicação 
           ├── main.spec # Especificações do PyInstaller (opcional)

yaml Copiar Editar

🔧 Funcionalidades
✅ Adicionar Produto
Nome, quantidade e preço são inseridos via GUI.
Os dados são salvos em um banco de dados local (estoque.db).
❌ Remover Produto
Remove produtos pelo nome informado.
📋 Mostrar Estoque
Exibe uma lista dos produtos disponíveis com suas quantidades e preços.
💸 Processar Compra
O usuário informa o nome do produto, quantidade desejada e valor pago.
O sistema:
Verifica se o produto existe;
Verifica se há quantidade suficiente;
Calcula o total e o troco;
Atualiza o estoque automaticamente.
🧠 Lógica Interna
backend.py
Gerencia a conexão com o SQLite:

def adicionar_produto(self, nome, quantidade, preco):
    INSERT OR REPLACE INTO produtos ...
caixa.py
Realiza as verificações e operações de compra:

python
Copiar
Editar
if quantidade_desejada > quantidade_estoque:
    return {"sucesso": False, "mensagem": "⚠️ Quantidade maior do que o disponível"}
interface.py
Contém toda a interface gráfica feita com tkinter, organizada de forma simples:

Campos de entrada para nome, quantidade e preço;

Botões de ações para adicionar, remover, visualizar e comprar;

Janela separada para o caixa.

main.py
Inicia a aplicação:

python
Copiar
Editar
root = tk.Tk()
app = EstoqueGUI(root)
root.mainloop()
🖥️ Tecnologias Utilizadas
Python 3.x

Tkinter (interface gráfica)

SQLite3 (banco de dados embutido)
#tale o Py
n.spec com o PyInstaller para gerar um executável:

bash
Copiar
Editar
pyinstaller main.spec
🏁 Objetivo
Este projeto tem como objetivo principal aprimorar a organização e controle de estoque, tornando mais acessível o registro, visualização e movimentação de produtos com um visual intuitivo.

# 📦 Aplicação .exe

Para transformar o projeto Python em um executável `.exe`, foi utilizado o **[PyInstaller](https://pyinstaller.org/)**. Isso permite que o sistema funcione em qualquer computador com Windows, sem necessidade de instalar o Python.

ps:(O .exe ja esta disponivel dentro da pasta dist)
