import streamlit as st
import dados


st.title("Filmes")


nome = st.text_input("Nome do fime:")

ano = st.number_input("Ano do filme:",min_value=2005, max_value=2025)

nota = st.number_input("Nota do filme:", min_value=0.0, max_value=10.0)

if st.button("Adicionar"):
    dados.inserir_dados(nome, ano, nota)
    st.success("Filme cadastrado")

id_exclusao = st.number_input("ID do filme a excluir:", min_value=1, step=1)

if st.button("Excluir"):
    dados.excluir_dados(id_exclusao)
    st.success("Filme excluído")
    
    
st.subheader("Filmes cadastrados")

filmes = dados.obter_dados()

if filmes:
    for filme in filmes:
        st.write(f"ID: {filme[0]} | Nome: {filme[1]} | Ano: {filme[2]} | Nota: {filme[3]}")
else:
    st.info("Nenhum filme cadastrado ainda.")

