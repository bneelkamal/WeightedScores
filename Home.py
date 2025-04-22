import random
import streamlit as st
import pandas as pd
import requests
import utils

st.set_page_config(page_title="Weighted Score Calculator App", layout="centered")

# Title & welcome message
st.title("Welcome to the Weighted Score Calculator App!")
st.write("Use the navigation side bar to Calculate your scores.")




# Example usage:
# if __name__ == "__main__":
    # print(get_random_motivational_quote())

# Random motivational quote
# quotes = [
# "Believe in yourself—every challenge is an opportunity to grow!",
# "Keep pushing forward. Your hard work will pay off!",
# "Success is a journey, not a destination. Stay determined!",
# "You are capable of amazing things. Keep learning and keep shining!"
# ]
# random_quote = random.choice(quotes)
# st.markdown(f"### Quote of the Day:\n> {random_quote}")


st.markdown(f"### Quote of the Day:\n> {utils.get_random_motivational_quote()}")