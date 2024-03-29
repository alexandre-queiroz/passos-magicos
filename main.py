from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import joblib

st.set_page_config(layout="wide")

# Options Menu
st.sidebar.image("assets/logo2.png")
st.sidebar.markdown("<hr>", unsafe_allow_html=True)
st.sidebar.title("Menu")

# Inicializa a variável de sessão se ainda não estiver definida
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = 'case'


def set_option(option):
    st.session_state.selected_option = option


st.sidebar.button('Apresentação do case', on_click=set_option, args=('case',))
st.sidebar.button('Petróleo Brent (FOB)', on_click=set_option, args=('brent',))
st.sidebar.button('Energia Renovável',
                  on_click=set_option, args=('renewable',))
st.sidebar.button('Estoque Petróleo', on_click=set_option, args=('stock',))
st.sidebar.button('Consumo Petróleo', on_click=set_option,
                  args=('consumption',))
st.sidebar.button('Predição Petróleo Brent',
                  on_click=set_option, args=('predict',))
st.sidebar.button('Tomada de decisão', on_click=set_option, args=('decision',))
st.sidebar.button('Glossário', on_click=set_option, args=('glossary',))
st.sidebar.button('Sobre nós', on_click=set_option, args=('more',))

if st.session_state.selected_option == 'case':
    st.title("Predição do preço do petróleo bruto brent (FOB)")

    st.markdown("##### Foi proposto que fizemos a análise dos dados do preço do petróleo brent, criando um dashboard interativo que gere insights relevantes para tomada de decisão. Além disso desenvolvemos um modelo de Machine Learning para fazer o forecasting do preço do petróleo.")
    st.image("assets/header.jpg")
    st.markdown("Brent é uma sigla, que normalmente acompanha a cotação do petróleo e indica a origem do óleo e o mercado onde ele é negociado. O petróleo Brent foi batizado assim porque era extraído de uma base da Shell chamada Brent. Atualmente, a palavra Brent designa todo o petróleo extraído no Mar do Norte e comercializado na Bolsa de Londres.")

    st.markdown(
        "Os preços dependem principalmente do custo de produção e transporte.")

    st.markdown(
        "O petróleo Brent é produzido próximo ao mar, então os custos de transporte são significativamente menores.")

    st.markdown("O Brent tem uma qualidade menor, mas, se tornou um padrão do petróleo e tem maior preço por causa das exportações mais confiáveis.")

    st.markdown("<hr>", unsafe_allow_html=True)

import streamlit as st

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.header("A cat")
    st.image("assets/logo2.png", width=200)

with tab2:
    st.header("A dog")
    st.image("assets/logo2.png", width=200)

with tab3:
    st.header("An owl")
    st.image("assets/logo2.png", width=200)
    st.markdown(
        "###### Para realização desta análise inicial usamos as seguintes fontes: https://www.eia.gov, https://guru.com.vc/glossario/brent")

# elif st.session_state.selected_option == 'brent':
#     st.title("Analisando o preço do petróleo ao longo do tempo")

#     st.markdown(
#         "Para podermos começar a manipular os dados, precisamos entendê-los melhor, para isso vamos exibir nossos dados em forma de gráficos utilizando séries temporais.")

#     fob_data = get_fob_data()
#     df = process_fob(fob_data)

#     # Criando um gráfico de linhas com Plotly
#     fig = px.line(df, x='Date', y='Value',
#                   title='Valores do petroleo brent FOB ao Longo do Tempo (Preço por Barril)')

#     # Personalizando o layout do gráfico
#     fig.update_layout(xaxis_title='Data',
#                       yaxis_title='Valor (Preço por Barril)')

#     # Exibindo o gráfico
#     st.plotly_chart(fig, use_container_width=True)

#     st.markdown(
#         "##### Após esta análise podemos ver algumas grandes mudanças de preço nos períodos próximos a 2008, 2011, 2014, 2020 e 2022, vamos entender um pouco mais sobre os motivs dessas grandes variações de preço.")
#     st.markdown("<br>", unsafe_allow_html=True)

#     # ------------------------------------- Análise de 2008 ----------------------------------------------------------
#     df_2008 = df[df['Year'] == 2008]
#     df_2008["Periodos de 2008"] = df_2008["Date"]

#     max_value_2008 = df_2008['Value'].max()
#     min_value_2008 = df_2008['Value'].min()

#     if min_value_2008 != 0:
#         variacao_percentual = (
#             (max_value_2008 - min_value_2008) / min_value_2008) * 100
#         # Formatação para duas casas decimais
#         variacao_percentual_texto = f"{variacao_percentual:.2f}%"
#     else:
#         variacao_percentual_texto = "Indefinido"

#     # Exibindo a variação
#     st.markdown(
#         f"##### Período de 2008: Variação entre a máxima e mínima {variacao_percentual_texto}")

#     col1, col2 = st.columns([3, 6])

#     # Coluna 1: Tabela de descrição
#     col1.markdown("<br>", unsafe_allow_html=True)  # Margem superior com HTML
#     col1.markdown("<br>", unsafe_allow_html=True)  # Margem superior com HTML
#     col1.write(df_2008[["Periodos de 2008", "Value"]].describe())

#     # Criando um gráfico de linhas com Plotly
#     fig = px.line(df_2008, x='Date', y='Value', line_shape='spline',
#                   title='Valores do petroleo brent em 2008')

#     # Personalizando o layout do gráfico
#     fig.update_layout(xaxis_title='Data',
#                       yaxis_title='Valor (Preço por Barril)')

