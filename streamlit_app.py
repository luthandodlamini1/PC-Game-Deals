
# Loading the libraries
import streamlit as st
import json
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="PC Game Deals",
    page_icon="🎮",
    layout="wide"
)

# Loading game data from JSON
def load_game():
    file_path = Path(__file__).with_name("deals.json")

    with open(file_path, "r", encoding="utf-8") as file:
        games = json.load(file)

    return games


# Price and sale functions
def get_price(price):
    if isinstance(price, str):
        price = price.replace("R", "").strip()

    return float(price)

def is_on_sale(game):
    normal_price = get_price(game["normalPrice"])
    sale_price = get_price(game["salePrice"])

    if sale_price < normal_price:
        return True
    else:
        return False


def calculate_discount(game):
    normal_price = get_price(game["normalPrice"])
    sale_price = get_price(game["salePrice"])

    if not is_on_sale(game):
        return 0

    discount = ((normal_price - sale_price) / normal_price) * 100
    return round(discount)


def get_current_price(game):
    if is_on_sale(game):
        return get_price(game["salePrice"])

    return get_price(game["normalPrice"])


# Loading data and calculating summary values
games = load_game()
total_games = len(games)

on_sale_games = []

for game in games:
    if is_on_sale(game):
        on_sale_games.append(game)


# Finding the cheapest game
cheapest_game = None

if len(games) > 0:
    cheapest_game = games[0]

    for game in games:
        if get_current_price(game) < get_current_price(cheapest_game):
            cheapest_game = game


# Page content
st.title("🎮 PC Game Deals")
st.write("Find your next game at a better price.")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Games", total_games)

with col2:
    st.metric("Games on Sale", len(on_sale_games))

with col3:
    if cheapest_game is not None:
        cheapest_price = get_current_price(cheapest_game)

        st.metric(
            "Cheapest Game",
            cheapest_game["title"],
            f"R{cheapest_price}"
        )
    else:
        st.metric("Cheapest Game", "No games available")


# Search and sale filter
st.divider()
st.subheader("Available Games")

search_word = st.text_input("Search for a game")
only_sale = st.checkbox("Show only games on sale")

displayed_games = []

for game in games:
    matches_search = search_word.lower() in game["title"].lower()
    matches_sale = True

    if only_sale:
        matches_sale = is_on_sale(game)

    if matches_search and matches_sale:
        displayed_games.append(game)


# Displaying games in three columns
game_columns = st.columns(3)

for index, game in enumerate(displayed_games):
    game_column = game_columns[index % 3]

    with game_column:
        with st.container(border=True):
            st.subheader(game["title"])
            st.write("Normal price:", game["normalPrice"])

            if is_on_sale(game):
                st.success("ON SALE")
                st.write("Sale price:", game["salePrice"])
                st.write(
                    "Discount:",
                    str(calculate_discount(game)) + "%"
                )

if len(displayed_games) == 0:
    st.info("No games match your search.")
