import streamlit as st
import pandas as pd
import plotly.express as px

# Passo 1: determinar/colocar as seções do site
    #+ Titulo - Sistema de vendas

tabela = pd.read_csv("vendas.csv")
st.title("Sistema de Vendas e Gestão Online")

    #+ Seção de cadastrar vendas
        #+ Campo data
        #+ Campo vendedor - Ana, Bruno, Carla
        #+ Campo produto - Notebook, Fone, celular
        #+ Campo quantidade
        #+ Campo valor
        #+ Botão de cadastrar

st.sidebar.write("## Cadastrar Vendas")
date = st.sidebar.date_input("Data da Venda")
seller = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
product = st.sidebar.selectbox("Produto", ["Notebook", "Fone", "Celular"])
quantity = st.sidebar.number_input("Quantidade", min_value=1, step=1)
value = st.sidebar.number_input("Valor", min_value=0.0, step=0.01)
button = st.sidebar.button("Cadastrar Venda")

if button:
    if(date and seller and product and quantity and value):
        new_sale = [str(date), seller, product, quantity, value]
        tabela.loc[len(tabela)] = new_sale
        tabela.to_csv("vendas.csv", index=False)
        st.success("Venda cadastrada com sucesso!")
    else:
        st.error("Por favor, preencha todos os campos.")

    #+ Seção vendas cadastradas
        #+ Tabela com as vendas 

st.write("## Vendas Cadastradas")
st.dataframe(tabela)

    #+ Seção dashboard
        #+ Card/Métrica -> faturamento total
        #+ Gráfico de barras -> venda por vendedor
        #+ Gráfico pizza -> venda por produto

st.write("## Dashboard")
st.metric("Faturamento Total", f"R$ {tabela['valor'].sum():.2f}")
grafico = px.bar(tabela, x="vendedor", y="valor", color="produto", title="Vendas por Vendedor")
st.plotly_chart(grafico)

grafico_pizza = px.pie(tabela, names="produto", values="valor", title="Vendas por Produto")
st.plotly_chart(grafico_pizza)