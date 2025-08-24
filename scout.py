# scouting_app.py

import streamlit as st
import pandas as pd

# 1. DADOS: A lista completa de parâmetros de avaliação
# Os dados estão estruturados como uma lista de dicionários para serem facilmente convertidos num DataFrame.
data = [
    {'Categoria': 'Técnica', 'Atributo/Parâmetro': 'Tinha pés rápidos?'},
    {'Categoria': 'Técnica', 'Atributo/Parâmetro': 'Tinha uma boa variedade de passe?'},
    {'Categoria': 'Técnica', 'Atributo/Parâmetro': 'Tinha boa capacidade de cabeceamento?'},
    {'Categoria': 'Técnica', 'Atributo/Parâmetro': 'Demonstrou capacidade para rematar de longa distância?'},
    {'Categoria': 'Técnica', 'Atributo/Parâmetro': 'Marcar golos de perto?'},
    {'Categoria': 'Técnica', 'Atributo/Parâmetro': 'Enfrentar jogadores em situações de 1 contra 1?'},
    {'Categoria': 'Técnica', 'Atributo/Parâmetro': 'Disfarçar/enganar?'},
    {'Categoria': 'Técnica', 'Atributo/Parâmetro': 'Cruzar para a área?'},
    {'Categoria': 'Técnica', 'Atributo/Parâmetro': 'Marcar golos de lances de bola parada?'},
    {'Categoria': 'Técnica', 'Atributo/Parâmetro': 'Marcar grandes penalidades?'},
    {'Categoria': 'Técnica', 'Atributo/Parâmetro': 'Fazer assistências?'},
    {'Categoria': 'Técnica', 'Atributo/Parâmetro': 'Vencer duelos 1 contra 1?'},
    {'Categoria': 'Técnica', 'Atributo/Parâmetro': 'Vencer duelos aéreos?'},
    {'Categoria': 'Técnica', 'Atributo/Parâmetro': 'Criar situações de 1 contra 1 com o guarda-redes adversário?'},
    {'Categoria': 'Técnica', 'Atributo/Parâmetro': 'Segurar a bola, envolver colegas de equipa e criar oportunidades para eles?'},
    {'Categoria': 'Técnica', 'Atributo/Parâmetro': 'Mostrar movimento inteligente com e sem bola?'},
    {'Categoria': 'Técnica', 'Atributo/Parâmetro': 'Produzir uma variedade de finalizações?'},
    {'Categoria': 'Técnica', 'Atributo/Parâmetro': 'Ir por dentro, por fora ou através dos defesas?'},
    {'Categoria': 'Técnica', 'Atributo/Parâmetro': 'Segurar a bola sob pressão?'},
    {'Categoria': 'Técnica', 'Atributo/Parâmetro': 'Receber sob pressão?'},
    {'Categoria': 'Técnica', 'Atributo/Parâmetro': 'Receber a bola no pé ou nas costas da defesa?'},
    {'Categoria': 'Técnica', 'Atributo/Parâmetro': 'Combinar com os colegas de equipa?'},
    {'Categoria': 'Técnica', 'Atributo/Parâmetro': 'Passar para colegas de equipa em melhores posições?'},
    {'Categoria': 'Técnica', 'Atributo/Parâmetro': 'Marcar a oposição em cantos e lances de bola parada?'},
    {'Categoria': 'Técnica', 'Atributo/Parâmetro': 'Fixar e rodar sobre os defesas?'},
    {'Categoria': 'Tática', 'Atributo/Parâmetro': 'Ocupou mais do que um defesa?'},
    {'Categoria': 'Tática', 'Atributo/Parâmetro': 'Retirou os defesas de posição?'},
    {'Categoria': 'Tática', 'Atributo/Parâmetro': 'Temporizou as corridas e manteve-se em jogo?'},
    {'Categoria': 'Tática', 'Atributo/Parâmetro': 'Manipulou a organização da equipa adversária?'},
    {'Categoria': 'Tática', 'Atributo/Parâmetro': 'Usou a velocidade para fazer corridas inteligentes nas costas da defesa adversária?'},
    {'Categoria': 'Tática', 'Atributo/Parâmetro': 'Fez corridas a partir de trás?'},
    {'Categoria': 'Tática', 'Atributo/Parâmetro': 'Fez corridas de apoio?'},
    {'Categoria': 'Tática', 'Atributo/Parâmetro': 'Pressionou os defesas adversários?'},
    {'Categoria': 'Tática', 'Atributo/Parâmetro': 'Interrompeu a construção de jogo do adversário?'},
    {'Categoria': 'Tática', 'Atributo/Parâmetro': 'Forçou os defesas a jogar uma bola longa ou a fazer um passe para trás?'},
    {'Categoria': 'Tática', 'Atributo/Parâmetro': 'Forçou o jogo numa direção?'},
    {'Categoria': 'Tática', 'Atributo/Parâmetro': 'Fez contra-pressão (counter press)?'},
    {'Categoria': 'Tática', 'Atributo/Parâmetro': 'Explorou pequenos espaços na área de penálti?'},
    {'Categoria': 'Tática', 'Atributo/Parâmetro': 'Fez corridas nas costas da defesa?'},
    {'Categoria': 'Tática', 'Atributo/Parâmetro': 'Baixou no terreno para receber a bola?'},
    {'Categoria': 'Tática', 'Atributo/Parâmetro': 'Ligou o jogo e criou espaço?'},
    {'Categoria': 'Tática', 'Atributo/Parâmetro': 'Ofereceu-se aos colegas de equipa?'},
    {'Categoria': 'Tática', 'Atributo/Parâmetro': 'Deu largura ao jogo (stretch play)?'},
    {'Categoria': 'Tática', 'Atributo/Parâmetro': 'Ofereceu uma ameaça de contra-ataque?'},
    {'Categoria': 'Tática', 'Atributo/Parâmetro': 'Demonstrou consciência da estratégia da equipa?'},
    {'Categoria': 'Tática', 'Atributo/Parâmetro': 'Demonstrou consciência das táticas do adversário?'},
    {'Categoria': 'Tática', 'Atributo/Parâmetro': 'Demonstrou consciência de como operar em bloco baixo, bloco médio ou pressão alta?'},
    {'Categoria': 'Física', 'Atributo/Parâmetro': 'Demonstrou velocidade em longas distâncias?'},
    {'Categoria': 'Física', 'Atributo/Parâmetro': 'Demonstrou aceleração a partir de uma posição estática?'},
    {'Categoria': 'Física', 'Atributo/Parâmetro': 'Demonstrou altos níveis de energia?'},
    {'Categoria': 'Física', 'Atributo/Parâmetro': 'Demonstrou resistência (stamina)?'},
    {'Categoria': 'Física', 'Atributo/Parâmetro': 'Demonstrou força para segurar os adversários e disputar a bola?'},
    {'Categoria': 'Física', 'Atributo/Parâmetro': 'Demonstrou capacidade no jogo aéreo?'},
    {'Categoria': 'Física', 'Atributo/Parâmetro': 'Demonstrou capacidade de salto e de cabeceamento?'},
    {'Categoria': 'Psicológica', 'Atributo/Parâmetro': 'Mostrou um alto nível de confiança e talvez um toque de arrogância?'},
    {'Categoria': 'Psicológica', 'Atributo/Parâmetro': 'Mostrou uma mentalidade determinada?'},
    {'Categoria': 'Psicológica', 'Atributo/Parâmetro': 'Mostrou vontade de trabalhar para a equipa?'},
    {'Categoria': 'Psicológica', 'Atributo/Parâmetro': 'Mostrou uma atitude altruísta?'},
    {'Categoria': 'Psicológica', 'Atributo/Parâmetro': 'Mostrou desejo de estar envolvido no terço final ou na construção de jogo a partir do meio-campo?'},
    {'Categoria': 'Psicológica', 'Atributo/Parâmetro': 'Mostrou antecipação na leitura do movimento dos que o rodeiam ou dos erros dos adversários?'},
    {'Categoria': 'Psicológica', 'Atributo/Parâmetro': 'Mostrou consideração pelo movimento antes da bola chegar?'},
    {'Categoria': 'Social', 'Atributo/Parâmetro': 'Comunicou bem?'},
    {'Categoria': 'Social', 'Atributo/Parâmetro': 'Organizou o movimento ofensivo?'},
    {'Categoria': 'Social', 'Atributo/Parâmetro': 'Estabeleceu uma boa relação com os árbitros?'}
]