#     # Exibindo o gráfico
#     col2.plotly_chart(fig, use_container_width=True)

#     st.markdown("A crise de 2008 começou em razão da especulação imobiliária nos Estados Unidos. Foi a chamada bolha, causada por um aumento abusivo nos valores dos imóveis. Ao atingir preços bem acima do mercado, o setor acabou entrando em colapso, pois a supervalorização não foi acompanhada pela capacidade financeira dos cidadãos de arcar com os custos. Assim, as hipotecas acabaram não tendo a liquidez esperada, ou seja, houve uma quebra econômica em razão do aumento dos juros e da inflação.")

#     st.markdown("A crise financeira global e a Grande Recessão que se seguiu tiveram um impacto negativo pronunciado no setor de petróleo e gás, uma vez que levou a uma queda acentuada nos preços do petróleo e gás e uma contração no crédito. A queda nos preços resultou em queda nas receitas das empresas de petróleo e gás. A crise financeira também levou a condições de crédito restritivas que resultaram em muitos exploradores e produtores pagando altas taxas de juros ao levantar capital, reduzindo assim os ganhos futuros.")

#     st.markdown("<br>", unsafe_allow_html=True)

#     # ------------------------------------- Análise de 2014      ----------------------------------------------------------
#     df_2014 = df[df['Year'] == 2014]
#     df_2014["Periodos de 2014"] = df_2014["Date"]

#     max_value_2014 = df_2014['Value'].max()
#     min_value_2014 = df_2014['Value'].min()

#     if min_value_2014 != 0:
#         variacao_percentual = (
#             (max_value_2014 - min_value_2014) / min_value_2014) * 100
#         # Formatação para duas casas decimais
#         variacao_percentual_texto = f"{variacao_percentual:.2f}%"
#     else:
#         variacao_percentual_texto = "Indefinido"

#     # Exibindo a variação
#     st.markdown(
#         f"##### Período de 2014: Variação entre a máxima e mínima {variacao_percentual_texto}")

#     col1, col2 = st.columns([6, 3])

#     # Coluna 1: Tabela de descrição
#     col2.markdown("<br>", unsafe_allow_html=True)  # Margem superior com HTML
#     col2.markdown("<br>", unsafe_allow_html=True)  # Margem superior com HTML
#     col2.write(df_2014[["Periodos de 2014", "Value"]].describe())

#     # Criando um gráfico de linhas com Plotly
#     fig = px.line(df_2014, x='Date', y='Value', line_shape='spline',
#                   title='Valores do petroleo brent em 2014')

#     # Personalizando o layout do gráfico
#     fig.update_layout(xaxis_title='Data',
#                       yaxis_title='Valor (Preço por Barril)')

#     # Exibindo o gráfico
#     col1.plotly_chart(fig, use_container_width=True)

#     st.markdown("A queda do preço do petróleo em 2014 foi influenciada por vários fatores, incluindo o aumento da produção de petróleo, especialmente nas áreas de xisto dos EUA, e uma demanda menor do que a esperada na Europa e na Ásia. Em novembro do mesmo ano, essa queda se acentuou, diante do excesso de oferta e da recusa dos países da Organização dos Países Exportadores de Petróleo (Opep) em reduzir seu teto de produção, independentemente do preço no mercado internacional. A Opep culpa a grande produção de óleo de xisto pelas baixas cotações da commodity e, segundo alguns analistas, estaria disposta a aceitar um preço ainda mais baixo para tirar do mercado outros produtores ou inviabilizar a exploração de rivais como os produtores norte-americanos.")

#     st.markdown("<br>", unsafe_allow_html=True)

#     # ------------------------------------- Análise de 2020      ----------------------------------------------------------
#     df_2020 = df[df['Year'] == 2020]
#     df_2020["Periodos de 2020"] = df_2020["Date"]

#     max_value_2020 = df_2020['Value'].max()
#     min_value_2020 = df_2020['Value'].min()

#     if min_value_2020 != 0:
#         variacao_percentual = (
#             (max_value_2020 - min_value_2020) / min_value_2020) * 100
#         # Formatação para duas casas decimais
#         variacao_percentual_texto = f"{variacao_percentual:.2f}%"
#     else:
#         variacao_percentual_texto = "Indefinido"

#     # Exibindo a variação
#     st.markdown(
#         f"##### Período de 2020: Variação entre a máxima e mínima {variacao_percentual_texto}")

#     col1, col2 = st.columns([3, 6])

#     # Coluna 1: Tabela de descrição
#     col1.markdown("<br>", unsafe_allow_html=True)  # Margem superior com HTML
#     col1.markdown("<br>", unsafe_allow_html=True)  # Margem superior com HTML
#     col1.write(df_2020[["Periodos de 2020", "Value"]].describe())

#     # Criando um gráfico de linhas com Plotly
#     fig = px.line(df_2020, x='Date', y='Value', line_shape='spline',
#                   title='Valores do petroleo brent em 2020')

#     # Personalizando o layout do gráfico
#     fig.update_layout(xaxis_title='Data',
#                       yaxis_title='Valor (Preço por Barril)')

#     # Exibindo o gráfico
#     col2.plotly_chart(fig, use_container_width=True)

#     texto = """
#     A crise de 2020 entre a Arábia Saudita e a Rússia foi uma queda de braço no mercado do petróleo que causou a maior queda no preço do barril desde 1991, quando Estados Unidos e aliados bombardeavam o Iraque na Guerra do Golfo. A tensão entre os países fez bolsas globais derreterem. Por trás dessa crise, está um xadrez geopolítico complexo e que vai além do petróleo. 

