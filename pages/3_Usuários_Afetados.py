import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Usúarios Afetados",
    page_icon= "👥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

with open("styles/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""
    <style>
        /* Muda a cor de fundo da sidebar */
        [data-testid="stSidebar"] {
            background-color: #c3d5db;
        }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    return pd.read_csv("data/Global_Cybersecurity_Threats_2015-2024.csv")

df = load_data()

st.title("👥 Usúarios Afetados")

#Número médio de usuários afetados por tipo de ataque
st.markdown('<div class="box-ajustada"><b>Número médio de usuários afetados por tipo de ataque</b></div>', unsafe_allow_html=True)

df_pais = df.groupby("Attack Type")["Number of Affected Users"].sum().reset_index()
fig2 = px.bar(df_pais, x="Attack Type", y="Number of Affected Users",
              color="Number of Affected Users", color_continuous_scale="OrRd",
              labels={"Attack Type": "Tipo de Ataque", "Number of Affected Users": "Número de Usúarios Afetados"})
st.plotly_chart(fig2, use_container_width=True)

st.markdown("""
<div class="interpretacao">
<b>Interpretação:</b><br>
O gráfico destaca que ataques como DDoS e SQL Injection se destacam por impactarem um grande número de usuários. O DDoS afeta amplamente o acesso a serviços online, causando indisponibilidade para milhares de usuários simultaneamente. 
Já o SQL Injection compromete bancos de dados inteiros, expondo informações sensíveis em larga escala. Esses tipos de ataque se mostram extremamente eficazes em termos de alcance populacional.
</div>
""", unsafe_allow_html=True)

#Indústrias com maior número total de usuários afetados
st.markdown('<div class="box-ajustada"><b>Indústrias com maior número de usuários afetados</b></div>', unsafe_allow_html=True)

df_usuarios_industria = df.groupby("Target Industry")["Number of Affected Users"].sum().reset_index()
fig2 = px.bar(df_usuarios_industria.sort_values("Number of Affected Users", ascending=False),
              x="Number of Affected Users", y="Target Industry", orientation="h",
              color="Number of Affected Users", color_continuous_scale="Oranges",
              labels={"Target Industry": "Setor", "Number of Affected Users": "Total de Usuários Afetados"})
st.plotly_chart(fig2, use_container_width=True)

st.markdown("""
<div class="interpretacao">
<b>Interpretação:</b><br>
O gráfico escancara que setores com o maior número de usuários afetados incluem saúde, bancário e tecnologia. 
Isso pode estar associado ao fato de que esses setores armazenam grandes volumes de dados pessoais e, muitas vezes, operam com sistemas legados e menos protegidos, tornando-os alvos atrativos para ataques em escala.
</div>
""", unsafe_allow_html=True)

#Correlação entre número de usuários afetados e perda financeira
st.markdown('<div class="box-ajustada"><b>Correlação entre número de usuários afetados e perda financeira</b></div>', unsafe_allow_html=True)

fig3 = px.scatter(df,
                  x="Number of Affected Users",
                  y="Financial Loss (in Million $)",
                  color="Attack Type",
                  hover_data=["Country", "Target Industry"],
                  labels={"Number of Affected Users": "Usuários Afetados", "Financial Loss (in Million $)": "Perda Financeira"},
                  title=None)
st.plotly_chart(fig3, use_container_width=True)

st.markdown("""
<div class="interpretacao">
<b>Interpretação:</b><br>
A dispersão dos dados mostra que, embora exista uma tendência de que ataques com mais usuários afetados possam gerar maiores perdas financeiras, porém essa correlação não é absoluta. 
Isso pois ataques altamente direcionados, mesmo com poucos afetados, podem causar prejuízos severos, especialmente quando envolvem setores estratégicos ou dados confidenciais.
</div>
""", unsafe_allow_html=True)
