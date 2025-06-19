import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Tendências Temporais",
    page_icon= "📈",
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

st.title("📈 Tendências Temporais")

#Quais ataques estão crescendo com o tempo
st.markdown('<div class="box-ajustada"><b>Evolução do número de ataques por tipo ao longo dos anos</b></div>', unsafe_allow_html=True)

df_ataques_por_ano = df.groupby(["Year", "Attack Type"]).size().reset_index(name="Incidentes")
fig1 = px.line(df_ataques_por_ano, x="Year", y="Incidentes", color="Attack Type", markers=True,
               labels={"Year": "Ano", "Incidentes": "Número de Incidentes", "Attack Type": "Tipo de Ataque"})
st.plotly_chart(fig1, use_container_width=True)

st.markdown("""
<div class="interpretacao">
<b>Interpretação:</b><br>
O gráfico demonstra um crescimento constante das perdas financeiras causadas por ameaças cibernéticas entre 2015 e 2024. Ataques do tipo Pishing possui uma margem de crescimento acentuada nos últimos dois anos em comparação aos demais.
Em contrapartida ataques com SQL injection, se revela em queda nos últimos anos, talvez evidenciando maior infraestrutura contra ataques deste tipo.
</div>
""", unsafe_allow_html=True)

#Crescimento das perdas financeiras ao longo dos anos
st.markdown('<div class="box-ajustada"><b>Crescimento das perdas financeiras ao longo dos anos</b></div>', unsafe_allow_html=True)

df_perdas_ano = df.groupby("Year")["Financial Loss (in Million $)"].sum().reset_index()
fig2 = px.area(df_perdas_ano, x="Year", y="Financial Loss (in Million $)",
               labels={"Financial Loss (in Million $)": "Perda Total (M $)", "Year": "Ano"},
               color_discrete_sequence=["#EF476F"])
st.plotly_chart(fig2, use_container_width=True)

st.markdown("""
<div class="interpretacao">
<b>Interpretação:</b><br>
Com o gráfico é possível observar um salto expressivo seguido de estabilização a partir de 2020, possivelmente impulsionado pelo aumento da digitalização e do trabalho remoto durante a pandemia.  
Esse aumento pode refletir tanto a sofisticação dos ataques quanto a maior dependência de ativos digitais pelas organizações.
</div>
""", unsafe_allow_html=True)



#Mudança nos alvos prioritários (setores)
st.markdown('<div class="box-ajustada"><b>Mudança nos setores mais atacados ao longo do tempo</b></div>', unsafe_allow_html=True)

df_setor_ano = df.groupby(["Year", "Target Industry"]).size().reset_index(name="Incidentes")
fig3 = px.line(df_setor_ano, x="Year", y="Incidentes", color="Target Industry", markers=True,
               labels={"Year": "Ano", "Incidentes": "Número de Incidentes", "Target Industry": "Setor Alvo"})
st.plotly_chart(fig3, use_container_width=True)

st.markdown("""
<div class="interpretacao">
<b>Interpretação:</b><br>
Há uma transição clara nos setores mais atacados ao longo dos anos. O setor bancário mostrou-se em queda em quantidade de ataques.
Enquanto o setor governamental evidencia um constante aumento de ataques sofridos. Reforçando assim a importância de atualizações contínuas nos mecanismos de defesa cybernetica dos países.
</div>
""", unsafe_allow_html=True)