# Mystery Number Game

A small web game built with Python and Streamlit: the app picks a number between 1 and 20, and you keep guessing until you find it, with "too high" and "too low" hints along the way.

I built it to learn how Streamlit handles state. Every button click re-runs the whole script, so the secret number, the attempt counter and the game-over flag all live in `st.session_state`, which keeps them across reruns. The code is commented line by line as a learning reference.

## How to play

1. Type a number from 1 to 20 and click **Submit Guess**.
2. The game tells you if your guess is too low or too high.
3. Keep guessing until you get it. The counter shows how many tries you've used.
4. When you find the number, click **Play Again** to start a new round with a new number.

Tip: start in the middle (10). Each hint cuts the remaining range roughly in half, so you should never need more than 5 guesses.

## Features

- Guess input limited to 1–20
- Hints after each guess and an attempt counter
- A **Play Again** button that resets the game without reloading the page

## Run it

```bash
pip install -r requirements.txt
streamlit run mysterynumbergame.py
```

## Tech

Python · Streamlit

---

Built by **Rafia Imran** · [GitHub profile](https://github.com/rafiasimran)
