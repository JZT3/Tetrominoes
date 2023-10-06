# Tetrimino Solver Project

## Introduction
This project is a personal exploration aimed at managing a larger-scale project, diving deep into Object-Oriented Programming (OOP) concepts in Python, and getting hands-on experience with Pygame. As a Python developer, I was inspired by the mobile game [Block Puzzle](https://play.google.com/store/apps/details?id=game.puzzle.blockpuzzle&hl=en_US&gl=US). Intrigued by its simple yet challenging gameplay, I decided to create a solver for it as a way to apply and showcase my growing skills in Python.

## Objectives
- Manage and develop a medium-scale project from the ground up.
- Showcase the application of OOP principles in Python.
- Experiment with Pygame for the first time.
- Develop a solver for the Block Puzzle game.

## Features
- **Tetrimino Shape Generation:** Dynamically generates all unique Tetrimino shapes within a 3x3 grid.
- **Isomorphic Shape Filtering:** Efficiently filters out isomorphic Tetrimino shapes.
- **Connected Component Checking:** Verifies if a given shape is a connected component without holes.
- **Bounding Box Calculation:** Computes the bounding box dimensions for each unique shape.

## How It Works
1. **Shape Generation:** Generates all possible Tetrimino shapes and filters out isomorphic ones to get a set of unique shapes.
2. **Solver Algorithm:** (To be implemented) Develop an algorithm that efficiently solves the Block Puzzle game using the generated Tetrimino shapes.
3. **Pygame Visualization:** Visualize the solving process using Pygame.

## Usage
### Prerequisites
- Python 3.x
- Pygame (if visualization is to be implemented)

### Running the Project
1. Clone the repository:
    ```bash
    git clone <REPOSITORY_LINK>
    cd <REPOSITORY_NAME>
    ```
2. Run the Tetrimino Solver:
    ```bash
    python main.py
    ```

## Testing
The project contains a suite of tests to ensure the correct generation and manipulation of Tetrimino shapes. To run the tests, use the following command:
```bash
python -m unittest discover tests
