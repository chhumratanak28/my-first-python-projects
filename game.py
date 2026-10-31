import streamlit as st
import random
def play_rps():
    st.title("🪨📄✂️ Rock, Paper, Scissors!")
    st.write("Can you beat the computer AI?")
    choices = ["🪨 Rock", "📄 Paper", "✂️ Scissors"]
    user_choice = st.radio("Choose your weapon:", choices, horizontal=True)
    if st.button("Play Match! ⚔️"):
        computer_choice = random.choice (choices)

        st.subheader(f"You choose: {user_choice}")
        st.subheader(f"Computer choose: {computer_choice}")
        if user_choice == computer_choice:
            st.warning("It's a tie! 🤝")
        elif (
                (user_choice == "🪨 Rock" and computer_choice == "✂️ Scissors")or
                (user_choice == "📄 Paper" and computer_choice == "🪨 Rock")or
                (user_choice == "✂️ Scissors" and computer_choice == "📄 Paper")
            ):
            st.success("You Win! 🏆")
            st.balloons()
        else:
            st.error("Computer Win! 🤖 Try again!")

        def play_number_guess():
            st.title("🎯 Secret Number Guessing Game")
            st.write("I am thinking of a number between **1 and 100**, ")

            if "secret_number" not in st.session_state:
                st.session_state.secret_number = random.randint(1,100)
                st.session_state.attempts = 0

            guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

            if st.button("Submit Guess 🔍"):
                st.session_state.attempts += 1


            if guess < st.session_state.secret_number:
                st.warning("⬆️ Too low! Try a higher number.")
            elif guess > st.session_state.secret_number:
                st.warning("⬇️ Too high! Try a lower number.")
            else:
                st.success(f"🎉 Correct! The number was {st.session_state.secret_number}! You got it in {st.session_state.attempts} tries!")
                st.balloons()


            if st.button("New Secret Number 🔄"):
                st.session_state.secret_number = random.randint(1,100)
                st.session_state.attempts = 0
                st.info("New number generated! Start guessing!")