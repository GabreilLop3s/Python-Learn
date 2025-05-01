import streamlit as st
import dados


st.title("Filmes")

nome = st.text_input("Nome do fime:")

ano = st.number_input("Ano do filme:",min_value=2005, max_value=2025)

nota = st.number_input("Nota do filme:", min_value=0.0, max_value=10.0)

if st.button("Adciionar"):
    dados.inserir_dados(nome, ano, nota)
    st.success("Filme cadastrado")
