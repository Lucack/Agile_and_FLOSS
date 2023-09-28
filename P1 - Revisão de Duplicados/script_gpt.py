import pandas as pd

# Nome do arquivo CSV
arquivo = 'P1 - Revisão de Duplicados\Duplicados.csv'

# Ler o arquivo CSV
df = pd.read_csv(arquivo)

# Assumindo que a coluna que você quer verificar é nomeada 'coluna_nome'
# Se não for esse o nome, substitua 'coluna_nome' pelo nome correto

df['Scopus'] = df['Scopus'].str.upper()


# Contar as repetições
contagem = df['Scopus'].value_counts()

# Exibir valores repetidos e suas contagens
print(contagem[contagem > 1])

# Remover duplicatas mantendo a primeira ocorrência
df_unico = df.drop_duplicates(subset='Scopus', keep='first')

# Salvar o CSV sem duplicatas
df_unico.to_csv('sem_duplicatas.csv', index=False)

print("Arquivo 'sem_duplicatas.csv' salvo com sucesso!")
