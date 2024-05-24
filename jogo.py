import streamlit as st

# Título
st.title("Jogo Maneiro da Cat")

# Introdução
st.write("Bem-vindo ao meu jogo de RPG! Você é o cara desta história.")

# Escolha do personagem
personagem = st.radio("Escolha seu personagem:",
                      ("JoJo", "Matheus", "Gecaberalda"))

# Descrição dos crias
if personagem == "JoJo":
    st.write("Você escolheu ser o doutor programador!")
elif personagem == "Matheus":
    st.write("Você escolheu ser o enfermeiro dos dados!")
else:
    st.write("Você escolheu ser a mãe da fgv!")

# Pt1
st.write("Você acorda na sala de programção vazia...")

# Escolha do caminho pt1
caminho = st.selectbox("O que você fará a seguir?",
                       ("7 andar", "Sapinho", "Permanecer"))

# Descrição do caminho escolhido
if caminho == "7 andar":
    st.write("Você decide seguir para o 7 andar socializar.")
elif caminho == "Sapinho":
    st.write("Você decide seguir para o sapinho almoçar.")
else:
    st.write("Você decide permanecer na sala e programar.")

# Final do jogo
st.write("E assim começa sua jornada épica...")


