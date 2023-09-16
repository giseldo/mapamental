import streamlit as st
import graphviz

st.write(""" Uma raposa passou embaixo de um pé carregado com lindas uvas. Ficou com muita vontade de comer aquelas uvas. Deu muitos saltos, tentou subir na parreira, mas não conseguiu. Depois de muito tentar foi-se embora, dizendo:
— Eu nem estou ligando para as uvas. Elas estão verdes, mesmo...""")

txt_protagonista = st.text_input(label="Quem é o protagonista?")

txt_modo = st.text_input(label="Quem é o narrador?")

graph = graphviz.Digraph()
graph.edge('Sobre a estrutura', "Quem é o protagonista?")
graph.edge('Sobre a estrutura', "Quem é o narrador?")
graph.edge('Quem é o protagonista?', txt_protagonista)
graph.edge('Quem é o narrador?', txt_modo)
st.graphviz_chart(graph)


btn_corrigir = st.button("Corrigir automaticamente")


if btn_corrigir:
    st.write("Gabarito")
    graph = graphviz.Digraph()
    graph.edge('Sobre a estrutura', "Quem é o protagonista?")
    graph.edge('Sobre a estrutura', "Quem é o narrador?")
    graph.edge('Quem é o protagonista?', "a raposa")
    graph.edge('Quem é o narrador?', "onisciente")
    st.graphviz_chart(graph)
    
    
    st.write("Nota 10.")



