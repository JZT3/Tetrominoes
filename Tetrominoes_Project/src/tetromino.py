from typing import List
import random

class Tetromino:
    """
    Class to represent a Tetromino shape.
    """
    
    def __init__(self, shape: List[List[int]]):
        """
        Initialize a Tetromino with a given shape.
        
        Parameters:
            shape (List[List[int]]): 2D array representing the shape.
        """
        self.shape = shape if shape is not None else self.generate_random_shape()

   

    def user_rotate(self) -> None:
        """
        Allows the user to rotate the Tetromino 90 degrees clockwise or counter-clockwise
        depending on which button they enter.
        """
        # Rotation logic here

    def get_shape(self) -> List[List[int]]:
        """
        Returns the current shape of the Tetromino.
        
        Returns:
            List[List[int]]: 2D array representing the shape.
        """
        return self.shape

    def __str__(self) -> str:
        """
        String representation of the Tetromino object for debugging.
        
        :return: String representation of the tetromino shape.
        """
        return "\n".join(" ".join(str(cell) for cell in row) for row in self.shape)
    
    