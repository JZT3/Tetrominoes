from typing import Set, Tuple, List
from collections import deque
import random

class ShapeGenerator:
    """
    This class is responsible for Tetromino shape generation and checking the uniqueness

    """
    
    @staticmethod
    def is_connected(bitmask: int) -> bool:
        # TODO: Implement the connectivity check logic here
        # This function should return True if the shape represented by the bitmask is connected
        return True  # Placeholder

    @classmethod
    def generate_shapes(cls) -> Set[int]:
        unique_shapes = set()

        for bitmask in range(1, 2 ** 9):
            if bin(bitmask).count('1') == 3 and cls.is_connected(bitmask):
                unique_shapes.add(bitmask)

        return unique_shapes

    @classmethod
    def generate_random_shape(cls) -> List[List[int]]:
        # TODO: Generate a random bitmask and convert it to a 2D list representation
        pass

    @classmethod
    def unique_shape_check(cls, num_of_shapes: int) -> List[List[List[int]]]:
        # TODO: Generate unique shapes up to 'num_of_shapes' using bitmasks
        # Then convert them to 2D list format to return
        pass

    @classmethod
    def shape_normalization(cls, shape: List[List[int]]) -> List[List[int]]:
        # TODO: Implement the normalization logic here
        pass

    @classmethod
    def rotation_permutations(cls, shape: List[List[int]]) -> List[List[int]]:
        # TODO: Implement the rotation logic here
        pass

    @classmethod
    def shape_to_tuple(cls, shape: List[List[int]]) -> Tuple[int, ...]:
        return tuple(cell for row in shape for cell in row)

if __name__ == "__main__":
    unique_shapes = ShapeGenerator.generate_shapes()
    print(f"The maximum number of unique contiguous shapes in a 3x3 grid is {len(unique_shapes)}.")
