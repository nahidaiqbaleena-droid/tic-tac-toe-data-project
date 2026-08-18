# Tic-Tac-Toe Simulation and Gameplay Analysis

## Abstract

This project uses Python to simulate and analyze 1,000 complete Tic-Tac-Toe games. Two automated players, X and O, alternate turns and randomly select valid, unoccupied positions until a player wins or the board is full. Every game is stored as one row in a pandas DataFrame, including the outcome, winner, number of moves, winning line, and move history. In the reproducible simulation, X won 59.6% of games, O won 27.2%, and 13.2% ended in draws. The results show a clear first-player advantage under random play and provide a baseline for future comparison with strategy-based computer players.

## Design

The project was designed as a reproducible experiment rather than only a playable game. A list of nine elements represents the 3 × 3 board, and the eight possible winning combinations are stored separately. Each game begins with an empty board and Player X. The program selects a random available position, updates the board, checks for a winning line, and changes players if the game is still active. A fixed random seed ensures that another user can reproduce the reported results. The simulation contains 1,000 rounds so that the outcome percentages are more stable than results based on only a few games.

## Data

The final dataset contains 1,000 rows and seven columns. Each row represents one completed game. The columns record a unique game identifier, result, winner, number of moves, draw status, winning line, and complete move history. Validation checks confirm that game identifiers are unique, no values are missing, outcomes belong to the allowed categories, and every game lasts between five and nine moves. The finalized data is exported as `tic_tac_toe_gameplay_data.csv` so it can be reused without rerunning the simulation.

## Algorithms

The project separates gameplay into small, reusable functions. `find_winner()` examines all rows, columns, and diagonals after every move. `simulate_game()` runs one game and returns a structured dictionary. `simulate_games()` repeats the process and builds the pandas DataFrame. The current players use random valid moves, so the algorithm does not intentionally win or block an opponent. This creates a neutral baseline. A future version could evaluate immediate wins, block threats, prioritize the center and corners, or implement the minimax algorithm for optimal play.

## Tools

Python is the primary programming language. Python's standard `random` module generates moves, pandas organizes and validates the gameplay data, and Matplotlib creates the outcome and game-length visualizations. Jupyter Notebook and Google Colab support an understandable, top-to-bottom analysis workflow. Git and GitHub provide version control, project organization, reproducibility, and a public portfolio location. An `environment.yml` file documents the main software dependencies.

## Communication

The project communicates results through a concise notebook, a cleaned Python script, a CSV dataset, a written summary, and presentation slides. The main result is that X, the first player, won 596 of 1,000 games, compared with 272 wins for O and 132 draws. The average game lasted 7.70 moves. These findings should not be interpreted as proof that X always wins; they describe random gameplay under the chosen simulation rules. The most important limitation is that X always moves first while both players use the same random decision rule. The presentation therefore frames the findings as a reproducible baseline and recommends comparing them with strategy-based play in future work.

## Code and Attribution

The project code was written for this course project using standard Python, pandas, and Matplotlib functionality. No external code was copied into the final implementation. Package documentation can be consulted through the official [Python](https://docs.python.org/3/), [pandas](https://pandas.pydata.org/docs/), and [Matplotlib](https://matplotlib.org/stable/) documentation.
