
from nltk.corpus import stopwords
import streamlit as st
import plotly.express as px
from wordcloud import WordCloud
from pywaffle import Waffle
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import nltk
import plotly.graph_objects as go
import networkx as nx
import numpy as np
import random
import pandas as pd
import json
from utils.leia import SentimentIntensityAnalyzer

# Baixe os recursos necessários
nltk.download('vader_lexicon')
nltk.download('stopwords')
# Function to create sidebar
st.set_page_config(page_title="Passos Mágicos", layout="wide")


def create_sidebar():
    st.sidebar.image('assets/logo-passos.png', use_column_width=True)
    st.sidebar.title("Passos Mágicos")
    st.sidebar.markdown(
        """
    ## A Associação Passos Mágicos
    
    A Associação Passos Mágicos tem uma trajetória de 30 anos de atuação, trabalhando na transformação da vida de crianças e jovens de baixa renda os levando a melhores oportunidades de vida.

    A transformação, idealizada por Michelle Flues e Dimetri Ivanoff, começou em 1992, atuando dentro de orfanatos, no município de Embu-Guaçu.

    Em 2016, depois de anos de atuação, decidem ampliar o programa para que mais jovens tivessem acesso a essa fórmula mágica para transformação que inclui: educação de qualidade, auxílio psicológico/psicopedagógico, ampliação de sua visão de mundo e protagonismo. Passaram então a atuar como um projeto social e educacional, criando assim a Associação Passos Mágicos.
    """
    )