#     O temor relacionado à provável diminuição da oferta por conta de conflitos na região fez os preços do barril de Brent (negociado na Opep, entre países europeus e asiáticos e pela Petrobras) saltarem 3,55% no dia 03 de janeiro, passando de US 66,25 para US 68,60.

#     A história começa com a tentativa saudita de fazer com que os países da Opep (Organização dos Países Exportadores de Petróleo), aliança da qual o reino é líder informal, cortassem a produção diária de barris de petróleo em 1,5 milhão de barris até o final do ano. O plano era diminuir a oferta para conter a queda nos preços, diante da expectativa de redução no consumo de petróleo mundo afora. Os russos não toparam, rompendo uma união que por anos controlou esse mercado. Para retaliar, os sauditas decidiram fazer o inverso: aumentaram a produção e baixaram drasticamente os preços. “Os russos produzem muito petróleo (cerca de 10 milhões de barris por dia) e ganham dinheiro com a escala da operação.

#     Coronavírus e tensão entre Arábia Saudita e Rússia:

#     Conforme a covid-19 avançava pelo mundo e obrigava nações a entrarem em isolamento social, o consumo de combustíveis diminuía. Com isso, a demanda por petróleo também enfrentou uma baixa drástica.
#     """

#     st.markdown(texto)

#     # Criando um boxplot com Plotly
#     fig = px.box(df, x='Year', y='Value', labels={'Year': 'Ano', 'Value': 'Valor'},
#                  title='Boxplot dos Valores do Petróleo brent (FOB) por Ano')

#     # Personalizando o layout do gráfico
#     fig.update_layout(xaxis_title='Ano', yaxis_title='Valor')

#     # Exibindo o gráfico
#     st.plotly_chart(fig, use_container_width=True)

#     st.markdown("<hr>", unsafe_allow_html=True)

#     st.markdown(
#         "###### Para realização desta análise do preço do petróleo brent usamos as seguintes fontes:\n"
#         "https://www.eia.gov, https://blog.stoodi.com.br/blog/historia/crise-de-2008, "
#         "https://economiaenegocios.com/como-a-crise-financeira-de-2008-afetou-o-setor-de-petroleo-e-gas, "
#         "https://exame.com/mundo/o-que-esta-por-tras-da-queda-de-braco-entre-arabia-saudita-e-russia, "
#         "https://einvestidor.estadao.com.br/investimentos/preco-petroleo-2020, "
#         "https://blog.stoodi.com.br/blog/historia/crise-do-petroleo-o-que-foi, "
#         "https://epoca.oglobo.globo.com/tempo/noticia/2015/01/entenda-os-motivos-para-bqueda-do-preco-do-petroleob.html, "
#         "https://g1.globo.com/economia/noticia/2015/01/entenda-queda-do-preco-do-petroleo-e-seus-efeitos.html"
#     )

# elif st.session_state.selected_option == 'renewable':
#     st.title("Analisando o crescimento da energia renovável")

#     st.markdown(
#         "Um ponto interessante que podemos analisar é o crescimento das fontes de energia renovável e seu impacto no consumo/preço do petróleo.")

#     renewable_data = get_renewable_energy_data()
#     df2 = pd.DataFrame(renewable_data['response']['data'])
#     df2 = df2[["period", "productName", "value"]]
#     df2['value'] = pd.to_numeric(df2['value'], errors='coerce')

#     # Supondo que df2 seja o seu DataFrame e que ele contenha as colunas 'period', 'value' e 'productName'
#     # Separando os dados para "Renewables" e "Electricity"
#     df_renewables = df2[df2['productName'] == 'Renewables']
#     df_electricity = df2[df2['productName'] == 'Electricity']

#     # Juntando os dados com base no 'period'
#     merged_df = pd.merge(df_renewables, df_electricity,
#                          on='period', suffixes=('_renew', '_elec'))

#     # Calculando a porcentagem de "Renewables" em relação a "Electricity" para cada período
#     merged_df['renewable_percentage'] = (
#         merged_df['value_renew'] / merged_df['value_elec']) * 100

#     # Agora, você pode adicionar esta porcentagem ao seu DataFrame original para uso no gráfico
#     # Por simplicidade, vou adicionar apenas a 'percentage' de volta ao df2, mas você pode ajustar conforme necessário
#     df2 = pd.merge(
#         df2, merged_df[['period', 'renewable_percentage']], on='period', how='left')

#     fig = px.line(df2, x='period', y='value', color='productName',
#                   title='Consumo de energia ao longo do tempo por Produto (BKWH)',
#                   hover_data={'renewable_percentage': ':.2f'})

#     # Personalizando o layout do gráfico
#     fig.update_layout(xaxis_title='Data', yaxis_title='Valor',
#                       legend_title='Produto')

#     # Exibindo o gráfico
#     st.plotly_chart(fig, use_container_width=True)

