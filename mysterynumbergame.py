# We import 'streamlit' as 'st'. This library handles all the web visuals (buttons, text, inputs).
import streamlit as st
import random

# The highest number the game can pick. Change it here and the whole game follows.
MAX_NUMBER = 20


def new_game():
    """Pick a new secret number and reset the counters in session state."""
    st.session_state.secret_number = random.randint(1, MAX_NUMBER)
    st.session_state.attempts = 0
    st.session_state.game_over = False


# --- 1. TITLE AND SETUP ---

# 'st.title' puts a large header on the webpage.
st.title("🕵️ Mystery Number Game")
st.write(f"I am thinking of a number between 1 and {MAX_NUMBER}. Can you guess it?")

# --- 2. SESSION STATE (THE BRAIN) ---
# In a web app, the code re-runs every time you click a button.
# We need a place to store variables (like the secret number) so they aren't lost/reset on every click.
# This place is called 'st.session_state'.

# We check: "Do we already have a secret number stored?"
# If NOT, this is the first run, so we start a new game.
if "secret_number" not in st.session_state:
    new_game()

# --- 3. USER INPUT ---

# 'st.number_input' creates a box where the user can type numbers.
# We set min and max values so the user can't guess 100 or -5.
guess = st.number_input("Take a guess:", min_value=1, max_value=MAX_NUMBER, step=1)

# --- 4. THE LOGIC BUTTON ---

# 'st.button' creates a clickable button.
# The code inside this 'if' block ONLY runs when the user clicks the button.
if st.button("Submit Guess"):

    # First, check if the game is already over.
    if st.session_state.game_over:
        st.error("The game is over! Click 'Play Again' below.")
    else:
        # If game is active, increase attempts in memory by 1.
        st.session_state.attempts += 1

        # LOGIC: Compare the 'guess' from the input box to the 'secret_number' in memory.
        if guess < st.session_state.secret_number:
            # st.warning shows a yellow message box.
            st.warning(f"Too low! You guessed {guess}.")

        elif guess > st.session_state.secret_number:
            st.warning(f"Too high! You guessed {guess}.")

        else:
            # st.success shows a green message box.
            st.success(f"CORRECT! The number was {st.session_state.secret_number}.")
            st.info(f"It took you {st.session_state.attempts} attempts.")
            # Mark the game as over in memory.
            st.session_state.game_over = True

# --- 5. RESET BUTTON ---

# This button lets the user restart without refreshing the whole browser page.
if st.button("Play Again"):
    new_game()
    # 'st.rerun' forces the app to reload immediately to show the reset state.
    st.rerun()
