PC Game Deals

A beginner Python project that reads PC game pricing information from a JSON file, identifies games currently on sale, calculates discounts, finds the cheapest game and allows users to search and filter the available games through a Streamlit interface.

Project overview

The project uses a local deals.json file as its data source. Python loads the records, processes the prices, and determines whether a game is on sale by comparing its sale price with its normal price.

The Streamlit interface presents the results in a simple web application.
Features
- Loads game records from deals.json.
- Counts the total number of games.
- Identifies games on sale by comparing normal and sale prices.
- Calculates the percentage discount for sale games.
- Determines the cheapest game using its current price.
- Searches game titles without being case-sensitive.
- Filters the list to show only games on sale.
- Displays game information in a three-column layout.

Technologies

- Python for data loading, processing and calculations.
- JSON for storing the game data.
- Streamlit for the interactive user interface.
- Pathlib for locating the JSON file relative to the Python script.

Project structure
PC-GAMES-DEAL/
├── deals.json
├── streamlit_app.py
└── README_PC_GAME_DEALS.md


Setup
Open a terminal in the project folder.

Create a virtual environment:
python3 -m venv .venv
Activate it on macOS:
source .venv/bin/activate
Install Streamlit:
python -m pip install streamlit
Run the Streamlit application
From the project folder, with the virtual environment activated, run:
python -m streamlit run streamlit_app.py
Streamlit will provide a local address in the terminal. Open that address in your browser.


How sale status is determined
The JSON data contains a normal price and a sale price for each game. A game is treated as being on sale when:
sale_price < normal_price
If both prices are equal, the game is not treated as being on sale. The application uses the sale price for a discounted game and the normal price otherwise when comparing current prices.

The price conversion function is designed to accept numeric values as well as strings such as "R150", because JSON price values may be represented in different formats.

Design decision: Streamlit
I am still developing my skills as a programmer and learning the technologies used in software development. During my research for this project, I realised that I could achieve the main interactive results I wanted using Python and Streamlit. I therefore chose to focus on a Python library I could learn and apply within the time available, rather than beginning several new technologies from scratch.

This was a practical learning decision, not a conclusion that HTML, CSS or JavaScript are unnecessary. I read about these technologies and became more interested in learning how they work together. They are part of my future learning goals.

Learning outcomes
This project gave me practical experience with:
- Reading structured data from a JSON file.
- Working with dictionaries, lists, loops and conditional statements.
- Converting values into numeric data types before performing calculations.
- Writing reusable functions.
- Searching and filtering records.
- Using a virtual environment to manage Python packages.
- Building an interactive interface with Streamlit.
- Debugging issues involving file paths, package environments, dictionary keys and inconsistent data types.

Future improvements
- Connect to a live game-deals API instead of relying only on a local JSON file.
- Add sorting by price and discount percentage.
- Include links to game stores.
- Improve input validation and handling of incomplete records.
- Build a separate front end using HTML, CSS and JavaScript to deepen my understanding of web development.
- Add automated tests for the pricing and discount functions.

Author's note
This is a learning project. I have aimed to keep the implementation understandable and to make deliberate choices that I can explain. I intend to continue improving it as I develop my Python, data-processing and web-development skills.