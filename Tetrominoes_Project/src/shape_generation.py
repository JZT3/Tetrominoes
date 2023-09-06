from typing import Set, List, Tuple
import random

class ShapeGenerator:
    """
    This class is responsible for Tetromino shape generation and checking the uniqueness
    """

    def __init__(self):
        self.unique_shapes = self.generate_shapes()
        self.unique_shapes_2D = [self.bitmask_to_2D(shape) for shape in self.unique_shapes]
        self.bounding_boxes = self.calculate_bounding_boxes()


    def generate_shapes(self) -> Set[int]:
        """
        Generates all unique shapes and returns a set of shapes in canonical forms.
        """
        unique_shapes = set()

        for bitmask in range(1, 2 ** 9):
            canonical_form = self.get_canonical_form(bitmask)
            if self.is_connected(canonical_form):  # Using self to call instance method
                unique_shapes.add(canonical_form)

        return unique_shapes


    @staticmethod
    def get_canonical_form(bitmask: int) -> int:
        """
        Generates all the rotations of a shape and returns the canonical (smallest) form.
        """
        rotations = [bitmask]
        for _ in range(3):  # Three more rotations to consider
            bitmask = ShapeGenerator.rotate_bitmask(bitmask)
            rotations.append(bitmask)

        return min(rotations)


    @staticmethod
    def rotate_bitmask(bitmask: int) -> int:
        """
        Rotates the shape represented by a bitmask 90 degrees clockwise.
        """
        grid = [[0, 0, 0] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                cell_value = (bitmask >> (3 * i + j)) & 1
                grid[i][j] = cell_value
        
        rotated_grid = [[0, 0, 0] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                rotated_grid[j][2 - i] = grid[i][j]

        rotated_bitmask = 0
        for i in range(3):
            for j in range(3):
                rotated_bitmask |= rotated_grid[i][j] << (3 * i + j)

        return rotated_bitmask

    def is_connected(self, bitmask: int) -> bool:
        """
        Check if a shape is a connected component and has no holes.
        
        Args:
            bitmask: The bitmask representing the shape.
            
        Returns:
            True if the shape is connected and has no holes, False otherwise.
        """
        num_ones = bin(bitmask).count('1')
        grid = self.bitmask_to_grid(bitmask)
        first_filled_cell = self.find_first_filled_cell(grid)

        if first_filled_cell is not None:
            visited = set()
            to_visit = [first_filled_cell]

            while to_visit:
                current = to_visit.pop()
                if current in visited:
                    continue

                visited.add(current)
                x, y = current

                if len(visited) == num_ones:
                    break

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_x, new_y = x + dx, y + dy

                    if (0 <= new_x < 3 and 0 <= new_y < 3) and (new_x, new_y) not in visited:
                        if grid[new_x][new_y] == 1:
                            to_visit.append((new_x, new_y))
                        else:
                            # Check if this empty cell is reachable from an edge; if not, it's a hole
                            for edge_dx, edge_dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                edge_x, edge_y = new_x + edge_dx, new_y + edge_dy
                                if not (0 <= edge_x < 3 and 0 <= edge_y < 3):
                                    break  # This empty cell is reachable from an edge, so it's not a hole
                            else:
                                return False  # This empty cell is not reachable from an edge; it's a hole

            return len(visited) == num_ones
        return False
    
    def bitmask_to_grid(self, bitmask: int) -> List[List[int]]:
        """
        Convert a bitmask to a 3x3 grid.
        
        Args:
            bitmask: The bitmask representing the shape.
            
        Returns:
            The 3x3 grid representing the shape.
        """
        grid = [[0, 0, 0] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                cell_value = (bitmask >> (3 * i + j)) & 1
                grid[i][j] = cell_value
        return grid
    
    def find_first_filled_cell(self, grid: List[List[int]]) -> [Tuple[int, int]]:
        """
        Find the first filled cell in a 3x3 grid.
        
        Args:
            grid: The 3x3 grid representing the shape.
            
        Returns:
            The coordinates (i, j) of the first filled cell, or None if no cell is filled.
        """
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 1:
                    return i, j
        return None

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


    def calculate_bounding_boxes(self) -> dict:
        """
        Calculate the bounding boxes for all unique shapes.
        
        Returns:
            A dictionary mapping each unique shape to its bounding box dimensions.
        """
        bounding_boxes = {}
        for shape in self.unique_shapes:
            shape_2D = self.bitmask_to_2D(shape)
            rows = len(shape_2D)
            cols = len(max(shape_2D, key=len))
            bounding_boxes[shape] = (rows, cols)
        return bounding_boxes

if __name__ == "__main__":
    shape_gen = ShapeGenerator()
    print(f"The maximum number of unique contiguous shapes in a 3x3 grid is {len(shape_gen.unique_shapes)}.")
    # Display all unique shapes in their 2D array representation
    for _ in range(5):
        shape = shape_gen.get_random_shape()
        print(shape)
