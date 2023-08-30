import pygame
from shape_generation import ShapeGenerator
from typing import Tuple, List

class Visualization:
    def __init__(self, window_size: Tuple[int, int], grid_size: int, cell_size: int):
        pygame.init()
        self.surface = pygame.display.set_mode(window_size)
        pygame.display.set_caption('Tetris Visualization')
        
        self.shape_gen = ShapeGenerator()
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.grid = [[0] * grid_size for _ in range(grid_size)]
        self.grid_x = (window_size[0] - grid_size * cell_size) // 2
        self.grid_y = (window_size[1] - grid_size * cell_size) // 2
        self.static_shapes_in_hotbar = None

    def draw_background(self, color: Tuple[int, int, int]) -> None:
        """
        Draws a rectangle on the given surface.
        
        Parameters:
            surface (pygame.Surface): The surface to draw on.
            color (Tuple[int, int, int]): The color of the rectangle (R, G, B).
            rect (pygame.Rect): The rectangle dimensions (x, y, width, height).
        """
        self.surface.fill(color)

    def draw_grid(self):
        start_x = self.grid_x
        start_y = self.grid_y

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                cell_color = (255, 255, 255) if self.grid[i][j] == 1 else (0, 0, 0)
                rect = pygame.Rect(start_x + j * self.cell_size, start_y + i * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.surface, cell_color, rect)
                pygame.draw.rect(self.surface, (128, 128, 128), rect, 1)

        grid_bottom = start_y + self.grid_size * self.cell_size
        return grid_bottom


    def draw_tetromino(self, surface: pygame.Surface, tetromino: 'Tetromino', position: Tuple[int, int]) -> None:
        """
        Draws a Tetromino on the given Pygame surface at the specified position.
        
        Parameters:
            surface (pygame.Surface): The surface to draw on.
            tetromino (Tetromino): The Tetromino to draw.
            position (Tuple[int, int]): The position to draw the Tetromino.
        """
        # Pygame drawing logic here
        pass


    def draw_hotbar(self, tetrominos: List[List[List[int]]], grid_bottom: int):
        standard_shape_size = 30
        gap = 10
        num_tetrominos = len(tetrominos)

        hotbar_width = (num_tetrominos * standard_shape_size) + ((num_tetrominos - 1) * gap)
        start_x = (self.grid_size * self.cell_size - hotbar_width) // 2
        start_y = grid_bottom + 10

        # Fill the background of the hotbar 
        self.surface.fill((200, 200, 200), (start_x, start_y, hotbar_width, standard_shape_size + 20))

        for idx, tetromino in enumerate(tetrominos):
            x_offset = start_x + (idx * (standard_shape_size + gap))
            
            # Calculate the bounding box dimensions for each shape
            bounding_box_width = len(max(tetromino, key=len))
            bounding_box_height = len(tetromino)
            
            # Calculate the scaling factors
            width_scale = standard_shape_size / bounding_box_width
            height_scale = standard_shape_size / bounding_box_height
            
            for i, row in enumerate(tetromino):
                for j, cell in enumerate(row):
                    if cell == 1:
                        color = (255, 255, 255)
                        rect = pygame.Rect(
                            x_offset + int(j * width_scale),
                            start_y + 10 + int(i * height_scale),
                            int(width_scale),
                            int(height_scale)
                        )
                        self.surface.fill(color, rect)


    def handle_drag_and_drop(self, event: pygame.event.Event, tetrominos: List['Tetromino'], grid: 'Grid') -> None:
        """
        Handles the drag-and-drop functionality.
        
        Parameters:
            event: The Pygame event to handle.
            tetrominos: List of Tetrominos available for placing.
            grid: The Grid object to place Tetrominos on.
        """
        # Drag-and-drop logic
        pass

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw_background((0, 12, 102))
            grid_bottom = self.draw_grid()

            # Initialize the static shapes in the hotbar if they're not set
            if self.static_shapes_in_hotbar is None:
                self.static_shapes_in_hotbar = [self.shape_gen.get_random_rotated_shape() for _ in range(3)]
            
            # Draw the hotbar using static shapes
            self.draw_hotbar(self.static_shapes_in_hotbar, grid_bottom)
            
            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    window_size = (800, 600)
    grid_size = 8
    cell_size = 50
    
    view = Visualization(window_size, grid_size, cell_size)
    view.run()