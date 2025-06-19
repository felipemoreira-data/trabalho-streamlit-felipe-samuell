import streamlit as st
import pandas as pd
import plotly.express as px



st.set_page_config(
    page_title="Tempo de Resolução",
    page_icon= "⏱️",
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


st.title("⏱️ Tempo de Resolução")


#Tempo médio por tipo de ataque
st.markdown('<div class="box-ajustada"><b>Tempo médio de resolução por tipo de ataque</b></div>', unsafe_allow_html=True)

df_tempo_ataque = df.groupby("Attack Type")["Incident Resolution Time (in Hours)"].mean().reset_index()
fig1 = px.bar(df_tempo_ataque, x="Incident Resolution Time (in Hours)", y="Attack Type", orientation="h",
              color="Incident Resolution Time (in Hours)", color_continuous_scale="Purples",
              labels={"Incident Resolution Time (in Hours)": "Tempo Médio (h)", "Attack Type": "Tipo de Ataque"})
st.plotly_chart(fig1, use_container_width=True)

st.markdown("""
<div class="interpretacao">
<b>Interpretação:</b><br>
Ataques como Malware,Man-in-the-Middle e SQL injection apresentam tempos de resolução mais altos. 
Isso sugere maior dificuldade em detectar e mitigar esses incidentes, além da necessidade de maior especialização técnica para reverter seus efeitos e restaurar a operação normal da organização.
</div>
""", unsafe_allow_html=True)

#Tempo médio por país
st.markdown('<div class="box-ajustada"><b>Comparação de tempo de resposta por país</b></div>', unsafe_allow_html=True)

df_tempo_pais = df.groupby("Country")["Incident Resolution Time (in Hours)"].mean().reset_index()
fig2 = px.bar(df_tempo_pais, x="Country", y="Incident Resolution Time (in Hours)",
              color="Incident Resolution Time (in Hours)", color_continuous_scale="BuPu",
              labels={"Country": "País", "Incident Resolution Time (in Hours)": "Tempo Médio (h)"})
st.plotly_chart(fig2, use_container_width=True)

st.markdown("""
<div class="interpretacao">
<b>Interpretação:</b><br>
Países com maior tempo médio de resolução, como Brasil e China podem estar enfrentando desafios como falta de investimento em equipes de resposta a incidentes, pouca eficiência em cybersegurança ou processos burocráticos. 
Em contrapartida, países com tempos mais baixos, tais como Estados Unidos e Rússia tendem a ter estruturas mais preparadas e ágeis para lidar com ameaças.
</div>
""", unsafe_allow_html=True)

#Relação entre tempo e perda financeira
st.markdown('<div class="box-ajustada"><b>Relação entre tempo de resolução e impacto financeiro</b></div>', unsafe_allow_html=True)

fig3 = px.scatter(df,
                  x="Incident Resolution Time (in Hours)",
                  y="Financial Loss (in Million $)",
                  color="Attack Type",
                  hover_data=["Country", "Target Industry"],
                  labels={
                      "Incident Resolution Time (in Hours)": "Tempo de Resolução (h)",
                      "Financial Loss (in Million $)": "Perda Financeira (M $)"
                  })
st.plotly_chart(fig3, use_container_width=True)

st.markdown("""
<div class="interpretacao">
<b>Interpretação:</b><br>
O gráfico sugere uma correlação moderada entre o tempo de resolução e a perda financeira: incidentes que levam mais tempo para serem resolvidos tendem a gerar maiores prejuízos. 
Isso reforça a importância de uma resposta rápida a incidentes, pois cada hora de inatividade ou vazamento potencializa os danos econômicos.
</div>
""", unsafe_allow_html=True)