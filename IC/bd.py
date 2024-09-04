import pandas as pd
import sqlite3

# Carregar o arquivo XLSX usando pandas
df1 = pd.read_excel('formulas_diferentes_nomes_iguais.xlsx', engine='openpyxl')
df2 = pd.read_excel('Formulas_duplicadas.xlsx', engine='openpyxl')
df3 = pd.read_excel('Nomes_da_velha_que_nao_existem_na_nova.xlsx', engine='openpyxl')
df4 = pd.read_excel('Nomes_diferentes_formulas_iguais.xlsx', engine='openpyxl')
df5 = pd.read_excel('Nomes_iguais.xlsx', engine='openpyxl')
df6 = pd.read_excel('Subclasses_que_batem.xlsx', engine='openpyxl')
df7 = pd.read_excel('Nomes_novos.xlsx', engine='openpyxl')
df8 = pd.read_excel('Subclasses_que_não_batem.xlsx', engine='openpyxl')
df9 = pd.read_excel('Subclasses_que_não_existem_na_velha.xlsx', engine='openpyxl')
df10 = pd.read_excel('Tudo_igual.xlsx', engine='openpyxl')

# Conectar ao banco de dados SQLite (ou criar se não existir)
conn = sqlite3.connect('bdic.db')

# Armazenar o DataFrame no banco de dados
df1.to_sql('formulas_diferentes_nomes_iguais', conn, if_exists='replace', index=False)
df2.to_sql('Formulas_duplicadas', conn, if_exists='replace', index=False)
df3.to_sql('Nomes_da_velha_que_nao_existem_na_nova', conn, if_exists='replace', index=False)
df4.to_sql('Nomes_diferentes_formulas_iguais', conn, if_exists='replace', index=False)
df5.to_sql('Nomes_iguais', conn, if_exists='replace', index=False)
df6.to_sql('Subclasses_que_batem', conn, if_exists='replace', index=False)
df7.to_sql('Nomes_novos', conn, if_exists='replace', index=False)
df8.to_sql('Subclasses_que_não_batem', conn, if_exists='replace', index=False)
df9.to_sql('Subclasses_que_não_existem_na_velha', conn, if_exists='replace', index=False)
df10.to_sql('Tudo_igual', conn, if_exists='replace', index=False)

# Fechar a conexão
conn.close()