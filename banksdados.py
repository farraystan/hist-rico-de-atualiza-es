import pandas as pd

# Suponha que você tenha um DataFrame chamado df

# Criando um DataFrame de exemplo
dados = {
    'Coluna1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Coluna2': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
}
df = pd.DataFrame(dados)

# Visualizar a coluna 1 e as linhas 3-8
consulta = df.iloc[2:8, 0]  # Selecionando as linhas 3 a 8 (indice 2 a 7) da coluna 1 (indice 0)
print(consulta)