def create_main_content():
    # Displaying a title and subtitle for the main page
    st.title("Transformando Vidas: O Impacto da Passos Mágicos Além dos Estudos")
    st.write("""
Nosso objetivo é destacar a significância do trabalho realizado pela Passos Mágicos e como ele desempenha um papel crucial na transformação das vidas de inúmeras pessoas, indo muito além do âmbito puramente acadêmico. Para isso, buscamos entender a essência dessa jornada por meio de depoimentos de alunos da Passos Mágicos, identificando as palavras-chave que melhor refletem essa experiência. Entre elas estão: Projeto, sonho, transformação, comunidade, vida, família, trabalho, professores, progresso e história.

Esses termos evidenciam a amplitude do impacto da ONG, que vai desde a realização de sonhos individuais até a transformação de comunidades e famílias inteiras. Através do apoio e da orientação fornecidos pela Passos Mágicos, cada integrante dessa jornada é capacitado a construir um futuro mais promissor, moldando não apenas seu próprio destino, mas também contribuindo para o desenvolvimento de uma sociedade mais inclusiva e igualitária.
             """)

    # Sample text for the word cloud
    text = """Em 2016, Yuri fez a melhor escolha de sua vida: ingressar na Associação Passos Mágicos. Na época, ele não fazia ideia do quão longe iria e da transformação que aconteceria em sua vida e na história de sua família. Hoje, Yuri se sente imensamente grato por essa decisão.

Yuri descreve sua evolução desde um jovem calado e recluso até se tornar alguém com grandes ambições e conquistas. Ele foi um aluno esforçado, se tornou um universitário sonhador e, finalmente, um estagiário com sede de crescimento. Agora, ele inicia sua luta para se tornar um verdadeiro protagonista, contribuindo ativamente para que outras centenas de crianças e jovens tenham oportunidades ainda melhores do que as que ele teve.

A Associação Passos Mágicos é uma porta aberta para que as crianças alcancem seus sonhos, enxerguem além de sua realidade cotidiana e se desenvolvam profissional, educacional e socialmente. Yuri expressa sua gratidão aos mentores, professores e colegas que o apoiaram nessa jornada transformadora. Ele também destaca a importância do sentimento de gratidão por todas as experiências, quedas, derrotas e vitórias que moldaram seu caminho.

Agora, como todo passarinho, Yuri bate suas asas e voa em busca de seus próprios sonhos, mas sempre lembrando da família e da comunidade que o ajudaram a chegar tão longe. Sua história é um testemunho inspirador do impacto positivo que a Passos Mágicos tem na vida das pessoas.

Olá, me chamo Raphaela Soares da Silva, tenho 19 anos, sou aluna do curso de Enfermagem na Universidade Santo Amaro.O projeto Passos Mágicos me cedeu a oportunidade de realizar um nano curso na plataforma da Fiap sobre "Libras".Aprender a língua Brasileira de Sinais é importante e a própria foi criada...

O Programa Sacode a Poeira foi a melhor coisa que me aconteceu nesse momento tão difícil, em que estamos vivendo, pois me deu muita motivação para cumprir minhas obrigações, a minha rotina está mais organizada, e com isso não estou ficando tão estressada, por causa do acumulo de tarefas, mas o melhor de tudo isso é que estou tendo mais tempo livre, diferente de antes...

Passos Mágicos é família, e quando falamos de família, vem junto a educação, as broncas (que com o tempo vemos que são muito necessárias), os conselhos que levamos para a vida e o mais importante, o AMOR...

Oi, meu nome é Eliane, tenho 22 anos e essa é a minha história.
Eu conheci a passos médicos, salvo me engano em novembro de 2015.
A gente me trabalhava em um fanato e ela foi apresentada pelo pastor que cuidava daquele fanato
a Tcha Michel e a Tjimite.
E eles iam na minha casa, a minha apresentar, uma passos, né.
E eu oferecero pra mim pra minha mão uma bolsa de estudos na união.
Eu entra aí no segundo ano, no estino médio e minha irmã no sexto.
Eu, de princípio, não queria aceitar, mas aceitei.
E desde então começou a minha trayetória na passos médicos.
Entrei na escola em 2016, com um testigo da área em várias matérias.
Achando que não iria conseguir passar, mas também com muita determinação.
Se dava a fim com várias horas do dia, constantemente até conseguir minha aprovação no segundo ano, no desno médio e no terceiro ano no ensino médio.
Em dezembro, numação de natal, eu fui presentiada pela passos a ganhar a primeira bolsa de estudos na faculdade, na Universidade Estácia de Sa, em direito.
Então, nasci os primeiro universitário da passos, criei no bolso de direito na faculdade estácil.
Em dezem, então, eu subi a cinco, né, por cinco anos, muito choro, muita alegria, noites mal dormidas.
Mas também, com muita esperança de o dia me tornar uma juiza, uma divulgada, né, alguém pra ajudar outras pessoas assim como fizeram comigo.
Então, em 12 do 2, de 2023, eu me for ver em direito, né, pela faculdade estácil de Sa.
Estou aqui pra dizer, não desize dos seus sonhos, tudo é possível quando você acredita neles.
Então, agradeço muito a Deus, porque sem Ele, eu não estaria aqui hoje, agradeço muito a Tcha Michel, a gente de Mitre e todos os professores da passos mágicos,
porque eles também me ajudaram, me apoiaram pra chegar até aqui hoje. Então, essa é minha história.

Oi gente, tudo bem? Eu sou a Macarena Correia e hoje é um dia incrível, um dia super especial.
Hoje é dia das mulheres, é o nosso dia. E eu estou aqui para para benizar todas as mulheres,
passos mágicos, muito obrigada por toda a apoio, por toda a dedicação, por sempre, sempre,
sempre estar juntinho com a gente, que era agradecer a todas as professoras, todos os profissionais,
todos os voluntários, as mulheres tão especiais que sem elas nada disso teria acontecido,
a passos não existiria sem mulheres tão inquiubas, tão guerreiras, tão fortes que batalham todos os dias
para trazer educação de qualidade, um futuro melhor e um dos princípios da passos,
educação que transforma e ajuda a transformar. Então eu estou aqui para quebecem imensamente
e para benizar todas as mulheres da passos mágicos, um beijo, feliz de a das mulheres!

Oi gente, tudo bem meu nome é Eduardo Acosta, tenho 17 anos em treino a passo mágicos em 2021.
Em 2022 eu te oportunidades me inscrever no projeto VENCER.
No projeto vencer a gente tem aulas da ONISA de química e biologia durante o ano
e também fazemos aulas no me salva que é um site.
O lá a gente tem um cronograma a seguir, que no começo eu não consime adaptar muito bem
porque eu não tinha uma rotina muito bem estabelecida, por conta que eu não tinha.
Mas com a Natal a gente chegou em um cronograma que eu consegui me adaptar e foi melhorando
durante o ano inteiro.
Bom, os professores da passo mágicos sempre ajudam a gente muito, eles sempre soluçam
todas as nossas dúvidas e eles sempre perguntam se a gente tá bem e outras coisas.
E com a ajuda da passo aos mágicos e com o meu esforço eu consegui passar na prova
e consegui uma bolsa.
E eu agradeço muito a passas mágicos hoje em dia.
Eu vou seguir.

Oi, meu nome é Maria Letiz, setenta e sete anos e vim aqui contar um pouquinho sobre meu ano de 2022
e como foi uma processo de chegar na aprovação na Universidade?
Um ano de 2022 foi um ano bem decisivo para mim, porque como todo mundo sabe,
dos teram anos nesse nome é de não é um ano fácil, mas junto com a paz, eu consegui realizar minha sonha
no início do ano, alguns alunos do teram anos nesse nome é de foram apresentados
a um programa, o vencer, que oferecia uma plataforma de estudos
e a gente também tinha cada 15 dias, live, escontia, Michel e com a Natalha, que foi a nossa área interior de estudos
e também é um apoio psicológico com as psicólogas da passos
eu estudei muito durante o ano e com todo o suporte, apoio da passos
eu senti mais confiante e comecei a acreditar que conseguia cansar nos objetivos
então agora tenho um prazer de dizer que eu passei nesse PM
e vou cursar a comunicação publicidade lá
eu tenho muito a agradecer a todas as pessoas que participaram da minha trajetória
e também é tudo que contribuem para que passos continuem ajudando crianças e jovens a realizar essas sonhas
O nosso projeto passa os mágicos no município de Buguaçu.
Nós temos 980 crianças estudando conosco e o nosso objetivo é transformar vidas através da educação.
Maria Buarda, quantos anos você tem?
Como a minha mãe entra um projeto?
Eu estava no hospital.
Aí minha boteça, eu vou colocar um projeto.
Aí eu disse assim, mas eu quero ir logo.
A minha boteça morou um pouco.
Come se achar o dia todo.
Aí minha boteça, assim, não, você vai fazer a prova a mim.
Você com feliz de entrar no projeto?
Você queria muito.
Que tanto você queria.
Muito, muito, muito.
Se pudesse, eu ficava o dia todo.
Oi, meu nome é Estela, tenho 16 anos.
E eu faço parte do projeto para os mágicos há 2 anos ou mais ou menos.
E o projeto mudou totalmente a minha forma.
Não só de estudar, mas a minha forma de viver.
Antes do projeto, meus planos eram muito pequenininhos.
Eu tinha sonhos muito medíocles para tudo o que eu podia viver.
O projeto me mostrou que eu possa viver muito mais, o que eu sempre pensei.
Abriu portas para mim para que eu pudesse tornar os meus sonhos reais.
Sou psicóloga na Unidas dos Mágicos há pouco mais de 4 anos.
Eu desenvolvo um trabalho tanto individual quanto em grupo com os alunos.
Ao longo desses anos, nós começamos a perceber a importância do suporte psicológico.
Que são emocional travar las crianças, né?
Ou ocupando espaço que poderia se ocupar pela aprendisagem.
Durante esse período, nós também percebemos a necessidade de um suporte para a família.
Traifico da sua família, se enfrenta, dinâmica, familiar, pouco de funcionar.
Foi aí que nós tivemos a ideia de trazer uma psicóloga para desenvolver um trabalho com a família.
Então, o tanto trabalho da psicologia, dos alunos, quanto para as famílias, ele é fundamental para o desenvolvimento emocional das nossas crianças.
Gustavo, quando são os que você tem?
Tenho 10 anos.
De que você sabe quanto tempo você está no projeto?
Eu acho que 2 anos.
2 anos?
O que que hoje significa o projeto para você?
Sim, significa que você pode aprender mais ainda, mais rápido, se estura na escola e no projeto.
Então, você pode aprender mais ainda.
Passos mágicos começou transformando a primeira vida da minha filha, em termos de estudo inicialmente.
Mas veio uma segunda parte no passos mágicos que foi o culto no nosso grupo assistido e que simplesmente transformou a minha família.
Nasceram as marmitinhas que é a MSFIT, quando eu comecei, a minha expectativa era se eu vende esse 20 marmitas na semana, eu me considero um sucesso.
E aí, para a minha surpresa, eu distribui algumas marmitas e vende 5 na primeira semana, na segunda semana eu tive um salto para 53.
Então, hoje, eu posso falar que eu já estou me estabilizando em praticamente 100 marmitas por semana.
Ficamos sentados, lado de cada um deles e perguntar para eles, você está precisando hoje, que eu posso fazer por você.

Qual a importância de um sonho?
Em que mundo estaríamos se ninguém tivesse sanhado?
Sonhos são a energia que move o mundo.
Sem eles, os grandes projetos seriam apenas pijas de papel.
A gente não ia saber que a Lua não é feita de queijo e que as estrelas não são vagalões.
Sem eles, nós nunca teríamos o átomo.
Você consegue lembrar qual foi o seu primeiro sonho?
O que você queria ser?
Onde queria chegar?
Esse sonho parecia impossível.
Para mim sim.
Deixa que eu te contar a minha história.
Tudo começou com o sonho.
Sempre sonhei-me da realidade da minha família.
Via meus pais exaus hoje um trabalho que usava tão pouco
e meus colegas não têm das oportunidades certas para aproveitar as qualidades.
Eu sentia que havia mais para ser vivido, mais lugares para visitar, mais histórias para conhecer, mais sonhos para realizar.
Hoje, eu sei que, na verdade, o que eu queria era mais perspectiva.
O perspectiva? Você sabia que naquele tempo eu nem entendia essa palavra?
Mas queria mudança.
Eu precisava de mudança.
Só não sabia por onde começar.
Então, olhei minha volta.
Vi uma umge que dizia transformar através da educação.
Eu achei meio estranho.
Era diferente de tudo que eu conhecia.
Sei lá. Eu resolvi arriscar.
Encontrei lá um lugar cheio de pessoas que sonhavam, assim como eu.
Entendi que mudança começa através da educação.
Viu novas possibilidades.
Aulas de vertiga que me dava a vontade de estudar.
Professores que eram muito mais que professores.
Era pessoas com quem eu poderia contar.
Que me mostraram que o estudo é o melhor caminho.
Collegas viajando para lugares que eu só vi nos filmes.
Conheci museus e as histórias que eles contavam.
Ah, e tinha aquelas tias que me chamavam
quando a minha coração estava apertada.
Não é como se eu não tivesse as problemas.
Eu só sabia que tinha um montão de gente
que sempre estaria lá por mim.
E tem também os meus amigos mais velhos entrando na faculdade.
O caiu testa do dano e engenharia lá longe.
E as mim fazendo um curso que eu nem sei falar,
mas sei que o sonho dela.
Era produção multimídia?
Acho que é algo assim.
Tudo isso foi possível pela passas mágicos.
Para mim, o verdadeiro significado de passas mágicos
são os passos que eu e meus amigos
estamos dando para reescrever a nossa história.
Assim eu aprendi que não adiantava sonhar sozinha.
Soinhar sozinha mudaria minha realidade.
Mas soinhar em conjunto nos faria mudar o mundo.
Tinha nada de antável longe,
se não fossemos juntos.
A passas me ensino a isso.
Meu sonho já não era mais transformar a minha realidade.
Era transformar o mundo.
Eu sou a Julia.
E essa é a minha história.
Esses são os meus sonhos.
Mas eu sei que como eu existem centenas de julhas
esperando para terem suas vidas transformadas.
Passa parte dessa mudança.
Alimente esse sonho.
Assim, vamos transformar o Brasil através da educação.
"""

    stop_words = set(stopwords.words('portuguese'))

    stop_words.add("então")
    stop_words.add("oi")
    stop_words.add("toda")
    stop_words.add("yuri")
    stop_words.add("né")
    stop_words.add("mim")
    stop_words.add("nome")

    # Removendo as stopwords do texto
    text = ' '.join([word for word in text.split()
                    if word.lower() not in stop_words])

    # Generate word cloud
    wordcloud = WordCloud(width=1800, height=400,
                          background_color='white', stopwords=stop_words).generate(text)

    # Prepare figure to display word cloud
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")

    # Use Streamlit's pyplot function to display the matplotlib plot
    st.pyplot(fig)

