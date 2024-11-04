import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

arquivo_csv = 'housing_sp_city.csv'
df = pd.read_csv(arquivo_csv,  encoding='latin1')
df2 = df.head(30000)

st.set_page_config(
    page_title = "Casas em São Paulo", 
    page_icon = "🏂",
    layout="wide",
    initial_sidebar_state="expanded")

with st.sidebar:
    st.title('Casas em São Paulo')
    #color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    #selected_color_theme = st.selectbox('Select a color theme', color_theme_list)

    lista_imoveis = ['Apartamento', 'Casa de dois andares', 'Casa', 'Flat', 'Escritório', 
                     'Comercial', 'Cobertura', 'Condomínio', 'Depósito', 'Loteamento Residencial', 'Loteamento Comercial',
                      'Loja', 'Kitnet', 'Prédio Residencial', 'Prédio Comercial', 'Clínica', 'Casa de Campo',
                       'Fazenda' ]
    escolha_imoveis_botao = st.selectbox('Escolha seu imóvel para pesquisa:', lista_imoveis)

df_filtrado = df2[df2['tipo_imovel'] == escolha_imoveis_botao]

col = st.columns((3, 4), gap='medium')
# Testes com streamlit
st.write("Dados do CSV:", df_filtrado)

with col[0]:
    fig_line = px.line(
    df2,
    x=df2.index,  # Usando o índice do DataFrame como eixo x
    y='area_util',
    title='Área Útil (m²)',
    labels={'area_util': 'Área Útil', 'index': 'Número de Imóveis'}
)
    st.plotly_chart(fig_line, use_container_width=True)

contagem_tipos = df2['tipo_imovel'].value_counts().reset_index()
contagem_tipos.columns = ['tipo_imovel', 'contagem']

with col[1]:
    fig = px.bar(contagem_tipos,x='tipo_imovel',y='contagem',title='Tipos de Imóvel',color='tipo_imovel', color_discrete_sequence=['#FF0000', '#FF6347', '#FF7F50', '#FFA07A', '#E9967A', '#FA8072', '#FF8C00', '#FFA500', '#FFD700', '#FFFF00', '#F0E68C',  '#BDB76B'])  # Cores personalizadas em hexadecimal
    st.plotly_chart(fig)

col2 = st.columns((4, 1), gap='medium')
with col2[0]:
    fig_line = px.line(
    df_filtrado,
    x=df_filtrado.index,  # Usando o índice do DataFrame como eixo x
    y='area_util',
    title='Área Útil Selecionada (m²)',
    labels={'area_util': 'Área Útil', 'index': 'Número de Imóveis'}
)
    st.plotly_chart(fig_line, use_container_width=True)

contagem_tipos = df_filtrado['tipo_imovel'].value_counts().reset_index()
contagem_tipos.columns = ['tipo_imovel', 'contagem']

with col2[1]:
    fig = px.bar(contagem_tipos,x='tipo_imovel',y='contagem',title='Tipo de Imóvel Selecionado',color='tipo_imovel', color_discrete_sequence=['#FF0000', '#FF6347', '#FF7F50', '#FFA07A', '#E9967A', '#FA8072', '#FF8C00', '#FFA500', '#FFD700', '#FFFF00', '#F0E68C',  '#BDB76B'])  # Cores personalizadas em hexadecimal
    st.plotly_chart(fig)    

# Limpando e tratando os dados do dataset

