import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Impactos Financeiros",
    page_icon= "💸",
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

st.title("💸 Impacto Financeiro")

#Perda média por tipo de ataque
st.markdown('<div class="box-ajustada"><b>Perda financeira média por tipo de ataque</b></div>', unsafe_allow_html=True)

df_ataque = df.groupby("Attack Type")["Financial Loss (in Million $)"].mean().reset_index()
fig1 = px.bar(df_ataque, x="Financial Loss (in Million $)", y="Attack Type", orientation='h',
              color="Financial Loss (in Million $)", color_continuous_scale="Blues",
              labels={"Financial Loss (in Million $)": "Perda Média (em Milhões $)", "Attack Type": "Tipo de Ataque"})
st.plotly_chart(fig1, use_container_width=True)

st.markdown("""
<div class="interpretacao">
<b>Interpretação:</b><br>
É possível observar que certos tipos de ataques geram perdas financeiras médias significativamente superiores aos demais. Ataques como DDoS e Man-in-the-Middle se destacam, com este último indicando que apesar de ser o menos frequente, causa um impacto econômico expressivo. 
Isso sugere que os investimentos em prevenção não devem focar apenas em volume, mas também no potencial de dano por incidente.
</div>
""", unsafe_allow_html=True)

#Perda financeira total por país
st.markdown('<div class="box-ajustada"><b>Perda financeira total por país</b></div>', unsafe_allow_html=True)

df_pais = df.groupby("Country")["Financial Loss (in Million $)"].sum().reset_index()
fig2 = px.bar(df_pais, x="Country", y="Financial Loss (in Million $)",
              color="Financial Loss (in Million $)", color_continuous_scale="OrRd",
              labels={"Country": "País", "Financial Loss (in Million $)": "Perda Total (M $)"})
st.plotly_chart(fig2, use_container_width=True)

st.markdown("""
<div class="interpretacao">
<b>Interpretação:</b><br>
O gráfico demonstra que países com maior perda financeira total são Brasil, Alemanha e Reino Unido. Esse padrão sugere que essas nações possuem infraestrutura digital significativa, alto volume de dados corporativos e talvez vulnerabilidades exploradas com maior frequência. 
A posição de destaque do Brasil também pode indicar desafios específicos na proteção cibernética regional, evidenciando a necessidade de políticas mais robustas de segurança digital.

</div>
""", unsafe_allow_html=True)

#Tendência de perdas ao longo dos anos
st.markdown('<div class="box-ajustada"><b>Tendência de perdas ao longo dos anos</b></div>', unsafe_allow_html=True)

df_ano = df.groupby("Year")["Financial Loss (in Million $)"].sum().reset_index()
fig3 = px.line(df_ano, x="Year", y="Financial Loss (in Million $)",
               markers=True, line_shape="spline",
               labels={"Year": "Ano", "Financial Loss (in Million $)": "Perda Total"})
st.plotly_chart(fig3, use_container_width=True)

st.markdown("""
<div class="interpretacao">
<b>Interpretação:</b><br>
Nota-se uma tendência crescente nas perdas financeiras ao longo dos anos, com destaque para um crescimento acentuado seguido de estabilização a partir de 2020. 
Esse padrão coincide com o cenário pandêmico global, quando empresas e serviços migraram rapidamente para o digital. 
A ausência de maturidade em segurança cibernética nesse período pode ter amplificado os impactos econômicos.
</div>
""", unsafe_allow_html=True)

#Perda por setor/indústria
st.markdown('<div class="box-ajustada"><b>Perda financeira por setor/indústria</b></div>', unsafe_allow_html=True)

df_industria = df.groupby("Target Industry")["Financial Loss (in Million $)"].sum().reset_index()
fig4 = px.bar(df_industria, x="Financial Loss (in Million $)", y="Target Industry", orientation='h',
              color="Financial Loss (in Million $)", color_continuous_scale="Viridis",
              labels={"Target Industry": "Setor", "Financial Loss (in Million $)": "Perda Total"})
st.plotly_chart(fig4, use_container_width=True)

st.markdown("""
<div class="interpretacao">
<b>Interpretação:</b><br>
O gráfico acentua que setores como tecnologia, bancário e governamental são os mais afetados financeiramente, o que é coerente com o valor dos dados que manipulam. 
Essas referidas indústrias em conjunto á governos de países operam com alta sensibilidade, e um ataque pode paralisar serviços essenciais ou comprometer grandes volumes de informações sigilosas, justificando os prejuízos elevados.


</div>
""", unsafe_allow_html=True)

#Comparação entre fontes de ataque 
st.markdown('<div class="box-ajustada"><b>Perda financeira por fonte de ataque</b></div>', unsafe_allow_html=True)

df_fonte = df.groupby("Attack Source")["Financial Loss (in Million $)"].mean().reset_index()
fig5 = px.pie(df_fonte, names="Attack Source", values="Financial Loss (in Million $)",
              color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig5, use_container_width=True)

st.markdown("""
<div class="interpretacao">
<b>Interpretação:</b><br>
Ataques de fontes externas (como grupos hackers e nações-estados) concentram a maior média de perdas financeiras. 
Isso revela o alto padrão e planejamento por trás desses ataques, motivados por espionagem industrial, chantagem ou sabotagem, ao contrário de fontes internas ou acidentais, cujo normalmente causam menor prejuizo.
""", unsafe_allow_html=True)

