import pandas as pd
import plotly.express as px
import streamlit as st

from utils import data_loading, data_processing


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
    df_reviews_positivos = data_loading.read_csvs_from_data(
        data_loading.REVIEWS_POSITIVOS_FILE
    )
    df_reviews_negativos = data_loading.read_csvs_from_data(
        data_loading.REVIEWS_NEGATIVOS_FILE
    )
    df_forecast = data_loading.read_csvs_from_data(data_loading.FORECAST_FILE)

    # clean and process data
    df = data_processing.clean_dataframe(df)
    df = data_processing.convert_to_datetime(
        df, ["order_purchase_timestamp", "order_approved_at"]
    )
    # st.subheader("Dados Processados")
    # st.dataframe(df)

    with st.sidebar:
        st.subheader("Desenvolvido Por:")
        st.markdown(
            """
            Elias Batista Souza - 2415532\n
            Erik Santos Bezerra - 2424108\n
            Erivelton Lima de Sousa - 2524891\n
            Lucas Gondim Sampaio Sales - 2514951\n
            Cristian Henrique Paulsson Pereira - 2316129\n
            """
        )
        st.subheader("Filtros")
        selected_states = st.multiselect(
            "Selecione Estados",
            options=df["customer_state"].unique(),
            default=df["customer_state"].unique(),
        )
        selected_categories = st.multiselect(
            "Selecione Categorias de Produto",
            options=df["product_category_name"].unique(),
            default=df["product_category_name"].unique(),
        )
        df = df[df["customer_state"].isin(selected_states)]
        df = df[df["product_category_name"].isin(selected_categories)]

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            # Plot orders by day
            orders_by_day = df.groupby(
                df["order_purchase_timestamp"].dt.strftime("%d/%m/%Y")
            ).size()
            st.subheader("Número de Pedidos por Dia")
            st.line_chart(orders_by_day, use_container_width=True)

        with col2:
            # Plot sales by customer stat
            sales_by_state = (
                df.groupby("customer_state").size().reset_index(name="sales")
            )
            fig = px.pie(
                sales_by_state,
                values="sales",
                names="customer_state",
            )
            st.subheader("Número de Vendas por Estado")
            st.plotly_chart(fig, use_container_width=True)

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Matriz de Termos Positivas")
            st.dataframe(df_reviews_positivos)
        with col2:
            st.subheader("Matriz de Termos Negativoss")
            st.dataframe(df_reviews_negativos)

    with st.container():
        st.subheader("Previsão")

        df_forecast["date"] = pd.to_datetime(df_forecast["date"])
        df_forecast = df_forecast.sort_values("date").copy()

        # Adjust these labels if needed
        df_hist = df_forecast[
            df_forecast["data_type"]
            .str.lower()
            .isin(["historical", "histórico"])
        ].copy()
        df_fut = df_forecast[
            df_forecast["data_type"].str.lower().isin(["forecast", "previsão"])
        ].copy()

        # Base figure: historical line
        fig = px.line(
            df_hist,
            x="date",
            y="sales_count",
        )
        fig.update_traces(
            name="Histórico", line=dict(color="#1f77b4", width=3)
        )

        # Add forecast line starting at last historical point (to connect seamlessly)
        if not df_hist.empty and not df_fut.empty:
            last_hist = df_hist.iloc[[-1]][["date", "sales_count"]]
            forecast_with_anchor = pd.concat(
                [last_hist, df_fut[["date", "sales_count"]]], ignore_index=True
            )

            fig_forecast = px.line(
                forecast_with_anchor,
                x="date",
                y="sales_count",
            )
            fig_forecast.update_traces(
                name="Previsão",
                line=dict(color="#ff7f0e", width=3),
            )

            # Add the forecast trace to the base figure
            for tr in fig_forecast.data:
                fig.add_trace(tr)

        # fig.update_layout(
        #     showlegend=True,
        #     legend=dict(
        #         title="Série",
        #         orientation="h",
        #         yanchor="bottom",
        #         y=1.02,
        #         xanchor="right",
        #         x=1,
        #     ),
        # )

        fig.update_xaxes(title_text="Data")
        fig.update_yaxes(title_text="Vendas")
        fig.update_layout(legend_title_text="Série")
        st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    main()
