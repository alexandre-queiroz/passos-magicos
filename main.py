
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


def create_waffle_chart():

    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("### Inscrições válidas X Alunos que compareceram")
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
                "### Inscrições válidas X Alunos que se matricularam (1ª sem)")
            # Waffle Chart data
            data = {'Não foram contemplados': (
                1121 - 298)/15, 'Foram contemplados': 298/15}
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
                    "### Inscrições válidas X Alunos que se matricularam")
                # Waffle Chart data
                data = {'Não foram contemplados': (
                    1121 - 298 - 254)/15, 'Foram contemplados': 298/15, 'Foram posteriormente': 254/15}
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
        st.markdown("### Alunos da passos que afetam outras pessoas")
        st.plotly_chart(fig)


def main():
    create_sidebar()
    choice = option_menu(None, ["Home", "Inscrições", "Data Visualization", "outra opção", "Data Analysis", "outra opção"],
                         icons=['house', 'bar-chart-fill',
                                'graph-up', 'graph-up'],
                         menu_icon="cast", default_index=0, orientation="horizontal")

    if choice == "Home":
        create_main_content()
    elif choice == "Inscrições":
        create_waffle_chart()


if __name__ == "__main__":
    main()
