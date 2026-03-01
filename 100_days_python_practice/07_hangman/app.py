import streamlit as st
import random
from hangman_words import word_list
from hangman_art import stages, logo

# 1. Configuración básica de la página
st.set_page_config(page_title="El Ahorcado", page_icon="🔤")

# 2. Inicializar la "memoria" del juego (Session State)
if 'game_over' not in st.session_state:
    st.session_state.lives = 6
    st.session_state.chosen_word = random.choice(word_list)
    st.session_state.correct_letters = []
    st.session_state.guessed_letters = [] # Guardamos todas para que no repita
    st.session_state.game_over = False

# Función para reiniciar todo cuando ganemos/perdamos
def reset_game():
    st.session_state.lives = 6
    st.session_state.chosen_word = random.choice(word_list)
    st.session_state.correct_letters = []
    st.session_state.guessed_letters = []
    st.session_state.game_over = False

# 3. Mostrar el Logo
st.title("🎯 Juego del Ahorcado")
st.markdown("¡Adivina la palabra antes de que se acaben tus vidas!")
st.divider() # Esto dibuja una línea horizontal elegante para separar el título del juego

# 4. Mostrar el progreso de la palabra
display = ""
for letter in st.session_state.chosen_word:
    if letter in st.session_state.correct_letters:
        display += letter + " "
    else:
        display += "_ "

st.markdown(f"### Palabra a adivinar: {display}")

# 5. Mostrar el dibujo (usamos st.text para que respete el arte ASCII) y las vidas
st.text(stages[st.session_state.lives])
st.write(f"**Vidas restantes:** {st.session_state.lives}/6")

# 6. Lógica de ingreso de letras (solo si el juego sigue activo)
if not st.session_state.game_over:
    # Usamos un formulario para que la página no parpadee al escribir cada letra
    with st.form(key='guess_form', clear_on_submit=True):
        guess = st.text_input("Adivina una letra:", max_chars=1).lower()
        submit_button = st.form_submit_button(label='Enviar letra')

    if submit_button and guess:
        if not guess.isalpha():
            st.warning("Por favor, ingresa solo letras.")
        elif guess in st.session_state.guessed_letters:
            st.warning(f"Ya intentaste con la letra '{guess}'. ¡Prueba otra!")
        else:
            st.session_state.guessed_letters.append(guess)
            
            if guess in st.session_state.chosen_word:
                st.session_state.correct_letters.append(guess)
                st.success("¡Bien hecho!")
            else:
                st.session_state.lives -= 1
                st.error(f"La letra '{guess}' no está. Pierdes una vida.")
            
            # Recargamos la página para actualizar el dibujo y los guiones al instante
            st.rerun() 

# 7. Comprobar si ganó o perdió
# Perder
if st.session_state.lives == 0 and not st.session_state.game_over:
    st.session_state.game_over = True
    st.error(f"¡PERDISTE! La palabra era: {st.session_state.chosen_word}")
    st.rerun()

# Ganar
if "_" not in display.replace(" ", "") and not st.session_state.game_over:
    st.session_state.game_over = True
    st.success("¡GANASTE! 🎉")
    st.balloons() # ¡Un pequeño efecto visual de Streamlit!
    st.rerun()

# 8. Botón para jugar de nuevo al terminar
if st.session_state.game_over:
    st.button("Jugar de nuevo", on_click=reset_game)