df = pd.DataFrame(data)

# 2. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(layout="wide", page_title="Scouting App")

# 3. INTERFACE DA APLICAÇÃO
st.title("⚽ Ficha de Avaliação de Jogador")
st.write("Preencha as informações abaixo para avaliar a performance de um jogador.")

# Cria duas colunas para informações gerais
col1, col2 = st.columns(2)
with col1:
    player_name = st.text_input("Nome do Jogador Avaliado:")
with col2:
    scout_name = st.text_input("Nome do Observador (Scout):")

st.markdown("---") # Linha divisória

# Opções de avaliação
options = ["-", "✔", "X"]

# Guarda as escolhas do utilizador num dicionário
evaluations = {}

# Agrupa os atributos por categoria e exibe-os
categories = df['Categoria'].unique()
for category in categories:
    st.subheader(f"Categoria: {category}")
    
    # Filtra o dataframe para a categoria atual
    category_df = df[df['Categoria'] == category]
    
    # Itera sobre cada atributo da categoria para criar um seletor
    for index, row in category_df.iterrows():
        attribute = row['Atributo/Parâmetro']
        # Usamos o `st.radio` para ser mais visual, com as opções na horizontal
        evaluations[attribute] = st.radio(
            label=attribute,
            options=options,
            key=f"{category}_{attribute}", # Chave única para cada widget
            horizontal=True,
            label_visibility="collapsed" # Esconde o label duplicado do radio
        )

# Botão para submeter e ver o relatório final
st.markdown("---")
if st.button("Gerar Relatório de Avaliação", type="primary"):
    if not player_name or not scout_name:
        st.warning("Por favor, preencha o nome do jogador e do observador.")
    else:
        st.header(f"Relatório Final para: {player_name}")
        st.subheader(f"Observador: {scout_name}")

        # Cria uma lista com os resultados
        results_list = []
        for index, row in df.iterrows():
            attribute = row['Atributo/Parâmetro']
            result = {
                "Categoria": row['Categoria'],
                "Atributo/Parâmetro": attribute,
                "Avaliação": evaluations[attribute]
            }
            results_list.append(result)

        # Converte a lista de resultados num DataFrame do Pandas
        results_df = pd.DataFrame(results_list)
        
        # Filtra para mostrar apenas os itens que foram avaliados (diferentes de "-")
        evaluated_df = results_df[results_df['Avaliação'] != '-']

        st.dataframe(evaluated_df, use_container_width=True)

        # Mostra um resumo rápido
        st.subheader("Resumo Rápido")
        value_counts = evaluated_df['Avaliação'].value_counts()
        
        col1_res, col2_res = st.columns(2)
        with col1_res:
            st.metric(label="Pontos Fortes (✔)", value=value_counts.get("✔", 0))
        with col2_res:
            st.metric(label="Pontos a Melhorar (X)", value=value_counts.get("X", 0))
