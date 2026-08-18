"""Simulate random Tic-Tac-Toe games and summarize their outcomes."""

import random
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


WINNING_LINES = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def find_winner(board):
    """Return the winning player and winning line, if either exists."""
    for line in WINNING_LINES:
        first, second, third = line
        if (
            board[first] != " "
            and board[first] == board[second] == board[third]
        ):
            return board[first], line
    return None, None


def simulate_game(game_id, random_generator):
    """Simulate one random game and return a structured game record."""
    board = [" "] * 9
    current_player = "X"
    move_history = []

    while True:
        available_positions = [
            index for index, value in enumerate(board) if value == " "
        ]
        selected_position = random_generator.choice(available_positions)
        board[selected_position] = current_player
        move_history.append(int(selected_position) + 1)

        winner, winning_line = find_winner(board)
        if winner is not None:
            return {
                "game_id": game_id,
                "result": f"{winner} Win",
                "winner": winner,
                "number_of_moves": len(move_history),
                "ended_in_draw": False,
                "winning_line": str(winning_line),
                "move_history": str(move_history),
            }

        if len(move_history) == 9:
            return {
                "game_id": game_id,
                "result": "Draw",
                "winner": "None",
                "number_of_moves": len(move_history),
                "ended_in_draw": True,
                "winning_line": "None",
                "move_history": str(move_history),
            }

        current_player = "O" if current_player == "X" else "X"


def simulate_games(number_of_games=1000, random_seed=42):
    """Simulate games and return one pandas DataFrame row per game."""
    random_generator = random.Random(random_seed)
    game_records = [
        simulate_game(game_id, random_generator)
        for game_id in range(1, number_of_games + 1)
    ]
    return pd.DataFrame(game_records)


def validate_data(gameplay_data, expected_games):
    """Validate the structure and allowed values of the gameplay dataset."""
    assert len(gameplay_data) == expected_games
    assert gameplay_data["game_id"].is_unique
    assert gameplay_data.isna().sum().sum() == 0
    assert gameplay_data["number_of_moves"].between(5, 9).all()
    allowed_results = {"X Win", "O Win", "Draw"}
    assert set(gameplay_data["result"]).issubset(allowed_results)


def create_results_chart(gameplay_data, output_path):
    """Create and save outcome and game-length charts."""
    result_order = ["X Win", "O Win", "Draw"]
    result_counts = gameplay_data["result"].value_counts().reindex(
        result_order,
        fill_value=0,
    )
    move_counts = gameplay_data["number_of_moves"].value_counts().sort_index()

    figure, axes = plt.subplots(1, 2, figsize=(12, 5))
    bars = axes[0].bar(
        result_counts.index,
        result_counts.values,
        color=["#3D8DFF", "#6DCBF4", "#B8BCC4"],
    )
    axes[0].set_title("Outcomes of Simulated Games")
    axes[0].set_ylabel("Number of Games")
    axes[0].bar_label(bars)

    axes[1].bar(move_counts.index, move_counts.values, color="#3D8DFF")
    axes[1].set_title("Distribution of Game Lengths")
    axes[1].set_xlabel("Number of Moves")
    axes[1].set_ylabel("Number of Games")
    axes[1].set_xticks(range(5, 10))

    figure.tight_layout()
    figure.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close(figure)


def main():
    """Run the complete simulation and export the dataset and chart."""
    project_root = Path(__file__).resolve().parents[1]
    data_directory = project_root / "data"
    image_directory = project_root / "images"
    data_directory.mkdir(exist_ok=True)
    image_directory.mkdir(exist_ok=True)

    number_of_games = 1000
    gameplay_data = simulate_games(number_of_games=number_of_games)
    validate_data(gameplay_data, expected_games=number_of_games)

    gameplay_data.to_csv(
        data_directory / "tic_tac_toe_gameplay_data.csv",
        index=False,
    )
    create_results_chart(
        gameplay_data,
        image_directory / "gameplay_results.png",
    )

    print(gameplay_data["result"].value_counts())
    print(f"Average moves: {gameplay_data['number_of_moves'].mean():.2f}")


if __name__ == "__main__":
    main()
