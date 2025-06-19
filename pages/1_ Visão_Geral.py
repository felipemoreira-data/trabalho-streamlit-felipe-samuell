import streamlit as st
import pandas as pd
import plotly.express as px



st.set_page_config(
    page_title="Visão Geral",
    page_icon= "💻",
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
st.title("📊 Visão Geral dos Dados")

@st.cache_data
def load_data():
    return pd.read_csv("data/Global_Cybersecurity_Threats_2015-2024.csv")

df = load_data()

st.subheader("Amostra dos dados")

df['Year'] = pd.to_numeric(df['Year'],errors='coerce')
df = df.dropna(subset = ['Year'])
df['Year'] = df['Year'].astype(int)

attack_p_year = df.groupby('Year').size().sort_index()

#Distribuição temporal dos ataques
with st.container():
    df_plot = attack_p_year.reset_index()
    df_plot.columns = ['Ano', 'Número de Ataques']

    fig = px.bar(df_plot, x='Ano', y='Número de Ataques',
             labels={'Ano': 'Ano', 'Número de Ataques': 'Nº de ataques'},
             title='Distribuição Temporal dos Ataques (2015–2024)',
             template='plotly_white')
    st.plotly_chart(fig, use_container_width=True)

st.markdown("""
<div class="interpretacao">
<b>Interpretação:</b><br>
É evidenciado que entre os anos de 2015 até 2019, houve uma disparidade de ataques nos anos de 2017 e 2018, e a partir de 2020 há uma certa equidade entre o número de ataques por ano.
Este padrão dos últimos 4 anos pode estar relacionado ao fator pândemico, contribuindo ao fenômeno de "migração virtual", e aumentando a depêndencia de insumos e serviços virtuais.               
</div>
""", unsafe_allow_html=True)    



#Países que sofreram a maior quantidade de ataques 
with st.container():
    country_counts = df['Country'].value_counts().reset_index()
    country_counts.columns = ['Países', 'Quantidade de Ataques']
    st.markdown("""
<div class="especific_word">            

<b>Países com Maiores Quantidades de Ataques sofridos<br>
</div>            
""", unsafe_allow_html=True)
    st.dataframe(country_counts)

st.markdown("""
<div class="interpretacao">
<b>Interpretação:</b><br>
O gráfico revela que a Inglaterra, Brasil e Índia lideram o ranking de países vítimas de ataques. A Inglaterra possui grande parte de sua economia digitalizada, logo isso agrega á um elevado número de ataques virtuais.
O brasil apesar de ser um país em desenvolvimento, ainda carece de infraestrutura anti ataques cybernéticos,que quando somado á uma grande demanda por serviços virtuais,acaba por se tornar um grande alvo, com o mesmo se aplicando pra Índia.            
</div>
""", unsafe_allow_html=True)
 



#Tpos de ataques mais recorrentes
with st.container():
    attack_counts = df['Attack Type'].value_counts().nlargest(10)
    fig_attack = px.bar(attack_counts,
                        x=attack_counts.index,
                        y=attack_counts.values,
                        labels={'x': 'Tipo de Ataques', 'y': 'Frequência'},
                        title='Tipos de Ataques Mais Comuns')
    st.plotly_chart(fig_attack,use_container_width=True)

st.markdown("""
<div class="interpretacao">
<b>Interpretação:</b><br>
DDoS (Ataque a Servidores/Redes) e Phishing (Sobrecarga massiva com botnets) lideram como tipos de ataques mais frenéticos, talvez por serem mais visados por criminosos que buscam difamar algum alvo ou aplicar fraudes e golpes financeiros.
Enquanto Man-in-the-Middle é o menos recorrente, isso muito provavelmente por ser de um grau mais pessoal, e por sua dificuldade excessiva de ser aplicado.
</div>
""", unsafe_allow_html=True)   

#Proporção de indústrias mais avisadas
with st.container():
    industry_counts = df['Target Industry'].value_counts().nlargest(10).reset_index()
    industry_counts.columns = ['Indústria', 'Quantidade']

    fig_industry = px.pie(industry_counts, 
                          names='Indústria', 
                          values='Quantidade',
                          title='Proporção de Indústrias Mais Visadas',
                          hole=0.4)
    st.plotly_chart(fig_industry, use_container_width=True)

st.markdown("""
<div class="interpretacao">
<b>Interpretação:</b><br>
O gráfico de pizzas mostra que a Indústria de TI (Tecnologia da Informação), é disparadamente a mais visada em ataques, isso muito pelo fato das grandes empresas de software/hardware além de movimentarem muito dinheiro, também são responsáveis por hospedar sistemas de todas outras indústrias.
Logo em seguida vem o setor Bancário, por ser o responsável por tamanhas movimentações financeiras, e o setor de Assistência Médica, talvez por concentrar um massivo número de informações pessoais de usúarios.
</div>
""", unsafe_allow_html=True)

#Fontes de ataques mais recorrentes
with st.container():
    source_counts = df['Attack Source'].value_counts().nlargest(10)
    fig_source = px.bar(source_counts, 
                        x=source_counts.index, 
                        y=source_counts.values,
                        labels={'x':'Fonte de Ataque', 'y':'Frequência'},
                        title='Fontes de Ataque Mais Frequentes')
    st.plotly_chart(fig_source, use_container_width=True)
  
st.markdown("""
<div class="interpretacao">
<b>Interpretação:</b><br>
A origem de ataque mais frequente se revela ser o próprio Estado-Nação, isso podendo ser coerente ao ato de países buscarem informações sigilosas de países/grupos terroristas inimigos, buscando defesa, ou até mesmo arquitetando ataques.
A menos frequente das origens pesquisadas são Grupo-Hackers, talvez devido a estes grupos agirem por motivações pessoais, sendo menos recorrentes que as outras fontes.
</div>
""", unsafe_allow_html=True)










