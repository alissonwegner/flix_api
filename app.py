import streamlit as st
from genres.page import show_genres

def main():
    st.title('Flix App')
    menu_option = st.sidebar.selectbox(
        'Selecione uma opção',
        ['Inicio', 'Generos', 'Atores', 'Filmes', 'Avaliações']

    )
    if menu_option == 'Inicio':
        st.write('Inicio')

    if menu_option == 'Generos':
        show_genres()

    if menu_option == 'Atores':
        st.write('Lista de Atores')

    if menu_option == 'Filmes':
        st.write('Lista de Filmes')    

    if menu_option == 'Avaliações':
        st.write('Lista de Avaliações')

if __name__ =='__main__':
    main()