#     st.markdown("Antes de iniciar a avaliação do impacto da energia renovável ao preço do petróleo, vamos entender o que é energia renovável.\n"
#                 "Quando falamos de energia, falamos da energia elétrica, ou da eletricidade, utilizada no nosso quotidiano, e quando a qualificamos como renovável, dizemos que esta fonte de energia é renovada rapidamente pela natureza.\n"
#                 "Ou seja, uma fonte de energia renovável é aquela reposta tão ou mais rapidamente do que a podemos consumir. Dessa forma, não estamos a extrair da natureza mais do que ela nos possa dar. Pelo contrário: é uma lógica de consumo sustentável. E atenção: não apenas extraímos menos recursos, como extraímos recursos melhores, que não agridem o planeta.\n\n"
#                 "##### Os 7 tipos de energia renovável conhecidos até ao momento:\n"
#                 "* Energia Solar: Energia renovável obtida através da transformação da energia luminosa do sol em elétrica. \n"
#                 "* Energia Eólica: Tipo de energia renovável obtida através da transformação da energia cinética dos ventos em elétrica.\n"
#                 "* Energia Hidráulica: Modalidade de energia renovável obtida através da transformação da energia cinética dos cursos de água em elétrica.\n"
#                 "* Energia Geotérmica: Energia renovável obtida através da transformação da energia térmica das águas quentes e vapores do interior da Terra em elétrica.\n"
#                 "* Energia Maremotriz: Tipo de energia renovável obtida através da transformação da energia cinética das ondas e marés em elétrica.\n"
#                 "* Energia do Hidrogénio: Energia obtida a partir da combinação entre o hidrogénio e o oxigénio, que liberta energia térmica, posteriormente convertida em eletricidade.\n"
#                 "* Biomassa: Energia obtida durante a transformação de derivados de organismos vivos para a produção de energia calorífica, que é de seguida convertida em elétrica.\n")

#     st.markdown("<br>", unsafe_allow_html=True)
#     st.image("assets/tipos_energia.png")
#     st.markdown("<br>", unsafe_allow_html=True)

#     st.markdown("##### E como a energia renovável pode afetar o preço do petróleo?\n\n"
#                 "A consequência imediata da redução no preço do barril do petróleo é o crescimento da demanda por combustíveis fósseis e fontes de energia proveniente do petróleo, porém, existem outros efeitos desastrosos a longo prazo, tais como os impactos nos investimentos em geração de energia renováveis, pois a energia é uma commodity, e os consumidores não querem pagar mais caro pela energia, estes desejam energia sustentável com baixa emissão de gases de efeito estufa (GEEs), mas com preço baixos. É importante salientar que o preço do petróleo é balizador do preço da energia, ou seja, quanto menor o preço do petróleo menor o preço da energia, diminuindo as taxas de retorno dos projetos em energia, incluindo os projetos de energia renováveis. A deterioração do preço do petróleo deve continuar, pois recentemente as sanções comerciais ao Irã (7º maior produtor do mundo) se encerram, criando mais excedente de petróleo. Esse cenário vem impactando às ações de empresas de energia listadas na FTSE e NYSE e levantando dúvidas sobre a capacidade de endividamento e a viabilidade de novos projetos de energia, principalmente, a energias renováveis. E como está o consumo de energia do petróleo x consumo de energia renovável atualmente? O Relatório de Estado Global de Energias Renováveis ​​2022 da REN21 (GSR 2022) declara que a transição global para energia limpa não está a acontecer, tornando improvável que o mundo seja capaz de cumprir metas climáticas críticas nesta década. “Ainda que muitos outros governos se comprometam com zero emissões de gases de efeito estufa em 2021, a realidade é que, em resposta à crise energética, a maioria dos países voltou a utilizar novas fontes de combustíveis fósseis e a queimar ainda mais carvão, petróleo e gás natural”, declarou Rana Adib, Directora Executiva da REN21. O GSR faz anualmente um balanço da implantação de energia renovável em todo o mundo. O relatório de 2022 é a 17ª edição consecutiva e comprova o que os especialistas têm alertado: a participação geral das energias renováveis ​​no consumo final de energia do mundo estagnou – subindo apenas de 8,7% em 2009 para 11,7% em 2019 – e o crescimento global a mudança do sistema energético para as energias renováveis ​​não está a acontecer. No sector de electricidade, foram atingidos valores recorde em capacidade de energia renovável (314,5 gigawatts, 17% acima de 2020) e geração (7.793 terawatts-hora) não conseguiram corresponder ao aumento geral no consumo de electricidade de 6%. No aquecimento e arrefecimento, a quota de energias renováveis ​​no consumo final de energia aumentou de 8,9% em 2009 para 11,2% em 2019. No sector dos transportes, onde a quota de energias renováveis ​​passou de 2,4% em 2009 para 3,7% em 2019, a falta de progressos é particularmente preocupante, já que o sector responde por quase um terço do consumo global de energia."
#                 "\n\n"
#                 "##### Qual a previsão sobre o uso das Energias Renovaveis?\n\n"
#                 "A geração de energia por meio da luz solar cresceu 12% no mundo e, segundo a Agência Internacional de Energia (IEA), esse progresso não deve parar. Muito pelo contrário, visto que diversos países pretendem investir em fontes renováveis com o intuito de reduzir substancialmente a emissão de carbono durante a próxima década. Por conta disso, a tendência é que o uso primário de energias renováveis cresça em torno de 60% nos próximos 30 anos. Segundo a multinacional British Petroleum, esse aumento será uma resposta inevitável à queda das fontes que dependem de combustíveis fósseis. Não é à toa que a empresa investiu mais de um bilhão de dólares em usinas de energia eólica dos Estados Unidos. Uma decisão estratégica que não ignora a força ainda maior que a energia renovável terá no futuro."
#                 )
#     st.image("assets/energia.jpg")

#     st.markdown(
#         "###### Para realização desta análise usamos as seguintes fontes:\n"
#         "https://www.epe.gov.br/pt/abcdenergia/matriz-energetica-e-eletrica,"
#         "https://goldenergy.pt/blog/energia-verde/tipos-de-energia-renovavel/"
#     )

