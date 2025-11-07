import streamlit as st
import random

# --- Page Setup ---
st.set_page_config(page_title="🎯 Guess the Number", page_icon="🎯", layout="centered")

st.title("🎯 Guess the Number")
st.write("I'm thinking of a number between **1 and 20**. You have **5 chances** to guess it!")

# --- Initialize Session State ---
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 20)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "message" not in st.session_state:
    st.session_state.message = ""
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# --- User Input ---
guess = st.number_input("Enter your guess:", min_value=1, max_value=20, step=1)

# --- Submit Guess ---
if st.button("Submit Guess"):
    if not st.session_state.game_over:
        st.session_state.attempts += 1

        if guess < st.session_state.secret_number:
            st.session_state.message = f"🔽 Too low! ({5 - st.session_state.attempts} chances left)"
        elif guess > st.session_state.secret_number:
            st.session_state.message = f"🔼 Too high! ({5 - st.session_state.attempts} chances left)"
        else:
            st.session_state.message = (
                f"🎉 Correct! You guessed it in {st.session_state.attempts} tries."
            )
            st.session_state.game_over = True

        # Game over if player uses all 5 chances
        if st.session_state.attempts >= 5 and not st.session_state.game_over:
            st.session_state.message = (
                f"💀 Game Over! The correct number was **{st.session_state.secret_number}**."
            )
            st.session_state.game_over = True
    else:
        st.info("Game over! Click 'New Game' to try again.")

# --- Display Result ---
st.write(st.session_state.message)

# --- Restart Button ---
if st.button("New Game"):
    st.session_state.secret_number = random.randint(1, 20)
    st.session_state.attempts = 0
    st.session_state.message = ""
    st.session_state.game_over = False
    st.success("🎯 New game started! Try to guess the new number between 1 and 20.")