def classificarsentimento(resultado1):
    if resultado1["compound"]>=0.8: 
        st.markdown("# 🥰")
    elif resultado1["compound"]<0.8 and resultado1["compound"]>=0.5: 
        st.markdown("# 😁")
    elif resultado1["compound"]<0.5 and resultado1["compound"]>=0.2: 
        st.markdown("# 😊")
    elif resultado1["compound"]<0.2 and resultado1["compound"]>=-0.2: 
        st.markdown("# 😐")
    elif resultado1["compound"]<-0.2 and resultado1["compound"]>=-0.5: 
        st.markdown("# 😟")
    elif resultado1["compound"]<-0.5 and resultado1["compound"]>=-0.8: 
        st.markdown("# 😠")
    else:
        st.markdown("# 😡")

def create_waffle_chart():

    st.title("O impacto da Passos Mágicos na sociedade de Embu-Guaçu")
    st.write("""Embu-Guaçu, situado na Região Metropolitana de São Paulo, é um município que abriga uma população de aproximadamente 66.970 pessoas. No entanto, mesmo diante desse número considerável, questões relacionadas à educação infantil merecem atenção especial.
Conforme indicado por um estudo conduzido pelo QEDU, nos anos de 2003, 2004 e 2005, um total de 3.617 crianças nasceram em Embu-Guaçu durante esse período. Este dado, por si só, ressalta a importância de estruturas educacionais adequadas para atender a demanda de jovens em idade escolar.
No entanto, o estudo também revelou uma preocupação alarmante: 265 dessas crianças, o que representa aproximadamente 7,3% do total, estavam fora da escola. Esse número reflete uma lacuna significativa no acesso à educação básica, um direito fundamental para o pleno desenvolvimento das crianças e para a construção de uma sociedade mais justa e igualitária.
Essa constatação destaca a necessidade urgente de políticas educacionais que visem garantir o acesso universal e equitativo à educação em Embu-Guaçu. Investimentos em infraestrutura escolar, programas de inclusão e sensibilização da comunidade são algumas das medidas que podem ser adotadas para enfrentar esse desafio e assegurar que todas as crianças tenham a oportunidade de frequentar a escola e alcançar seu potencial máximo.""")

    col1, col2 = st.columns(2)
    with col1:
        # Inicializando o grafo
        G = nx.Graph()

        # Parâmetros da rede
        num_main_nodes = 11
        num_neighbor_nodes = 5
        total_nodes = 669

        # Adicionar os nós principais e seus vizinhos
        for main_node in range(num_main_nodes):
            G.add_node(main_node)
            for i in range(num_neighbor_nodes):
                neighbor_node = num_main_nodes + main_node * num_neighbor_nodes + i
                G.add_node(neighbor_node)
                G.add_edge(main_node, neighbor_node)

                # Conectar cada vizinho a um nó adicional
                extra_node = num_main_nodes + num_main_nodes * \
                    num_neighbor_nodes + main_node * num_neighbor_nodes + i
                G.add_node(extra_node)
                G.add_edge(neighbor_node, extra_node)

        # Adicionar nós adicionais sem conexões para totalizar 669 nós
        for extra_node in range(G.number_of_nodes(), total_nodes):
            G.add_node(extra_node)

        # Posicionar os nós
        pos = nx.spring_layout(G, seed=42)

        # Dados para nós
        node_x = []
        node_y = []
        node_color = []
        for node in G.nodes():
            x, y = pos[node]
            node_x.append(x)
            node_y.append(y)
            # Cor baseada no número de conexões
            node_color.append(len(G[node]))

        # Dados para arestas
        edge_x = []
        edge_y = []
        for edge in G.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])

        # Criar a figura
        fig = go.Figure()

        # Adicionar arestas
        fig.add_trace(go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=0.5, color='#888'),
            hoverinfo='none',
            mode='lines'))

        # Adicionar nós
        fig.add_trace(go.Scatter(
            x=node_x, y=node_y,
            mode='markers',
            hoverinfo='text',
            marker=dict(
                showscale=True,
                colorscale='Viridis',
                reversescale=True,
                color=node_color,
                size=10,
                colorbar=dict(
                    thickness=15,
                    title='Pessoas afetadas pela educação',
                    xanchor='left',
                    titleside='right'
                ),
                line_width=2)))

        # Atualizar layout da figura
        fig.update_layout(
            title='Network Graph with 669 Nodes',
            showlegend=False,
            hovermode='closest',
            margin=dict(b=0, l=0, r=0, t=0),
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))

        # Streamlit: renderizando a figura
        st.plotly_chart(fig)
    with col2:
        st.markdown("""Em 2023, a Passos Mágicos contava com um corpo discente de 1.100 alunos, cujo impacto se estendia muito além dos limites da instituição. Cada um desses alunos desempenhava um papel crucial não apenas em seu próprio desenvolvimento educacional, mas também na influência que exerciam sobre outras pessoas em seu círculo social.

Considerando que cada aluno afeta diretamente outras 5 pessoas, entre familiares, amigos e conhecidos, e cada uma dessas pessoas, por sua vez, influencia mais uma pessoa, o alcance do impacto da Passos Mágicos se torna surpreendentemente amplo.

Dessa forma, com os 1.100 alunos matriculados na Passos Mágicos em 2023, o impacto direto se estende a 5.500 pessoas. Essas são pessoas cujas vidas são de alguma forma tocadas pela educação e pelo ambiente proporcionados pela instituição.

Além disso, considerando o efeito multiplicador dessas influências, atingimos um número adicional de 5.500 pessoas indiretamente afetadas. Este é um reflexo do poder transformador da educação e do papel fundamental que a Passos Mágicos desempenha na comunidade.

Assim, em um cálculo modesto, podemos afirmar que um total de 12.100 pessoas são afetadas pela educação proporcionada pela Passos Mágicos em 2023. Esse número não apenas sublinha a importância da instituição na vida dos alunos, mas também evidencia seu impacto positivo na sociedade em geral.""")

    st.title("O impacto da Passos Mágicos: Daqui a 10 anos")
    st.write("A cada ano, a instituição Passos Mágicos aceita em média 150 alunos a mais do que no ano anterior. Com essa progressão constante, em um período de 10 anos, estima-se que a Passos Mágicos terá uma matrícula total de aproximadamente 2.600 alunos ativos. Esse número não apenas reflete o crescimento contínuo e sustentável da instituição, mas também demonstra seu papel vital na comunidade educacional de Embu-Guaçu. Considerando os dados demográficos atuais, essa estimativa de 2.600 alunos representa aproximadamente 71% da população infantil de Embu-Guaçu. Esse é um indicativo poderoso do impacto significativo que a Passos Mágicos tem na vida educacional das crianças e jovens da região. Essa expansão não apenas amplia o acesso à educação de qualidade, mas também contribui para o desenvolvimento e o progresso da comunidade como um todo.")
    st.image("assets/crescimento.jpeg")
    col1, col2 = st.columns(2)
    with col1:
        st.write("""\n\nCom base na projeção de crescimento para os próximos 10 anos, estima-se um aumento de 1.500 alunos na instituição educacional Passos Mágicos, totalizando um corpo discente de 2.600 estudantes. Essa expansão não apenas influenciará o ambiente escolar, mas também terá um impacto significativo na comunidade ao redor.

Considerando que cada aluno da Passos Mágicos afete diretamente outras 5 pessoas, entre familiares, amigos e conhecidos, e cada uma dessas pessoas influencie mais uma pessoa, o efeito multiplicador se torna evidente. Esse ciclo de influência cria uma rede interconectada de pessoas afetadas pela educação proporcionada pela instituição.

Portanto, com os 2.600 alunos matriculados na Passos Mágicos, temos um impacto direto em 13.000 pessoas. Além disso, considerando o efeito multiplicador, atingimos um número adicional de 13.000 pessoas indiretamente afetadas. Em um cálculo modesto, podemos afirmar que há um total de 28.600 pessoas que experimentam os efeitos da educação fornecida pela Passos Mágicos. Esse número não apenas reflete a importância da instituição na vida dos alunos, mas também destaca seu papel vital na formação e desenvolvimento da comunidade em geral.""")
    with col2:
        # Inicializando o grafo
        G = nx.Graph()

        # Parâmetros da rede
        num_main_nodes = 26
        num_neighbor_nodes = 5
        total_nodes = 669

        # Adicionar os nós principais e seus vizinhos
        for main_node in range(num_main_nodes):
            G.add_node(main_node)
            for i in range(num_neighbor_nodes):
                neighbor_node = num_main_nodes + main_node * num_neighbor_nodes + i
                G.add_node(neighbor_node)
                G.add_edge(main_node, neighbor_node)

                # Conectar cada vizinho a um nó adicional
                extra_node = num_main_nodes + num_main_nodes * \
                    num_neighbor_nodes + main_node * num_neighbor_nodes + i
                G.add_node(extra_node)
                G.add_edge(neighbor_node, extra_node)

        # Adicionar nós adicionais sem conexões para totalizar 669 nós
        for extra_node in range(G.number_of_nodes(), total_nodes):
            G.add_node(extra_node)

        # Posicionar os nós
        pos = nx.spring_layout(G, seed=42)

        # Dados para nós
        node_x = []
        node_y = []
        node_color = []
        for node in G.nodes():
            x, y = pos[node]
            node_x.append(x)
            node_y.append(y)
            # Cor baseada no número de conexões
            node_color.append(len(G[node]))

        # Dados para arestas
        edge_x = []
        edge_y = []
        for edge in G.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])

        # Criar a figura
        fig = go.Figure()

        # Adicionar arestas
        fig.add_trace(go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=0.5, color='#888'),
            hoverinfo='none',
            mode='lines'))

        # Adicionar nós
        fig.add_trace(go.Scatter(
            x=node_x, y=node_y,
            mode='markers',
            hoverinfo='text',
            marker=dict(
                showscale=True,
                colorscale='Viridis',
                reversescale=True,
                color=node_color,
                size=10,
                colorbar=dict(
                    thickness=15,
                    title='Pessoas afetadas pela educação',
                    xanchor='left',
                    titleside='right'
                ),
                line_width=2)))

        # Atualizar layout da figura
        fig.update_layout(
            title='Network Graph with 669 Nodes',
            showlegend=False,
            hovermode='closest',
            margin=dict(b=0, l=0, r=0, t=0),
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))

        # Streamlit: renderizando a figura
        st.plotly_chart(fig)

    st.markdown("## Seleção para participação do projeto Passos Mágicos")
    st.markdown(
        "Em 2023 a Passos Mágicos organizou uma prova onde era necessario a realização da inscrição como pré-requisito.")
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("### 1) inscrições válidas X alunos que compareceram")
            # Waffle Chart data
            data = {'Não fizeram a prova': (
                1121 - 817)/15, 'Fizeram a prova': 817/15}
            # Create a figure using plt.figure and Waffle class
            fig = plt.figure(
                FigureClass=Waffle,
                rows=5,
                values=data,
                colors=["#ced4d9", "#983D3D"],
                labels=["{0} - {1}".format(k, int(v*15))
                        for k, v in data.items()],
                legend={'loc': 'upper left', 'bbox_to_anchor': (1, 1)}
            )
            # Display the figure using Streamlit
            st.pyplot(fig)

        with col2:
            st.markdown(
                "### 2) inscrições válidas X alunos que se matricularam (1ª sem)")
            # Waffle Chart data
            data = {'Não foram contemplados': (
                817 - 298)/15, 'Foram contemplados': 298/15}
            # Create a figure using plt.figure and Waffle class
            fig = plt.figure(
                FigureClass=Waffle,
                rows=5,
                values=data,
                colors=["#ced4d9", "#182cdb"],
                labels=["{0} - {1}".format(k, int(v*15))
                        for k, v in data.items()],
                legend={'loc': 'upper left', 'bbox_to_anchor': (1, 1)}
            )
            # Display the figure using Streamlit
            st.pyplot(fig)

            with col3:
                st.markdown(
                    "### 3) inscrições válidas X alunos que se matricularam")
                # Waffle Chart data
                data = {'Não foram contemplados': (
                    817 - 298 - 254)/15, 'Foram contemplados': 298/15, 'Foram posteriormente': 254/15}
                # Create a figure using plt.figure and Waffle class
                fig = plt.figure(
                    FigureClass=Waffle,
                    rows=5,
                    values=data,
                    colors=["#ced4d9", "#182cdb", "#db8a18"],
                    labels=["{0} - {1}".format(k, int(v*15))
                            for k, v in data.items()],
                    legend={'loc': 'upper left', 'bbox_to_anchor': (1, 1)},
                )
                # Display the figure using Streamlit
                st.pyplot(fig)

    st.write("""* Observou-se que, dentre os 1.121 alunos inscritos para a prova, uma proporção significativa de 304 alunos, equivalente a 27% do total, optaram por não realizar o exame.

* No contexto das matrículas referentes ao 1º Semestre, a instituição Passos Mágicos disponibilizou um total de 298 bolsas de estudo. Esse número representa uma parte significativa da comunidade estudantil, contemplando precisamente 36% dos alunos matriculados nesse período.

* Durante uma segunda rodada de seleção, um adicional de 254 alunos, representando 31% do total, foi agraciado com novas bolsas de estudo. Com essa inclusão, o número total de alunos contemplados ao longo do ano de 2023 ascendeu para 552, o que equivale a uma proporção significativa de 67% dos estudantes beneficiados com esse importante suporte financeiro. Esse aumento no número de bolsistas reflete o compromisso contínuo da instituição em ampliar o acesso à educação e em fornecer apoio adicional aos alunos que demonstram mérito e necessidade financeira.""")