# elif st.session_state.selected_option == 'stock':
#     st.title("Analisando o estoque mundial de petróleo")

#     st.markdown("A oferta e demanda estão completamente ligadas ao preço do petróleo, caos haja muito petróleo em estoque não há necessidade de comprar/vender mais petróleo acarretando em um menor demanda portanto em um preço menor por barril.")

#     stock_data = get_petroleum_stock()
#     df3 = pd.DataFrame(stock_data['response']['data'])
#     df3 = df3[["period", "productName", "value"]]
#     df3['value'] = pd.to_numeric(df3['value'], errors='coerce')

#     df3.sort_values('period', inplace=True)

#     # Criando um gráfico de linhas com Plotly
#     fig = px.line(df3, x='period', y='value',
#                   title='Estoque de petroleo ao Longo do Tempo')

#     # Personalizando o layout do gráfico
#     fig.update_layout(xaxis_title='Data', yaxis_title='Valor')

#     # Exibindo o gráfico
#     st.plotly_chart(fig, use_container_width=True)

#     st.markdown("* Excesso de Oferta: Quando os estoques de petróleo estão constantemente aumentando, isso pode indicar um excesso de oferta no mercado. Um excesso de oferta significa que há mais petróleo disponível do que a demanda do mercado pode absorver, levando geralmente a uma queda nos preços.\n\n"
#                 "* Pressão nos Preços à Vista: O aumento do estoque de petróleo pode criar pressão descendente nos preços do petróleo à vista (spot prices). Os preços à vista refletem as condições de oferta e demanda imediatas e são influenciados pela disponibilidade de petróleo no curto prazo.\n\n"
#                 "* Redução da Capacidade de Armazenamento: Se os estoques atingirem níveis muito altos e a capacidade de armazenamento estiver próxima do limite, os produtores podem ser forçados a vender o petróleo a preços mais baixos para evitar custos adicionais associados ao armazenamento.\n\n"
#                 "* Decisões da OPEP e Outros Produtores: A Organização dos Países Exportadores de Petróleo (OPEP) e outros grandes produtores de petróleo frequentemente ajustam sua produção em resposta às condições do mercado. Se os estoques estiverem altos e os preços estiverem sob pressão, a OPEP e outros produtores podem considerar a redução da produção para equilibrar o mercado e sustentar os preços.\n\n"
#                 "* Expectativas do Mercado: Os participantes do mercado, como investidores e traders, frequentemente reagem às informações sobre os estoques de petróleo. Se os estoques estiverem aumentando constantemente, isso pode influenciar as expectativas do mercado sobre os futuros movimentos dos preços, levando a uma venda antecipada e à queda dos preços.\n\n"
#                 "É importante observar que outros fatores também influenciam os preços do petróleo, como eventos geopolíticos, mudanças na demanda global, condições econômicas e desenvolvimentos tecnológicos. Além disso, os mercados de petróleo são frequentemente voláteis e podem ser afetados por eventos imprevistos. Assim, a relação entre os estoques de petróleo e os preços é complexa e dinâmica.")

#     st.markdown("Estoques globais de petróleo e cotação do Brent:")
#     st.image("assets/estoque.png")

#     st.subheader("Fontes:")
#     st.markdown("* OPEP - https://www.epe.gov.br/sites-pt/publicacoes-dados-abertos/publicacoes/PublicacoesArquivos/publicacao-542/NT-EPE-DPG-SDB-2020-04_Pre%C3%A7os%20Petr%C3%B3leo%20e%20Derivados_2020_2030.pdf.\n * IBP - https://www.ibp.org.br/personalizado/uploads/2021/06/relacao-entre-estoques-e-preco-do-petroleo.pdf#:~:text=Desse%20modo%2C%20uma%20eleva%C3%A7%C3%A3o%20dos%20estoques%20pode%20indicar,o%20pre%C3%A7o%20spot%20cair%C3%A1%20para%20reequilibrar%20o%20mercado.")

# elif st.session_state.selected_option == 'consumption':

#     st.title(
#         "Como o consumo de petróleo afeta o valor do petróleo? - Demanda e Oferta\n\n")
#     st.markdown("Ao final de 2019, as condições da indústria mundial do petróleo indicavam a continuidade, no curto prazo, da dinâmica até então vigente – um equilíbrio tênue entre oferta e demanda que manteve os preços spot do petróleo Brent em relativa estabilidade, oscilando entre US$ 60/b e US$ 70/b. Contudo, os primeiros meses de 2020 foram marcados por eventos relevantes que acarretaram variações significativas nos preços internacionais do petróleo.\n\n"
#                 "Medidas de distanciamento social e restrições à mobilidade, visando à redução da circulação de pessoas, têm sido amplamente adotadas em grande parte do mundo como prevenção à pandemia de Covid-19. Embora variem em espectro, tais ações têm impactado a mobilidade, com consequências sobre consumo, serviços e atividade industrial, reduzindo o nível da atividade econômica mundial. Assim, a pandemia tem infligido efeitos consideráveis sobre a demanda mundial de petróleo. As atividades dos transportes rodoviários de passageiros e aéreo foram as mais afetadas pela ampla adoção de medidas de restrição à mobilidade no mundo, levando a reduções históricas no consumo global de gasolina e de querosene de aviação (QAV) (IEA, 2020a).\n\n"
#                 "Ao mesmo tempo em que a demanda foi severamente impactada, a indústria do petróleo observou alterações na dinâmica da oferta mundial. O acordo para limitar a produção entre países-membros da Organização dos Países Exportadores de Petróleo (OPEP) e outros grandes produtores, em especial a Rússia, não foi renovado no início de março de 2020. Em abril, a Arábia Saudita anunciou o aumento da sua produção para mais de 12 milhões b/d, retomando a política de disputa de mercado. Em seguida, a OPEP+ (grupo formado pelos membros da OPEP, Rússia e outros países produtores) fechou acordo para a redução da sua oferta de petróleo, inicialmente com cortes de 9,7 milhões b/d a partir de maio. Simultaneamente, retrações adicionais de produção foram observadas em outros países, com destaque para Estados Unidos e Canadá (IEA, 2020a).\n")

