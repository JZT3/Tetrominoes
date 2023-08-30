from typing import List, Tuple

class Grid:
    """
    Class to represent an 8x8 grid.
    """

    def __init__(self, size: Tuple[int, int]):
        """
        Initialize an empty grid with a given size.
        
        Parameters:
            size (Tuple[int, int]): Dimensions of the grid (rows, columns).
        """
        self.grid = [[0 for _ in range(size[1])] for _ in range(size[0])]

    def place_tetromino(self, tetromino: Tetromino, position: Tuple[int, int]):
        """
        Places a Tetromino on the grid at the specified position.
        
        Parameters:
            tetromino (Tetromino): The Tetromino to place.
            position (Tuple[int, int]): The top-left corner position to start placing the Tetromino.
        """
        # Placement logic here

    def is_valid_placement(self, tetromino: Tetromino, position: Tuple[int, int]) -> bool:
        """
        Checks if a Tetromino can be placed at the specified position without overlapping.
        
        Parameters:
            tetromino (Tetromino): The Tetromino to check.
            position (Tuple[int, int]): The top-left corner position to start placing the Tetromino.
        
        Returns:
            bool: True if valid placement, False otherwise.
        """
        # Validation logic here

    def row_column_clear(self):
        """
        Clears rows or columns that were filled.
        """
        # Clear filled rows

        # Clear filled columns