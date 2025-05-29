import pandas as pd
import plotly.express as px
import streamlit as st

st.title('Dashboard Interativo - Contagem por Categoria')

uploaded_file = st.file_uploader('Faça upload do arquivo churn_telecon.csv', type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    colunas_categoricas = df.select_dtypes(include='object').columns.tolist()
    if 'customerID' in colunas_categoricas:
        colunas_categoricas.remove('customerID')
    
    coluna_escolhida = st.selectbox('Escolha a coluna para visualizar:', colunas_categoricas)
    
    contagem = df.groupby(coluna_escolhida)['customerID'].count().reset_index()
    contagem.rename(columns={'customerID': 'Quantidade de Clientes'}, inplace=True)
    
    fig = px.bar(contagem,
                 x=coluna_escolhida,
                 y='Quantidade de Clientes',
                 text='Quantidade de Clientes',
                 title=f'Quantidade de Clientes por {coluna_escolhida}')
    fig.update_traces(textposition='outside')
    fig.update_layout(xaxis_tickangle=-45)
    
    st.plotly_chart(fig, use_container_width=True)



Criação do app.py com o código do BI
