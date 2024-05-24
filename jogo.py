import streamlit as st

# Título do jogo
st.title("Meu Jogo de RPG")

# Introdução
st.write("Bem-vindo ao mundo do RPG! Você é o herói desta história.")

# Escolha do personagem
personagem = st.radio("Escolha seu personagem:",
                      ("Guerreiro", "Mago", "Arqueiro"))

# Introdução ao personagem escolhido
if personagem == "Guerreiro":
    st.write("Você escolheu ser um guerreiro corajoso!")
elif personagem == "Mago":
    st.write("Você escolheu ser um poderoso mago!")
else:
    st.write("Você escolheu ser um ágil arqueiro!")

# Começo da aventura
st.write("Você acorda em uma floresta misteriosa...")

# Escolha do caminho
caminho = st.selectbox("Qual caminho você seguirá?",
                       ("Floresta Profunda", "Montanhas Geladas", "Caverna Escura"))

# Descrição do caminho escolhido
if caminho == "Floresta Profunda":
    st.write("Você decide entrar na densa Floresta Profunda.")
elif caminho == "Montanhas Geladas":
    st.write("Você decide escalar as perigosas Montanhas Geladas.")
else:
    st.write("Você decide explorar a assustadora Caverna Escura.")

# Final do jogo
st.write("E assim começa sua jornada épica...")


