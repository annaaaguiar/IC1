import streamlit as st
import sqlite3
import pandas as pd


# Função para conectar ao banco de dados SQLite
def get_connection():
    return sqlite3.connect('IC/bdic.db')

# Função para obter os nomes das tabelas
def get_table_names(conn):
    query = "SELECT name FROM sqlite_master WHERE type='table';"
    return pd.read_sql(query, conn)['name'].tolist()

# Função para carregar os dados de uma tabela específica
def load_table_data(conn, table_name):
    query = f"SELECT * FROM {table_name};"
    return pd.read_sql(query, conn)

# Configuração da página
st.title('Cruzamento de Dados entre Phenol-Explorer (2016) e PhytoHub')
st.sidebar.title('Selecione uma Opção')

# Conectar ao banco de dados
conn = get_connection()

# Definir a ordem das tabelas na barra lateral
table_options = {
    'Todas as informações': 'Tudo_igual',
    'Nomes iguais entre as planilhas': 'Nomes_iguais',
    'Nomes adicionados apenas na planilha PytoHub': 'Nomes_novos',
    'Nomes que continham apenas na planilha Phenol-Explorer': 'Nomes_da_velha_que_nao_existem_na_nova',
    'Fórmulas que permanecem as mesmas entre as planilhas, porém com nomes diferentes': 'Nomes_diferentes_formulas_iguais',
    'Nomes que permanecem os mesmos entre as planilhas, porém com fórmulas diferentes': 'formulas_diferentes_nomes_iguais',
    'Fórmulas duplicadas': 'Formulas_duplicadas',
    'Subclasses citados apenas na planilha do PythoHub': 'Subclasses_que_não_existem_na_velha',
    'Subclasses que são compatíveis entre as planilhas': 'Subclasses_que_batem',
    'Subclasses que não são compatíveis entre as planilhas': 'Subclasses_que_não_batem'
}

# Adicionar a seleção na barra lateral
selected_option = st.sidebar.selectbox('Escolha uma opção', list(table_options.keys()))
selected_table = table_options[selected_option]

# Carregar e exibir dados da tabela selecionada
if selected_table:
    df = load_table_data(conn, selected_table)


        
st.write('Visualize os dados diretamente abaixo:')
st.dataframe(df)

# Fechar a conexão
conn.close()