#     consumption_data = get_consumption()
#     df4 = pd.DataFrame(consumption_data['response']['data'])
#     df4 = df4[["period", "productName", "value"]]
#     df4['value'] = pd.to_numeric(df4['value'], errors='coerce')

#     df4.sort_values('period', inplace=True)

#     # Criando um gráfico de linhas com Plotly
#     fig = px.line(df4, x='period', y='value',
#                   title='Consumo de petroleo ao Longo do Tempo')

#     # Personalizando o layout do gráfico
#     fig.update_layout(xaxis_title='Data', yaxis_title='Valor')

#     # Exibindo o gráfico
#     st.plotly_chart(fig, use_container_width=True)

#     st.markdown("Abaixo incluímos um gráfico que apresenta a progressão de Oferta e Demanda Mundial do Petróleo ao longo de 7 trimestres. \n")
#     st.image("assets/oferta_demanda.jpg")

#     st.subheader("Fontes:")
#     "* EPE - https://www.epe.gov.br/sites-pt/publicacoes-dados-abertos/publicacoes/PublicacoesArquivos/publicacao-542/NT-EPE-DPG-SDB-2020-04_Pre%C3%A7os%20Petr%C3%B3leo%20e%20Derivados_2020_2030.pdf."

# elif st.session_state.selected_option == 'glossary':
#     st.markdown("<br>", unsafe_allow_html=True)
#     st.image("assets/glossario.jpg")

#     st.title("Glossário")

#     st.markdown(
#         "#### OCDE (Organização para a Cooperação e Desenvolvimento Econômico):\n\n")
#     "Organização para a Cooperação e Desenvolvimento Econômico é uma organização econômica intergovernamental com 38 países membros, fundada em 1961 para estimular o progresso econômico e o comércio mundial.\n\n"
#     "É um fórum de países que se descrevem comprometidos com a democracia e a economia de mercado, oferecendo uma plataforma para comparar experiências políticas, buscar respostas para problemas comuns, identificar boas práticas e coordenar as políticas domésticas e internacionais de seus membros. A maioria dos membros da OCDE é formada por economias de alta renda com um Índice de Desenvolvimento Humano (IDH) muito alto e consideradas países desenvolvidos. Em 2017, os países membros da OCDE representavam coletivamente 62,2% do PIB nominal global (49,6 trilhões de dólares) e 42,8% do PIB global (54,2 trilhões de dólares internacionais) por paridade de poder de compra. A organização é um observador oficial das Nações Unidas. \n\n"
#     "São países membros: Alemanha, Austrália, Áustria, Bélgica, Canadá, Chile, Colômbia, Coréia, Costa Rica, Dinamarca, Eslováquia, Eslovênia, Espanha, Estados Unidos, Estônia, Finlândia, França, Grécia, Hungria, Irlanda, Islândia, Israel, Itália, Japão, Letônia, Lituânia, Luxemburgo, México, Noruega, Nova Zelândia, Países Baixos, Polônia, Portugal, Reino Unido, República Checa, Suécia, Suíça e Turquia."

#     st.markdown(
#         "#### OPEP (Organização dos Países Exportadores de Petróleo):\n\n")
#     "OPEP é o acrônimo de Organização dos Países Exportadores de Petróleo, uma organização internacional criada em 1960 com o objetivo de restringir a oferta no mercado internacional e pensar de forma conjunta a política de venda dos países-membros.\n\n"
#     "Atualmente a OPEP conta com 14 países: Arábia Saudita, Emirados Árabes, Irã, Iraque, Kuwait, Catar, Angola, Argélia, Gabão, Guiné Equatorial, Líbia, Nigéria, Venezuela, Equador, e Indonésia. A OPEP é muito poderosa e sua atuação está inteiramente relacionada às crises que se seguiram"

#     st.markdown("####  PETRÓLEO BRENT: \n\n")
#     "O termo Petróleo Brent designa a origem de extração do petróleo. No caso do Brent, o nome se dá por conta de uma base da Shell chamada Brent. Atualmente, esse termo diz respeito a todo o petróleo que é extraído no Mar do Norte."

#     st.subheader("Fontes:")
#     "* OCDE - https://pt.wikipedia.org/wiki/Organiza%C3%A7%C3%A3o_para_a_Coopera%C3%A7%C3%A3o_e_Desenvolvimento_Econ%C3%B4mico.\n* OPEP - https://blog.stoodi.com.br/blog/historia/crise-do-petroleo-o-que-foi/.\n * BRENT - https://www.mobills.com.br/blog/investimentos/petroleo-brent-grafico/."

# elif st.session_state.selected_option == 'predict':
#     st.title("Predição do Petróleo Brent")

#     st.markdown(
#         "Com base em todos os dados que foram analisados até agora será feita a predição dos próximos valores do petróleo brent.")

#     fob_data = get_fob_data()
#     df = process_fob(fob_data)

