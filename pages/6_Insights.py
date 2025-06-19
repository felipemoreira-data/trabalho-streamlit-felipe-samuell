import streamlit as st
import pandas as pd



st.set_page_config(
    page_title="Insights",
    page_icon= "💡",
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

st.title("💡 Insights e Recomendações")

st.markdown("""
<div class="interpretacao">
<b>A Digitalização em Massa e sua Correlação com o Aumento do Número de Ataques:</b><br>
A análise dos dados revela que o impacto financeiro dos ataques cibernéticos tem crescido de forma consistente ao longo da última década, com destaque para um salto expressivo a partir de 2020. Esse comportamento parece estar fortemente relacionado ao cenário pandêmico, acelerando a transformação digital de empresas e instituições públicas. 
A adoção emergencial de soluções remotas e digitais, sem um amadurecimento em cibersegurança, tornou organizações mais vulneráveis. A tendência é clara: à medida que a digitalização avança, o custo dos ataques aumenta proporcionalmente, tanto em termos econômicos quanto sociais.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="interpretacao">
<b>A Vulnerabilidade Dos Países e a Necessidade por Maiores Investimentos em Políticas de Cybersegurança:</b><br>
Dentre os países mais afetados financeiramente, Brasil, Alemanha e Reino Unido lideram o ranking. No caso do Brasil, essa posição alarmante evidencia fragilidades estruturais na proteção de dados e na capacidade de resposta a ataques. 
A presença de países desenvolvidos, como Alemanha e Reino Unido, também reforça que uma maior digitalização exige investimentos proporcionais em segurança da informação. 
Como recomendação, os países mais afetados devem providenciar programas nacionais de cibersegurança, capacitar mão de obra técnica e impor regulamentações mais rígidas sobre proteção de dados.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="interpretacao">
<b>Os Tipos de Ataque e Seus Respectivos Impactos:</b><br>
No recorte por tipo de ataque, observa-se que categorias como DDoS e Man-in-the-Middle são as que mais causam perdas financeiras médias por incidente, exigindo maior sofisticação dos agentes de ameaça e maior preparo técnico das equipes de defesa. 
Já ataques como Phishing e SQL Injection, embora não necessariamente gerem os maiores prejuízos monetários por ocorrência, têm impacto massivo sobre os usuários finais, afetando diretamente a disponibilidade de serviços e comprometendo bancos de dados inteiros. 
Isso evidencia a necessidade de medidas de prevenção que equilibrem proteção técnica e experiência do usuário, especialmente em serviços públicos e essenciais.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="interpretacao">
<b>Os Tipos de Setores e Sua Relação com a Quantidade De Ataques Sofridos:</b><br>
Setores como saúde, tecnologia e finanças lideram tanto em perdas econômicas quanto em número de usuários afetados. O setor de saúde, por exemplo, lida com dados extremamente sensíveis, enquanto o setor financeiro é um dos mais visados por sua importância na atividade dos serviços. 
Isso reforça a importância de políticas setoriais específicas de cibersegurança. Organizações desses setores devem investir em sistemas de monitoramento em tempo real, backups regulares, e treinamento contínuo dos colaboradores visando um rápido tempo de resposta a incidentes.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="interpretacao">
<b>Os Prejuízos Financeiros Decorrentes da Demora no Tempo de Resposta á Ataques:</b><br>
Outro ponto crítico identificado está na relação entre o tempo de resolução dos incidentes e o prejuízo financeiro. 
Ataques que levam mais tempo para serem abatidos tendem a causar maiores danos, enfatizando a importância de uma resposta rápida e processos bem definidos de contenção e recuperação. 
A recomendação estratégica aqui é o investimento em planos de resposta a incidentes, simulações regulares de ataques e inteligência cibernética mais proativa.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="interpretacao">
<b>Recomendações Fundamentadas no Crescimento do Índice de Ataques:</b><br>
Por fim, a análise temporal revela uma evolução nos tipos de ataques mais frequentes e nos setores mais visados. Mostrando assim que criminosos adaptam suas táticas conforme o comportamento digital da sociedade muda. Assim, é fundamental que a defesa cibernética também seja dinâmica e adaptável. 
Organizações devem adotar estratégias de segurança baseadas em risco e em dados preditivos, utilizando ferramentas como aprendizado de máquina para detecção de anomalias, SIEMs(Gerenciamento de Informações e Eventos de Segurança) inteligentes e eficientes segmentações de rede, visando o controle de acesso á sistemas, e deste modo limitando o impacto de Ataques.
</div>
""", unsafe_allow_html=True)