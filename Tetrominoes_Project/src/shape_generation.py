from typing import Set, List
import random

class ShapeGenerator:
    """
    This class is responsible for Tetromino shape generation and checking the uniqueness

    """

    def __init__(self):
        self.unique_shapes = self.generate_shapes()


    @staticmethod
    def generate_shapes() -> Set[int]:
        unique_shapes = set()

        for bitmask in range(1, 2 ** 9):
            if bin(bitmask).count('1') == 3 and ShapeGenerator.is_connected(bitmask):
                unique_shapes.add(bitmask)

        return unique_shapes


    @staticmethod
    def is_connected(bitmask: int) -> bool:
        grid = [[0, 0, 0] for _ in range(3)]
        first_filled_cell = None
        for i in range(3):
            for j in range(3):
                cell_value = (bitmask >> (3 * i + j)) & 1
                grid[i][j] = cell_value
                if cell_value == 1 and first_filled_cell is None:
                    first_filled_cell = 3 * i + j  # Convert to 1D index

        # If there are no filled cells, the shape is not connected
        if first_filled_cell is None:
            return False

        visited = set()
        to_visit = [first_filled_cell]

        while to_visit:
            current = to_visit.pop()
            if current in visited:
                continue
            visited.add(current)

            x, y = divmod(current, 3)  # Convert back to 2D coordinates

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < 3 and 0 <= new_y < 3 and grid[new_x][new_y] == 1:
                    to_visit.append(3 * new_x + new_y)  # Convert to 1D index

        return len(visited) == bin(bitmask).count('1')



    def get_random_shape(self) -> List[List[int]]:
        shape_bitmask = random.choice(list(self.unique_shapes))
        shape_2D = self.bitmask_to_2D(shape_bitmask)
        return shape_2D


    @staticmethod
    def bitmask_to_2D(bitmask: int) -> List[List[int]]:
        shape_2D = []
        for row in range(3):
            shape_row = []
            for col in range(3):
                bit_position = 3 * row + col
                cell_value = (bitmask >> bit_position) & 1
                shape_row.append(cell_value)
            shape_2D.append(shape_row)
        return shape_2D
    

    @staticmethod
    def apply_random_rotation(shape: List[List[int]]) -> List[List[int]]:
        """
        Applys a random number of 90-degree rotations to the shape.

        Args:
            shape: The 2D array representing the shape.

        Returns:
            The rotated shape.
        """
        rotations_num = random.randint(0, 3)  # 0 to 3 rotations
        for _ in range(rotations_num):
            shape = [[shape[2 - j][i] for j in range(3)] for i in range(3)]
        return shape
    
    def get_random_rotated_shape(self) -> List[List[int]]:
        shape = self.get_random_shape()
        rotated_shape = self.apply_random_rotation(shape)
        return rotated_shape
    

if __name__ == "__main__":
    shape_gen = ShapeGenerator()
    print(f"The maximum number of unique contiguous shapes in a 3x3 grid is {len(shape_gen.unique_shapes)}.")
    
    # Display all unique shapes in their 2D array representation
    for _ in range(5):
        shape = shape_gen.get_random_rotated_shape()
        print(shape)