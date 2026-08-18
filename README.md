# Tic-Tac-Toe Data Project

## Overview

This project uses Python to build and analyze a functional Tic-Tac-Toe game. The minimum viable product simulates gameplay between two players who randomly select valid positions. It demonstrates one complete game and then simulates 100 games to examine wins by Player X, wins by Player O, draws, and the number of moves required to finish. The project applies functions, lists, loops, conditional logic, randomization, data collection, and visualization in a way that is accessible to both technical and nontechnical readers.

## Design

The game represents the 3 × 3 board as a list containing nine positions. Players X and O alternate turns and select only unoccupied positions. After each move, the program checks the three rows, three columns, and two diagonals. A full board without a winner is recorded as a draw.

The current MVP includes simulated gameplay. Future versions can accept human input and introduce a strategic computer opponent.

## Data

The program collects the following information from 100 simulated games:

- Number of wins by Player X
- Number of wins by Player O
- Number of draws
- Number of moves per game
- Average number of moves required to finish a game

These results provide a baseline for comparing random gameplay with future strategic gameplay.

## Algorithms

Functions are used to display the board, identify valid moves, evaluate winning combinations, and simulate games. The current algorithm randomly chooses from the unoccupied positions. The planned strategic algorithm will first look for an immediate winning move, then block the opponent, and finally select the center, a corner, or another valid position.

## Tools

- Python 3
- Jupyter Notebook or Google Colab
- Matplotlib
- Git
- GitHub
- GitHub Desktop

## Communication

The notebook combines Markdown explanations, readable Python code, printed gameplay, summary statistics, and a bar chart. These elements explain both the development process and the results of the simulation.

## Repository Structure

```text
tic-tac-toe-data-project/
├── README.md
├── LICENSE
├── environment.yml
├── images/
└── notebooks/
    └── TicTacToe_MVP.ipynb
```

## Installation and Use

### Google Colab

1. Open Google Colab.
2. Upload `notebooks/TicTacToe_MVP.ipynb`.
3. Select **Runtime → Run all**.
4. Review the sample game, statistics, and chart.

### Local Jupyter installation

1. Clone or download this repository.
2. Create the Conda environment:

   ```bash
   conda env create -f environment.yml
   ```

3. Activate it:

   ```bash
   conda activate tic-tac-toe-project
   ```

4. Start Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

5. Open `notebooks/TicTacToe_MVP.ipynb` and run all cells from top to bottom.

## Future Improvements

- Add human keyboard input
- Validate invalid and occupied positions
- Create a strategic computer opponent
- Compare random and strategic gameplay
- Examine first-player advantage
- Add more statistical visualizations

## Author

**Nahida Iqbal**  
MS Industrial Engineering Student  
Southern Illinois University Edwardsville

## License

This project is available under the MIT License.
