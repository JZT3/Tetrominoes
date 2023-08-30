from typing import Set, Tuple, List
import random

class ShapeGenerator:
    """
    This class is responsible for Tetromino shape generation and checking the uniqueness

    """
    def __init__(self) -> None:
        pass

    @staticmethod
    def generate_random_shape() -> List[List[int]]:
        """
        Generate a random Tetromino shape no bigger than a 3x3 units.
        Each random shape will be contigous. 
        
        Returns:
            List[List[int]]: 2D array representing the random shape.
        """
        # Initialize a 3x3 matrix with zeros
        shape = [[0 for _ in range(3)] for _ in range(3)]
        
        # Randomly pick a starting cell
        start_x, start_y = random.randint(0, 2), random.randint(0, 2)
        shape[start_x][start_y] = 1
        
        # List to keep track of filled cells
        filled_cells = [(start_x, start_y)]
        
        # Expand from the starting cell to form a contiguous shape
        for _ in range(random.randint(1, 8)):  # 1 to 8 additional cells to be filled
            x, y = random.choice(filled_cells)
            
            # Get list of empty contiguous cells
            contiguous_empty_cells = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= x + dx < 3 and 0 <= y + dy < 3 and shape[x + dx][y + dy] == 0:
                    contiguous_empty_cells.append((x + dx, y + dy))
            
            # If there are no empty contiguous cells, break
            if not contiguous_empty_cells:
                break
            
            # Randomly pick one empty contiguous cell and fill it
            new_x, new_y = random.choice(contiguous_empty_cells)
            shape[new_x][new_y] = 1
            filled_cells.append((new_x, new_y))
        
        return shape

    @staticmethod
    def is_contiguous(shape: List[List[int]]) -> bool:
        """Check if a shape is contiguous."""
        visited = set()
        to_visit = []

        # Find the first filled cell
        for i in range(3):
            for j in range(3):
                if shape[i][j] == 1:
                    to_visit.append((i, j))
                    break
            if to_visit:
                break

        # Depth-First Search to check contiguity
        while to_visit:
            x, y = to_visit.pop()
            if (x, y) in visited:
                continue
            visited.add((x, y))

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < 3 and 0 <= new_y < 3 and shape[new_x][new_y] == 1:
                    to_visit.append((new_x, new_y))
                    
        return len(visited) == sum(cell for row in shape for cell in row)

    @classmethod
    def rotation_permutations(cls, shape: List[List[int]]) -> List[List[int]]:
        """Generate all unique rotations of a shape."""
        unique_rotations: Set[Tuple[int, ...]] = set()

        current_shape = shape
        for _ in range(4):  # Only 4 rotations are possible for any shape
            current_shape = [[current_shape[2 - j][i] for j in range(3)] for i in range(3)]
            normalized_shape = cls.shape_normalization(current_shape)
            unique_rotations.add(cls.shape_to_tuple(normalized_shape))

        # Convert back to List[List[int]] format
        unique_rotations = [list(map(list, zip(*[iter(tpl)]*3))) for tpl in unique_rotations]
        
        return unique_rotations

    @classmethod
    def shape_normalization(cls, shape: List[List[int]]) -> List[List[int]]:
        """Translate a shape to its canonical form."""
        rows = [row for row in shape if any(cell == 1 for cell in row)]
        if not rows:
            return [[0, 0, 0] for _ in range(3)]
        
        min_col = min(col for row in shape for col, cell in enumerate(row) if cell == 1)
        normalized_rows = [row[min_col:] + row[:min_col] for row in rows]
        return normalized_rows + [[0, 0, 0] for _ in range(3 - len(rows))]


    @classmethod
    def shape_to_tuple(cls, shape: List[List[int]]) -> Tuple[int, ...]:
        """Convert a shape to a tuple for set operations."""
        return tuple(cell for row in shape for cell in row)
    

    @classmethod
    def unique_shape_check(cls, num_of_shapes:int) -> List:
        """
        Generate a set of unique Tetromino shapes up to the desired number of shapes.

        Parameters:
            desired_number_of_shapes (int): The number of unique shapes to generate.

        Returns:
            List[List[List[int]]]: A list of unique Tetromino shapes.
        """
        unique_shapes = set()
        unique_shape_matrices = []

        while len(unique_shapes) < num_of_shapes:
            shape = cls.generate_random_shape()
            normalized_shape = cls.shape_normalization(shape)
            identifier = cls.shape_to_tuple(normalized_shape)

            # Check for redundant shapes
            is_redundant = any(cls.shape_to_tuple(cls.shape_normalization(rotated_shape)) in unique_shapes
                            for rotated_shape in cls.rotation_permutations(shape))

            if not is_redundant:
                unique_shapes.add(identifier)
                unique_shape_matrices.append(shape)

        return unique_shape_matrices 


if __name__ == "__main__":
    """
    I want to find the theoretical max number of possible shape configurations
    inside a 3x3 grid. There are 2^9 (512) possibilities.

    Each cell has 2 choices 0 or 1. There are 9 cells in a 3x3 grid.
    total configurations = 2^9.
    
    Then I want to filter out all the non-contiguous shapes.
    I do this by considering translations and rotations
    """
    unique_shapes: Set[Tuple[int, ...]] = set()

    # Loop over all 512 possible configurations
    for i in range(2**9):
        shape = [[(i >> (3 * row + col)) & 1 for col in range(3)] for row in range(3)]
        
        if not ShapeGenerator.is_contiguous(shape):
            continue

        # Check all rotations
        for _ in range(4):
            normalized_shape = ShapeGenerator.shape_normalization(shape)
            unique_shapes.add(ShapeGenerator.shape_to_tuple(normalized_shape))
            shape = ShapeGenerator.rotation_permutations(shape)

    print(f"The maximum number of unique contiguous shapes in a 3x3 grid is {len(unique_shapes)}.")

