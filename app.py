import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Painel IQVU - Belo Horizonte", layout="wide")

df = pd.read_csv("bd_iqvu_1994_2016.csv", sep=";", encoding="latin-1",
decimal=",")
df.columns = df.columns.str.replace("\ufeff", "", regex=False).str.strip()



df_filtrado = df[
    (df["NOMEUP"].isin(["Taquaril", "Santa Ines"])) &
    (df["ï»¿SERIE"].isin(["SERIE HISTORICA"]))
].copy()

df_tabela = df_filtrado[["NOMEUP", "ANO", "IQVU"]]
st.dataframe(df_tabela)
st.title("Painel Streamlit do IQVU de Belo Horizonte — Taquaril e Santa Inês")

st.sidebar.header("Controles")
opcao = st.sidebar.radio("Selecione a visualização:", ["Tabela", "Gráficos"])
if opcao == "Tabela":
    st.header("Tabela do IQVU (Série Histórica)")
    st.dataframe(df_tabela, use_container_width=True, hide_index=True)

elif opcao == "Gráficos":
    st.header("Gráficos do IQVU — Taquaril e Santa Inês")

#-----------------------------------------------------------------------------

df_taquaril = df_tabela[df_tabela["NOMEUP"] == "Taquaril"] 
 
fig_linha_taquaril = px.line( 
    df_taquaril, 
    x="ANO", 
    y="IQVU", 
    markers=True, 
    title="Evolução do IQVU — Taquaril (1994 a 2016)", 
    template="plotly_dark" 
) 
fig_linha_taquaril.update_traces(line_color="#FF6B6B", line_width=3, marker_size=8) 
fig_linha_taquaril.update_xaxes(type="category") 
st.plotly_chart(fig_linha_taquaril, use_container_width=True)

#-----------------------------------------------------------------------------

df_santa_ines = df_tabela[df_tabela["NOMEUP"] == "Santa Ines"] 
 
fig_linha_santa_ines = px.line( 
    df_santa_ines, 
    x="ANO", 
    y="IQVU", 
    markers=True, 
    title="Evolução do IQVU — Santa Inês (1994 a 2016)", 
    template="plotly_dark" 
) 
fig_linha_santa_ines.update_traces(line_color="#00F5D4", line_width=3, marker_size=8) 
fig_linha_santa_ines.update_xaxes(type="category") 
st.plotly_chart(fig_linha_santa_ines, use_container_width=True)

#-----------------------------------------------------------------------------


st.markdown("---")
st.caption("Fonte dos dados: dados abertos da Prefeitura de Belo Horizonte — https://dados.pbh.gov.br/")
