from typing import List, Callable, Dict, Any

class Tetromino:
    """
    Class to represent a Tetromino shape in a Tetris game.
    """
    def __init__(self, shape: List[List[int]], x: int, y: int, hotbar: List[List[List[int]]]):
        """
        Initialize a Tetromino with a given shape at position (x, y) and provide a hotbar for game-over checks.
        
        Parameters:
            shape (List[List[int]]): 2D array representing the shape.
            x (int): The x-coordinate of the shape.
            y (int): The y-coordinate of the shape.
            hotbar (List[List[List[int]]]): List of available Tetromino shapes.
        """
        self.shape = shape
        self.x = x
        self.y = y
        self.hotbar = hotbar
        self.score = 0

    def event_handler(self, event_name: str) -> Callable[[Callable[[Any], None]], Callable[[Any], None]]:
        """
        Decorator to register event handlers for the Tetromino class.
        
        Parameters:
            event_name (str): The name of the event.
            
        Returns:
            The decorator function.
        """
        def decorator(func: Callable[[Any], None]) -> Callable[[Any], None]:
            setattr(self, event_name, func)
            return func
        return decorator

    def trigger_event(self, event_name: str, grid: List[List[int]]) -> None:
        """
        Trigger an event based on the name provided.
        
        Parameters:
            event_name (str): The name of the event to be triggered.
            grid (List[List[int]]): The current grid.
        """
        handler = getattr(self, event_name, None)
        if handler:
            handler(grid)
        else:
            print(f"Unknown event: {event_name}")



    def is_valid_move(self, new_shape: List[List[int]], x: int, y: int, grid: List[List[int]], set_in_place: bool = False) -> bool:
        grid_height = len(grid)
        grid_width = len(grid[0])
        
        for i, row in enumerate(new_shape):
            for j, cell in enumerate(row):
                if cell:  # If it's a filled cell in the shape
                    if i + y >= grid_height or j + x < 0 or j + x >= grid_width or grid[i + y][j + x]:
                        return False
        return True



    def player_move(self, direction: str, grid: List[List[int]]) -> None:
        dx, dy = 0, 0
        if direction == "left":
            dx = -1
        elif direction == "right":
            dx = 1
        elif direction == "up":
            dy = 1
        elif direction == "down":
            dy = -1
            
        if self.is_valid_move(self.shape, self.x + dx, self.y + dy, grid):
            self.x += dx
            self.y += dy


    def rotate_shape(self, rotation_type: str) -> List[List[int]]:
        """
        Helper method to rotate the shape of the tetromino.
        
        Parameters:
            rotation_type: Either 'cw' (clockwise) or 'ccw' (counterclockwise).
            
        Returns:
            The rotated shape.
        """
        # Create a copy of the current shape
        new_shape = [list(row) for row in self.shape]
        
        if rotation_type == 'cw':
            # Rotate the shape clockwise
            n = len(new_shape)
            for i in range(n // 2):
                for j in range(i, n - i - 1):
                    temp = new_shape[i][j]
                    new_shape[i][j] = new_shape[n - j - 1][i]
                    new_shape[n - j - 1][i] = new_shape[n - i - 1][n - j - 1]
                    new_shape[n - i - 1][n - j - 1] = new_shape[j][n - i - 1]
                    new_shape[j][n - i - 1] = temp
        elif rotation_type == 'ccw':
            # Rotate the shape counterclockwise
            n = len(new_shape)
            for i in range(n // 2):
                for j in range(i, n - i - 1):
                    temp = new_shape[i][j]
                    new_shape[i][j] = new_shape[j][n - i - 1]
                    new_shape[j][n - i - 1] = new_shape[n - i - 1][n - j - 1]
                    new_shape[n - i - 1][n - j - 1] = new_shape[n - j - 1][i]
                    new_shape[n - j - 1][i] = temp
        
        return new_shape


    def rotate_cw(self, grid: List[List[int]]) -> None:
        """
        Rotate the tetromino shape clockwise and update the grid.
        
        Parameters:
            grid: The current grid.
        """
        new_shape = self.rotate_shape('cw')
        if self.is_valid_move(new_shape, self.x, self.y, grid):
            self.shape = new_shape


    def rotate_ccw(self, grid: List[List[int]]) -> None:
        """
        Rotate the tetromino shape counterclockwise and update the grid.
        
        Parameters:
            grid (List[List[int]]): The current grid.
        """
        new_shape = self.rotate_shape('ccw')
        if self.is_valid_move(new_shape, self.x, self.y, grid):
            self.shape = new_shape


    def set_in_place(self, grid: List[List[int]]) -> None:
        """
        Set the Tetromino in place on the grid and trigger relevant events.
        
        Parameters:
            grid (List[List[int]]): The current grid.
        """
        if self.is_valid_move(self.shape, self.x, self.y, grid, set_in_place=True):
            self.update_grid(grid)
            self.trigger_event('handle_line_clears', grid)
        elif self.is_game_over(grid):
            self.trigger_event('handle_set_in_place_failure', grid)



    def handle_line_clears(self, grid: List[List[int]]) -> None:
        rows_to_clear = {i for i, row in enumerate(grid) if all(cell == 1 for cell in row)}
        
        # Create a new grid with cleared rows removed and empty rows added at the top
        new_grid = [[0] * len(grid[0])] * len(rows_to_clear) + [row for i, row in enumerate(grid) if i not in rows_to_clear]
        
        # Update the grid with the new grid
        for i in range(len(grid)):
            grid[i] = new_grid[i]
        
        # Update the score
        self.score += len(rows_to_clear) * 10
        
        # Optional: Add sound effects or animations here



    def handle_set_in_place_failure(self) -> None:
    # Logic for handling set in place failure (e.g., game over)
        pass


    def update_grid(self, grid: List[List[int]]) -> None:
        """
        Update the grid based on the current Tetromino shape and position.
        
        Parameters:
            grid (List[List[int]]): The current grid.
        """
        for i, row in enumerate(self.shape):
            grid_row = grid[i + self.y]
            for j, cell in enumerate(row):
                if cell:
                    grid_row[self.x + j] = 1  # In-place update

    def is_game_over(self, grid: List[List[int]]) -> bool:
        """
        Check if the game is over.
        
        Parameters:
            grid (List[List[int]]): The current grid.
            
        Returns:
            bool: True if the game is over, False otherwise.
        """
        for tetromino_shape in self.hotbar:
            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    if self.is_valid_move(tetromino_shape, x, y, grid):
                        return False
                    if y == 0 and x == 0:
                        break
                if y == 0:
                    break
        return True


    def __str__(self) -> str:
        """
        String representation of the Tetromino object for debugging.
        
        :return: String representation of the tetromino shape.
        """
        return "\n".join(" ".join(str(cell) for cell in row) for row in self.shape)
    

