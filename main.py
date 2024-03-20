import streamlit as st
import plotly.express as px
from wordcloud import WordCloud
from pywaffle import Waffle
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

# Function to create sidebar
st.set_page_config(layout="wide", page_title="My Streamlit App")


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
    st.title("Introdução")
    st.write("Texto da introdução.")

    # Sample text for the word cloud
    text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

    # Generate word cloud
    wordcloud = WordCloud(width=800, height=200,
                          background_color='white').generate(text)

    # Prepare figure to display word cloud
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")

    # Use Streamlit's pyplot function to display the matplotlib plot
    st.pyplot(fig)


def create_waffle_chart():

    st.header("Inscrições válidas X Alunos que compareceram")
    # Waffle Chart data
    data = {'Não fizeram a prova': (
        1121 - 817)/16, 'Fizeram a prova': 817/16}
    # Create a figure using plt.figure and Waffle class
    fig = plt.figure(
        FigureClass=Waffle,
        rows=5,
        values=data,
        colors=["#ced4d9", "#983D3D"],
        # title={'label': 'My Waffle Chart', 'loc': 'center'},
        labels=["{0} - {1}".format(k, int(v*16))
                for k, v in data.items()],
        legend={'loc': 'upper left', 'bbox_to_anchor': (1, 1)}
    )
    # Display the figure using Streamlit
    st.pyplot(fig)

    st.header("Inscrições válidas X Alunos que se matricularam(1ª sem)")
    # Waffle Chart data
    data = {'Não foram contemplados': (
        1121 - 298)/15, 'Foram contemplados': 298/15}
    # Create a figure using plt.figure and Waffle class
    fig = plt.figure(
        FigureClass=Waffle,
        rows=5,
        values=data,
        colors=["#ced4d9", "#182cdb"],
        # title={'label': 'My Waffle Chart', 'loc': 'center'},
        labels=["{0} - {1}".format(k, int(v*15))
                for k, v in data.items()],
        legend={'loc': 'upper left', 'bbox_to_anchor': (1, 1)}
    )
    # Display the figure using Streamlit
    st.pyplot(fig)

    st.header("Inscrições válidas X Alunos que se matricularam")
    # Waffle Chart data
    data = {'Não foram contemplados': (
        1121 - 298 - 254)/15, 'Foram contemplados': 298/15, 'Foram posteriormente': 254/15}
    # Create a figure using plt.figure and Waffle class
    fig = plt.figure(
        FigureClass=Waffle,
        rows=5,
        values=data,
        colors=["#ced4d9", "#182cdb", "#db8a18"],
        # title={'label': 'My Waffle Chart', 'loc': 'center'},
        labels=["{0} - {1}".format(k, int(v*15)) for k, v in data.items()],
        legend={'loc': 'upper left', 'bbox_to_anchor': (1, 1)},
    )
    # Display the figure using Streamlit
    plt.tight_layout()
    st.pyplot(fig)


def main():
    create_sidebar()
    choice = option_menu(None, ["Home", "Data Analysis", "Data Visualization", "outra opção"],
                         icons=['house', 'bar-chart-fill',
                                'graph-up', 'graph-up'],
                         menu_icon="cast", default_index=0, orientation="horizontal")

    if choice == "Home":
        create_main_content()
    elif choice == "Data Analysis":
        create_waffle_chart()


if __name__ == "__main__":
    main()