#     renewable_data = get_renewable_energy_data()
#     df2 = pd.DataFrame(renewable_data['response']['data'])
#     df2 = df2[["period", "productName", "value"]]
#     df2['value'] = pd.to_numeric(df2['value'], errors='coerce')
#     df2['value'] = round(df2['value'], 3)

#     stock_data = get_petroleum_stock()
#     df3 = pd.DataFrame(stock_data['response']['data'])
#     df3 = df3[["period", "productName", "value"]]
#     df3['value'] = pd.to_numeric(df3['value'], errors='coerce')

#     consumption_data = get_consumption()
#     df4 = pd.DataFrame(consumption_data['response']['data'])
#     df4 = df4[["period", "productName", "value"]]
#     df4['value'] = pd.to_numeric(df4['value'], errors='coerce')

#     df_renewables = df2[df2['productName'] == 'Renewables']
#     df_electricity = df2[df2['productName'] == 'Electricity']

#     # Juntando os dados com base no 'period'
#     merged_df = pd.merge(df_renewables, df_electricity,
#                          on='period', suffixes=('_renew', '_elec'))

#     # Calculando a porcentagem de "Renewables" em relação a "Electricity" para cada período
#     merged_df['percentage'] = (
#         merged_df['value_renew'] / merged_df['value_elec']) * 100

#     # Agora, você pode adicionar esta porcentagem ao seu DataFrame original para uso no gráfico
#     # Por simplicidade, vou adicionar apenas a 'percentage' de volta ao df2, mas você pode ajustar conforme necessário
#     df2 = pd.merge(
#         df2, merged_df[['period', 'percentage']], on='period', how='left')

#     df2_filtrado = df2[df2['productName'] == 'Renewables']
#     df2_filtrado['Year'] = df2_filtrado['period'].apply(
#         lambda x: int(str(x)[:4]))

#     merged_df = pd.merge(
#         df, df2_filtrado[["percentage", "Year"]], on='Year', how='left')

#     last_percentage = df2_filtrado['percentage'].iloc[0]
#     merged_df['percentage'].fillna(last_percentage, inplace=True)

#     merged_df2 = pd.merge(merged_df, df3[[
#                           "value", "period"]], left_on='MonthYear', right_on='period', how='left')

#     last_stock = df3['value'].iloc[0]
#     merged_df2['value'].fillna(last_stock, inplace=True)

#     merged_df2.rename(
#         columns={'value': 'stock', 'percentage': 'renewable_percentage'}, inplace=True)
#     merged_df2.drop(columns=['period'], inplace=True)

#     merged_df3 = pd.merge(merged_df2, df4[[
#                           "value", "period"]], left_on='MonthYear', right_on='period', how='left')

#     merged_df3.rename(columns={'value': 'consumption'}, inplace=True)
#     merged_df3.drop(columns=['period'], inplace=True)

#     last_consumption = df3['value'].iloc[0]
#     merged_df3['consumption'].fillna(last_consumption, inplace=True)

#     # Converter a coluna 'Date' e 'MonthYear' para formatos numéricos
#     merged_df3['Date'] = pd.to_datetime(
#         merged_df3['Date']).map(pd.Timestamp.toordinal)
#     merged_df3['Year'] = pd.to_datetime(merged_df3['MonthYear']).dt.year
#     merged_df3['Month'] = pd.to_datetime(merged_df3['MonthYear']).dt.month
#     merged_df3.drop('MonthYear', axis=1, inplace=True)

#     # Loop que executa 100 vezes
#     for _ in range(60):
#         last_prediction = model.predict(
#             merged_df3.iloc[-1:].drop(['Value'], axis=1))

#         # Calcular a média móvel dos últimos 7 e 30 dias e aplicar o multiplicador
#         sma_7 = merged_df3['Value'].iloc[-7:].mean()
#         sma_30 = merged_df3['Value'].iloc[-30:].mean()

#         # Calcular o desvio padrão dos últimos 7 e 30 dias e aplicar o multiplicador
#         std_7 = merged_df3['Value'].iloc[-7:].std()
#         std_30 = merged_df3['Value'].iloc[-30:].std()

#         # Calcular o valor mínimo e máximo dos últimos 7 dias e aplicar o multiplicador
#         min_7 = merged_df3['Value'].iloc[-7:].min()
#         max_7 = merged_df3['Value'].iloc[-7:].max()

#         # Obtenha os valores originais dos campos
#         renewable_percentage = merged_df3.iloc[-1]["renewable_percentage"]
#         stock = merged_df3.iloc[-1]["stock"]
#         consumption = merged_df3.iloc[-1]["consumption"]

#         # Aplique o multiplicador aos valores originais
#         renewable_percentage *= (1 + 0.001)
#         stock *= (1 + 0.002)
#         consumption *= (1 + 0.005)

#         base_linha = {
#             'Date': merged_df3.iloc[-1]["Date"] + 1,
#             'Value': last_prediction[0],
#             'Year': merged_df3.iloc[-1]["Year"],
#             'SMA_7': sma_7,
#             'SMA_30': sma_30,
#             'STD_7': std_7,
#             'STD_30': std_30,
#             'MIN_7': min_7,
#             'MAX_7': max_7,
#             'renewable_percentage': renewable_percentage,
#             'stock': stock,
#             'consumption': consumption,
#             'Month':  merged_df3.iloc[-1]["Month"],
#         }

#         nova_linha = pd.DataFrame([base_linha])
#         merged_df3 = pd.concat([merged_df3, nova_linha], ignore_index=True)