def main():
    create_sidebar()
    choice = option_menu(None, ["O Projeto", "Impacto Alunos", "Qualidade de Ensino", "Sentimentos", "Referências", "Quem somos?"],
                         icons=['house', 'bar-chart-fill',
                                'graph-up', 'graph-up'],
                         menu_icon="cast", default_index=0, orientation="horizontal")

    if choice == "O Projeto":
        create_main_content()
    elif choice == "Qualidade de Ensino":
        st.title("Qualidade de Ensino")
        st.markdown("""Na Passos Mágicos, os estudantes são classificados com base em suas notas, representadas por diferentes pedras preciosas:
                    \n•	Quartzo (2,4 a 5,5)
                    \n• Ágata (5,5 a 6,8)
                    \n•	Ametista (6,8 a 8,2)
                    \n•	Topázio (8,2 a 9,2)
                    \nDurante uma análise realizada entre os anos de 2020 e 2022, notamos um aumento de quase 3% no número de alunos premiados com a pedra Topázio, indicativa das notas mais altas, e uma diminuição de 3% na atribuição da pedra Quartzo, que corresponde às notas mais baixas. Esse padrão sugere um progresso contínuo dos alunos ao longo dos anos, refletindo um esforço e dedicação crescentes em suas jornadas educacionais na instituição. Esse avanço é um sinal positivo do compromisso tanto dos alunos quanto dos educadores da Passos Mágicos com a excelência acadêmica e o desenvolvimento pessoal de cada estudante.""")
        df = pd.read_csv("inputs/PEDE_PASSOS_DATASET_FIAP.csv", sep=";", usecols=["NOME", "IDADE_ALUNO_2020", "ANOS_PM_2020", "PONTO_VIRADA_2020", "PEDRA_2020", "PEDRA_2021", "REC_EQUIPE_1_2021", "REC_EQUIPE_2_2021", "REC_EQUIPE_3_2021", "REC_EQUIPE_4_2021", "PONTO_VIRADA_2021",
                         "NIVEL_IDEAL_2021", "DEFASAGEM_2021", "FASE_2022", "ANO_INGRESSO_2022", "PEDRA_2022", "NOTA_PORT_2022", "NOTA_MAT_2022", "NOTA_ING_2022", "REC_AVA_1_2022", "REC_AVA_2_2022", "REC_AVA_3_2022", "REC_AVA_4_2022", "PONTO_VIRADA_2022", "NIVEL_IDEAL_2022"])
        col1, col2, col3 = st.columns(3)
        with col1:
            df_filtrado = df[df['PEDRA_2020'] != 'D9891/2A']
            df_filtrado = df_filtrado[df_filtrado['PEDRA_2021'] != '#NULO!']
            # PEDRA_2020
            # Contando os valores da coluna PEDRA_2020
            contagem_PEDRA_2020 = df_filtrado['PEDRA_2020'].value_counts()

            # Obtendo os rótulos (categorias) e os valores da contagem
            labels = contagem_PEDRA_2020.index.tolist()
            valores = contagem_PEDRA_2020.values.tolist()

            # Criando o gráfico de pizza
            # Por exemplo, vermelho, azul e verde
            cores = ['#9966cc', '#a6cad6', '#ac7175', '#776048']
            # Criando o gráfico de pizza
            fig = go.Figure(
                data=[go.Pie(labels=labels, values=valores, marker=dict(colors=cores))])

            # Personalizando o layout do gráfico
            fig.update_layout(
                title='Distribuição dos dados da coluna PEDRA_2020')

            # Exibindo o gráfico
            st.plotly_chart(fig)
        with col2:
            # PEDRA_2021
            # Contando os valores da coluna PEDRA_2020
            contagem_PEDRA_2020 = df_filtrado['PEDRA_2021'].value_counts()

            # Obtendo os rótulos (categorias) e os valores da contagem
            labels = contagem_PEDRA_2020.index.tolist()
            valores = contagem_PEDRA_2020.values.tolist()

            # Criando o gráfico de pizza
            # Por exemplo, vermelho, azul e verde
            cores = ['#9966cc', '#a6cad6', '#ac7175', '#776048']
            # Criando o gráfico de pizza
            fig = go.Figure(
                data=[go.Pie(labels=labels, values=valores, marker=dict(colors=cores))])

            # Personalizando o layout do gráfico
            fig.update_layout(
                title='Distribuição dos dados da coluna PEDRA_2021')

            # Exibindo o gráfico
            st.plotly_chart(fig)
        with col3:
            # PEDRA_2022
            # Contando os valores da coluna PEDRA_2020
            contagem_PEDRA_2020 = df_filtrado['PEDRA_2022'].value_counts()

            # Obtendo os rótulos (categorias) e os valores da contagem
            labels = contagem_PEDRA_2020.index.tolist()
            valores = contagem_PEDRA_2020.values.tolist()

            # Criando o gráfico de pizza
            # Por exemplo, vermelho, azul e verde
            cores = ['#9966cc', '#a6cad6', '#ac7175', '#776048']
            # Criando o gráfico de pizza
            fig = go.Figure(
                data=[go.Pie(labels=labels, values=valores, marker=dict(colors=cores))])

            # Personalizando o layout do gráfico
            fig.update_layout(
                title='Distribuição dos dados da coluna PEDRA_2022')
            st.plotly_chart(fig)
        st.markdown("Pode-se observar a presença constante da pedra ametista como uma marca representativa desde o ano de 2020, sugerindo que a maioria dos estudantes tem demonstrado um desempenho intermediário. Essa consistência na predominância da ametista ao longo do tempo pode indicar uma estabilidade no padrão de desempenho dos alunos, refletindo uma distribuição equilibrada entre resultados positivos e desafios a serem superados. É importante analisar mais a fundo esse cenário para compreender os fatores que contribuem para essa tendência e buscar estratégias que possam promover um avanço para níveis de desempenho mais elevados.")
        # GRÁFICO DE LINHAS
        # Contando os valores únicos para cada pedra em 2020
        contagem_pedra_2020 = df['PEDRA_2020'].value_counts()
        contagem_pedra_2021 = df['PEDRA_2021'].value_counts()
        contagem_pedra_2022 = df['PEDRA_2022'].value_counts()

        # Criando DataFrames para 2021 e 2022
        df_2021 = pd.DataFrame.from_dict({'PEDRA_2021': contagem_pedra_2021})
        df_2022 = pd.DataFrame.from_dict({'PEDRA_2022': contagem_pedra_2022})

        # Combinando os DataFrames
        df_combined = pd.concat(
            [contagem_pedra_2020, df_2021, df_2022], axis=1)
        df_combined = df_combined.drop(index=['D9891/2A', '#NULO!'])
        # Transpondo o DataFrame para ter os anos como índices e as pedras como colunas
        df_transposed = df_combined.transpose()

        # Criando o gráfico de linhas
        fig = go.Figure()

        # Adicionando as linhas para cada ano em cada pedra
        # Por exemplo, azul, vermelho, verde e laranja
        cores = ['#9966cc', '#a6cad6', '#ac7175', '#776048']

        # Criando uma figura vazia
        fig = go.Figure()

        # Adicionando uma linha para cada coluna do DataFrame transposto
        for i, coluna in enumerate(df_transposed.columns):
            fig.add_trace(go.Scatter(
                x=df_transposed.index,
                y=df_transposed[coluna],
                mode='lines',
                name=coluna,
                # Garante que as cores sejam recicladas se houver mais linhas do que cores definidas
                line=dict(color=cores[i % len(cores)])
            ))

        # Personalizando o layout do gráfico
        fig.update_layout(
            title='Contagem de valores únicos para cada pedra em cada ano',
            xaxis_title='Ano',
            yaxis_title='Contagem'
        )
        st.plotly_chart(fig)

        st.markdown("""Anualmente, a instituição realiza provas com o intuito de avaliar o nível de conhecimento de cada aluno. A partir do desempenho obtido, são tomadas decisões quanto à progressão dos estudantes em seu percurso educacional. Com base nesses resultados, determina-se se o aluno permanecerá na mesma fase, retornará à fase anterior ou será promovido para a próxima etapa do seu aprendizado.

Durante o período entre 2021 e 2022, observa-se um cenário em que a maioria dos alunos mantém-se na mesma fase em que se encontravam, evidenciando uma estabilidade no progresso acadêmico. Contudo, é notável que muitos estudantes avançam para o próximo nível, indicando um crescimento significativo em seus conhecimentos e habilidades.

Além disso, alguns alunos têm a oportunidade privilegiada de receber bolsas de estudo em outras instituições de ensino. Essa oportunidade não apenas reconhece o mérito e o esforço desses alunos, mas também os capacita a explorar novas oportunidades educacionais e a aprimorar ainda mais seus horizontes acadêmicos.

Esse cenário ressalta a importância das avaliações regulares no processo educacional, bem como o compromisso da instituição em promover o avanço e o sucesso acadêmico de seus alunos, proporcionando-lhes oportunidades de crescimento e desenvolvimento contínuo.""")
        col1, col2 = st.columns(2)
        with col1:
            count_rec_equipe_1_2021 = df['REC_EQUIPE_1_2021'].value_counts()
            count_rec_equipe_2_2021 = df['REC_EQUIPE_2_2021'].value_counts()
            count_rec_equipe_3_2021 = df['REC_EQUIPE_3_2021'].value_counts()
            count_rec_equipe_4_2021 = df['REC_EQUIPE_4_2021'].value_counts()
            dfs = [count_rec_equipe_1_2021, count_rec_equipe_2_2021,
                   count_rec_equipe_3_2021, count_rec_equipe_4_2021]
            df_combined = pd.concat(dfs, axis=1)
            # GRAFICO 2021
            # Renomeação das colunas para facilitar a identificação
            df_combined.columns = ['Equipe_1',
                                   'Equipe_2', 'Equipe_3', 'Equipe_4']

            # Criação do gráfico de barras empilhadas com Plotly
            fig = go.Figure()

            for index, row in df_combined.iterrows():
                fig.add_trace(go.Bar(
                    x=df_combined.columns,
                    y=row,
                    name=index,
                    hoverinfo='y'
                ))

            fig.update_layout(
                title='Contagem de valores únicos por Equipe e Categoria',
                xaxis_title='Equipe',
                yaxis_title='Contagem',
                barmode='stack'
            )
            st.plotly_chart(fig)
        with col2:
            count_rec_equipe_1_2022 = df['REC_AVA_1_2022'].value_counts()
            count_rec_equipe_2_2022 = df['REC_AVA_2_2022'].value_counts()
            count_rec_equipe_3_2022 = df['REC_AVA_3_2022'].value_counts()
            count_rec_equipe_4_2022 = df['REC_AVA_4_2022'].value_counts()
            # Combinação dos DataFrames
            # grafico 2
            dfs = [count_rec_equipe_1_2022, count_rec_equipe_2_2022,
                   count_rec_equipe_3_2022, count_rec_equipe_4_2022]
            df_combined = pd.concat(dfs, axis=1)

            # Renomeação das colunas para facilitar a identificação
            df_combined.columns = ['Equipe_1',
                                   'Equipe_2', 'Equipe_3', 'Equipe_4']

            # Criação do gráfico de barras empilhadas com Plotly
            fig = go.Figure()

            for index, row in df_combined.iterrows():
                fig.add_trace(go.Bar(
                    x=df_combined.columns,
                    y=row,
                    name=index,
                    hoverinfo='y'
                ))

            fig.update_layout(
                title='Contagem de valores únicos por Equipe e Categoria',
                xaxis_title='Equipe',
                yaxis_title='Contagem',
                barmode='stack'
            )
            st.plotly_chart(fig)

    elif choice == "Sentimentos":
        st.title("Análise de Sentimentos")
        st.markdown("""A análise de sentimentos de dados é uma técnica usada para entender as emoções expressas em textos, comentários, avaliações ou qualquer tipo de dados textuais. O objetivo é determinar se o sentimento expresso é positivo, negativo ou neutro. Por exemplo, em uma análise de sentimentos de comentários de clientes sobre um produto, a análise identificaria se os comentários são geralmente positivos (por exemplo, "amei este produto"), negativos (por exemplo, "não gostei da qualidade") ou neutros (por exemplo, "ok, nada de especial"). Isso é feito usando algoritmos de processamento de linguagem natural que examinam as palavras e frases no texto para inferir o sentimento geral. A análise de sentimentos de dados é amplamente utilizada em áreas como análise de mídia social, avaliação de produtos, feedback do cliente e pesquisa de opinião.""")
        st.markdown("**O que fizemos?**")
        st.markdown("Selecionamos três depoimentos disponíveis no site da Passos Mágicos e utilizamos nossa ferramenta de Análise de Sentimentos para mapear o sentimento e a satisfação dos estudantes. Abaixo, apresentamos os resultados:")
        s = SentimentIntensityAnalyzer()
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("assets/menina1.jpeg")
            texto1 = """Raphaela Soares: Olá, sou Raphaela Soares da Silva, estudante de Enfermagem na Universidade Santo Amaro, com 19 anos de idade. Agradeço à Passos Mágicos pela oportunidade de participar de um nano curso na plataforma da FIAP sobre "Libras". Aprender a Língua Brasileira de Sinais é crucial, sendo uma habilidade valiosa para minha formação na área da saúde."""

            st.markdown(texto1)
            resultado1 = s.polarity_scores(texto1)
            st.markdown(
                "**Resultado da análise utilizando nossa ferramenta de análise de sentimentos:**")
            # resultado1_dict = json.loads(resultado1)
            st.json(resultado1)
            classificarsentimento(resultado1)

        with col2:
            st.image("assets/menina2.jpeg")
            text2 = """Bruna Ramos: Me chamo Bruna Ramos da Silva, e estudo na Passos Mágicos desde 2017. Conheci a Associação através de um tio e desde então minha vida vem sendo transformada pela família Passos Mágicos. Em 2019, ganhei uma bolsa para estudar na União (atualmente Rede Decisão), marcando uma virada na minha vida. A qualidade de ensino era notavelmente superior. Em 2020, fui informada sobre vagas para o ensino médio técnico no Einstein, não hesitei e aceitei imediatamente. A Passos Mágicos tem sido meu apoio desde que sonhei em seguir Medicina e agora, sou estudante da UNISA no curso que sempre sonhei."""
            st.markdown(text2)
            resultado2 = s.polarity_scores(text2)
            st.markdown(
                "**Resultado da análise utilizando nossa ferramenta de análise de sentimentos:**")
            st.json(resultado2)
            classificarsentimento(resultado2)

        with col3:
            st.image("assets/menina3.jpeg")
            text3 = """Maria Letícias: Na ONG, aprendi a acreditar em mim mesma e que sonhos são possíveis. Com a Passos, tive oportunidades para evoluir e aprender mais a cada dia. No terceiro ano do ensino médio, os alunos prestes a fazer vestibular foram apresentados ao programa VemSer da Passos, que oferece apoio aos estudos. Mesmo em um ano desafiador, tivemos suporte em cada etapa, proporcionando mais tranquilidade. Com muito esforço, passei noites estudando, mas valeu a pena. Realizei meu sonho, fui aprovada na ESPM e agora sou bolsista em Comunicação e Publicidade. Com a Passos, iniciei um novo ciclo, e é fundamental ter ao meu lado pessoas que se importam com meu futuro."""
            st.markdown(text3)
            resultado3 = s.polarity_scores(text3)
            st.markdown(
                "**Resultado da análise utilizando nossa ferramenta de análise de sentimentos:**")
            st.json(resultado3)
            classificarsentimento(resultado3)

        # Função para realizar a análise de sentimentos
        def analisar_sentimento(texto):
            sia = SentimentIntensityAnalyzer()
            sentiment = sia.polarity_scores(texto)
            return sentiment

        # Área para inserir o texto
        texto_input = st.text_area(
            "Insira um depoimento ou texto para ser analisado:")

        # Botão para realizar a análise quando o texto for inserido
        if st.button("Analisar Sentimentos"):
            if texto_input:
                # Realizar a análise de sentimentos
                sentiment = analisar_sentimento(texto_input)

                # Exibir o resultado da análise
                st.write("### Resultado da Análise de Sentimentos:")
                st.write(f"Sentimento: {sentiment}")
                classificarsentimento(sentiment)
            else:
                st.warning("Por favor, insira um texto para análise.")

    elif choice == "Impacto Alunos":
        create_waffle_chart()
    elif choice == "Referências":
        st.title("Referências")
        st.subheader("Neste espaço incluímos todos os locais que nos ajudaram a entender melhor o que é a Organização Passos Mágicos, bem como entender o cenário atual de Embu-Guaçu e dados estatisticos sobre estudos no Brasil.")
        st.markdown(
            "* Passos Mágicos: https://passosmagicos.org.br/\n\n"
            "* Nóticia - Indicador de Permanência Escolar: https://conteudos.qedu.org.br/academia/indicador-permanencia-escolar/,\n\n "
            "* QEDU - Dados de Embu-Guaçu: https://qedu.org.br/municipio/3515103-embu-guacu,\n\n "
            "* Video - Conheça a Passos Mágicos: https://www.youtube.com/watch?v=36ZfZQa68og,\n\n "
            "* Video - Qual a importancia de um sonho?: https://www.youtube.com/watch?v=hT_jOmLzpH4,\n\n "
            "* GOV.BR - MEC e Inep divulgam resultados do Censo Escolar 2023: https://www.gov.br/inep/pt-br/assuntos/noticias/censo-escolar/mec-e-inep-divulgam-resultados-do-censo-escolar-2023,\n\n "
            "* GOV.BR - Lição de casa é um dos fatores de maior impacto no rendimento dos alunos: https://www.gov.br/inep/pt-br/assuntos/noticias/saeb/licao-de-casa-e-um-dos-fatores-de-maior-impacto-no-rendimento-dos-aluno,\n\n"
            "* Estadão Expresso - Análise: o dilema da lição de casa: https://expresso.estadao.com.br/educacao/analise-o-dilema-da-licao-de-casa/#:~:text=O%20pr%C3%B3prio%20Pisa%20passou%20a%20pesquisar%20a%20influ%C3%AAncia,s%C3%A3o%20muito%20mais%20determinantes%20para%20um%20bom%20resultado,\n\n"
            "* Depoimentos Passos Mágicos: https://passosmagicos.org.br/uma-historia-de-sucesso/,\n\n"
            "* Depoimentos Facebook: https://www.facebook.com/passosmagicos/videos,\n\n"
            "* Noticia Linkedin - Vitórias que Transformam: https://www.linkedin.com/pulse/vit%C3%B3rias-que-transformam-passosmagicos-fz1le/?originalSubdomain=pt.\n\n"
            "* Git Hub - Classificação das Palavras: https://github.com/rafjaa/LeIA"
        )
        st.image("assets/referencias.jpeg")
    elif choice == "Quem somos?":
        st.title("Quem somos?")
        st.subheader("Essa atividade foi realizada pelos integrantes Alexandre Augusto de Oliveira Queiroz, Bruna Borges de Moura Scarpe e Hadassa Caroline Juricic, que fazem parte do curso de pós graduação em Análise de dados da FIAP.\n\n")
        st.markdown("Nos foi proposto nesse desafio do Tech Challenge 5 realizar um trabalho apresentando uma melhoria para a Passos Mágicos. Neste trabalho nos jogamos de cabeça e coração, onde fizemos diversas análises exploratórias com os dados fornecidos pela Organização, bem como pesquisas na internet. Ao final criamos dados que demonstram o quão importante a Passos Mágicos é importante na vida dos moradores e crianças de Embu-Guaçu e porque o projeto deve ser realizado a níveis mundiais! Através de nossos insights geramos algumas percepções e insights que podem ajudar a investidores ou pessoas que querem apoiar a Passos Mágicos em tomadas de decisões.")
        st.image("assets/obrigadof.png")


if __name__ == "__main__":
    main()
