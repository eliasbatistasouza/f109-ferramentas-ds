import streamlit as st

from utils import data_loading


def main():
    st.set_page_config(page_title="Home", layout="wide")

    st.title("Ferramentas de Data Science - F109")
    st.markdown(
        """
            Este é um projeto de demonstração para a disciplina de Ferramentas de Data Science (F109).
            O objetivo é mostrar como carregar, processar e visualizar dados usando Python e Streamlit.
            """
    )

    # Load and display data
    df = data_loading.merge_ecommerce_data()
    st.subheader("Dados Processados")
    st.dataframe(df)


if __name__ == "__main__":
    main()