#     # Certifique-se de que o DataFrame tem pelo menos 200 linhas
#     if len(merged_df3) >= 200:
#         merged_df3 = merged_df3.iloc[-200:]

#     X_merged_df3 = merged_df3.drop(['Value'], axis=1)

#     # Fazer previsões com o modelo treinado
#     y_pred_merged_df3 = model.predict(X_merged_df3)

#     merged_df3['Value'] = merged_df3['Value'].iloc[:-99]

#     X_merged_df3['Predicted'] = y_pred_merged_df3

#     from datetime import datetime

#     # Função para converter número ordinal em data
#     def ordinal_to_date(ordinal):
#         try:
#             return datetime.fromordinal(int(ordinal))
#         except (ValueError, OverflowError):
#             return pd.NaT  # Retorna 'Not a Time' para valores inválidos

#     # Convertendo a coluna 'Date'
#     merged_df3['Date'] = merged_df3['Date'].apply(ordinal_to_date)
#     X_merged_df3['Date'] = X_merged_df3['Date'].apply(ordinal_to_date)

#     # Definir 'Date' como índice
#     merged_df3.set_index('Date', inplace=True)
#     X_merged_df3.set_index('Date', inplace=True)

#     # Criar um DataFrame para o gráfico usando o índice
#     df_graph = pd.DataFrame({
#         'Actual': merged_df3['Value'],
#         'Predicted': X_merged_df3['Predicted']
#     })

#     # Criar o gráfico
#     fig = go.Figure()

#     ultima_data = merged_df3[~merged_df3['Value'].isna()].index[-1]

#     # Adicionar uma linha separando a marca de 100 índices
#     # Nota: Esta parte pode precisar de ajustes, pois 'x0' e 'x1' devem ser datas, não números
#     fig.add_shape(
#         go.layout.Shape(
#             type="line",
#             x0=ultima_data,  # Exemplo: substitua por uma data real
#             x1=ultima_data,  # Exemplo: substitua por uma data real
#             y0=df_graph['Actual'].min() - 6,
#             y1=df_graph['Actual'].max() + 6,
#             line=dict(color="gray", width=2, dash="dash")
#         )
#     )

#     # Adicione o traço para os Valores Reais com legenda "Actual"
#     fig.add_trace(go.Scatter(
#         x=df_graph.index, y=df_graph['Actual'], mode='lines', name='Real'))

#     # Adicionar um traço para os Valores Previstos com legenda
#     fig.add_trace(go.Scatter(
#         x=df_graph.index, y=df_graph['Predicted'], mode='lines', name='Previsto', line=dict(color='orange')))

#     fig.update_layout(title='Comparação entre Valores Reais e Valores Previstos (Próximos 60 dias)',
#                       xaxis_title='Data',
#                       yaxis_title='Preço por barril (US$)',
#                       legend_title='Legenda',
#                       xaxis=dict(type='date'))  # Configurar o eixo x para mostrar datas

#     # Mostrar o gráfico
#     st.plotly_chart(fig, use_container_width=True)

#     st.write(X_merged_df3[["Predicted", "MIN_7",
#              "MAX_7", "SMA_7", "SMA_30"]].tail(100))

# elif st.session_state.selected_option == 'decision':
#     st.title("Tomada de Decisão")

#     st.markdown(
#         "#### Para auxiliar na tomada de decisão, realizamos quatro tipos de análises:")

#     st.markdown("1. Análise do preço do petróleo\n"
#                 "2. Análise do uso de energia renovável\n"
#                 "3. Análise do estoque de petróleo\n"
#                 "4. Análise do consumo de petróleo\n")

#     st.markdown("Com base em nossa análise preditiva, que contempla os próximos 100 dias, observarmos que o valor se manterá estável, ou seja, dentro do valor médio no período de Fevereiro a Maio de 2024, enquanto no período de Dezembro a Janeiro, o valor sofre uma deflação.")

#     st.markdown("É importante ressaltar que o valor pode sofrer diversas alterações, devido a uma gama de variáveis, conforme as análises realizadas, como crises econômicas, eventos geopoliticos, mudanças na demanda global, condições economicas e desenvolvimentos técnologicos, conforme citado anteriormente.")

#     st.markdown("Além disso, com o aumento do consumo de energia renovável, pode existir um impacto, mesmo que não muito significativo.")

#     st.markdown(
#         "Como também o impacto do aumento do estoque do petróleo que pode fazer com que a oferta supere a demanda.")

#     st.title("Conclusão")

#     st.markdown(
#         "De forma geral, recomendariamos que a compra do petróleo fosse realizada no periodo de baixa do valor, conforme análise preditiva, e caso necessário, a venda no periodo de estabilidade, ou aumento do valor. Considerando os fatores acima, e acompanhando a evolução do mercado.")

#     st.markdown("É importante ressaltar que informações como OPEP, OCDE, bem como noticias do mercado mundial devem ser acompanhadas diariamente")

#  elif st.session_state.selected_option == 'more':
#      st.title("Sobre nós")

#      st.markdown(

#          "Essa atividade foi realizada pelos integrantes Alexandre Augusto de Oliveira Queiroz, Bruna Borges de Moura Scarpe e Hadassa Caroline Juricic, que fazem parte do curso de pós graduação em Análise de dados da FIAP.\n"
#          "Nos foi proposto nesse desaio do Tech Challenge 4, realizar um trabalho analisando os dados de preço do petróleo brent, onde fizemos diversas análises, criamos um modelo de machine learning para prever o preço do petróleo e defininos insights que nos gerou bons resulatos para tomada de decisão. ")

#      st.image("assets/obg.png")
