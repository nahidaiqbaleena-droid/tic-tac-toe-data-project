# Tic-Tac-Toe Data Project

## Overview

This project uses Python to build and analyze a functional Tic-Tac-Toe game. The final experiment simulates 1,000 games between two players who randomly select valid positions. It examines wins by Player X, wins by Player O, draws, and the number of moves required to finish. The project applies functions, lists, loops, conditional logic, randomization, pandas data collection, validation, and visualization in a way that is accessible to both technical and nontechnical readers.

## Design

The game represents the 3 × 3 board as a list containing nine positions. Players X and O alternate turns and select only unoccupied positions. After each move, the program checks the three rows, three columns, and two diagonals. A full board without a winner is recorded as a draw.

The current MVP includes simulated gameplay. Future versions can accept human input and introduce a strategic computer opponent.

## Data

The program collects the following information from 1,000 simulated games:

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
- pandas

## Communication

The project combines Markdown explanations, readable Python code, printed gameplay, summary statistics, charts, a one-page written report, and presentation slides. These elements explain both the development process and the results of the simulation.

## Key Results

- Player X won 596 of 1,000 games (59.6%).
- Player O won 272 games (27.2%).
- 132 games ended in draws (13.2%).
- The average game lasted 7.70 moves.

Because X always moved first, the simulation shows a first-player advantage under random play. It is a reproducible baseline rather than proof that X always wins.

## Repository Structure

```text
tic-tac-toe-data-project/
├── README.md
├── PROJECT_WRITEUP.md
├── LICENSE
├── environment.yml
├── data/
│   └── tic_tac_toe_gameplay_data.csv
├── images/
│   └── gameplay_results.png
├── notebooks/
│   ├── TicTacToe_MVP.ipynb
│   └── TicTacToe_Data_Acquisition.ipynb
├── presentation/
│   └── TicTacToe_Project_Presentation.pptx
└── src/
    └── tic_tac_toe_analysis.py
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

## Final Project Materials

- [Written project description](PROJECT_WRITEUP.md)
- [Presentation slides](presentation/TicTacToe_Project_Presentation.pptx)
- [Clean Python script](src/tic_tac_toe_analysis.py)
- [Final gameplay dataset](data/tic_tac_toe_gameplay_data.csv)

## Author

**Nahida Iqbal**  
MS Industrial Engineering Student  
Southern Illinois University Edwardsville

## License

This project is available under the MIT License.
