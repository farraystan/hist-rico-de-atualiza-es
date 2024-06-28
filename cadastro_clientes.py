import pandas as pd

# Solicitar informações do cliente
nome = input("Nome do cliente: ")
email = input("E-mail do cliente: ")
telefone = input("Telefone do cliente: ")

# Criar um DataFrame com os dados do cliente
dados_cliente = pd.DataFrame({
    'Nome': [nome],
    'E-mail': [email],
    'Telefone': [telefone]
})

# Carregar a planilha existente ou criar uma nova
try:
    planilha = pd.read_excel('clientes.xlsx')
except FileNotFoundError:
    planilha = pd.DataFrame()

# Concatenar os dados do novo cliente com os dados existentes
planilha = pd.concat([planilha, dados_cliente], ignore_index=True)

# Salvar os dados na planilha Excel
planilha.to_excel('clientes.xlsx', index=False)


