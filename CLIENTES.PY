import sqlite3

def criar_tabela():
    # Conectar-se ao banco de dados (criará um novo se não existir)
    conn = sqlite3.connect('clientes.db')
    
    # Criar o cursor
    cursor = conn.cursor()
    
    # Criar tabela de clientes se ainda não existir
    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT NOT NULL,
                       contato TEXT NOT NULL)''')
    
    # Commit e fechar conexão
    conn.commit()
    conn.close()

def cadastrar_cliente(nome, contato):
    # Conectar-se ao banco de dados
    conn = sqlite3.connect('clientes.db')
    
    # Criar o cursor
    cursor = conn.cursor()
    
    # Inserir dados na tabela de clientes
    cursor.execute('''INSERT INTO clientes (nome, contato) VALUES (?, ?)''', (nome, contato))
    
    # Commit e fechar conexão
    conn.commit()
    conn.close()

def main():
    # Criar a tabela de clientes
    criar_tabela()
    
    # Pedir ao usuário para inserir nome e contato do cliente
    nome = input("Digite o nome do cliente: ")
    contato = input("Digite o contato do cliente: ")
    
    # Cadastrar o cliente no banco de dados
    cadastrar_cliente(nome, contato)
    
    print("Cliente cadastrado com sucesso!")

if __name__ == "__main__":
    main()
