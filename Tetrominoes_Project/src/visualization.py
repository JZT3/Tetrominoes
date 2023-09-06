import pygame
from shape_generation import ShapeGenerator
from tetromino_functionality import Tetromino
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
        self.hotbar = [self.shape_gen.get_random_shape() for _ in range(3)]
        self.selected_tetromino: Optional[Tetromino] = None
        self.grid_center_x = self.grid_x + (self.grid_size * self.cell_size) // 2
        self.grid_center_y = self.grid_y + (self.grid_size * self.cell_size) // 2


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


    def draw_hotbar(self, tetrominos: List[List[List[int]]]):
        standard_shape_size = 30
        gap = 10
        num_tetrominos = len(tetrominos)

        grid_bottom_y = self.grid_center_y + (self.grid_size * self.cell_size) // 2
        grid_bottom_x = self.grid_center_x + (self.grid_size * self.cell_size) // 2

        # Define bounding box dimensions and scaling factors before using them
        bounding_box_width = 3
        bounding_box_height = 3
        width_scale = standard_shape_size // bounding_box_width
        height_scale = standard_shape_size // bounding_box_height

        # Calculate total shapes' width including gaps
        shapes_width = sum(len(t) * width_scale for t in tetrominos)

        # Total hotbar width including shapes and gaps
        total_width = shapes_width + (len(tetrominos) - 1) * gap

        hotbar_width = (num_tetrominos * standard_shape_size) + ((num_tetrominos - 1) * gap)
        start_x = self.grid_center_x - (total_width // 2)
        start_y = grid_bottom_y

        # Fill the background of the hotbar 
        self.surface.fill((200, 200, 200), (start_x, start_y, hotbar_width, standard_shape_size + 20))

        for idx, tetromino in enumerate(tetrominos):
            x_offset = start_x + (idx * (standard_shape_size + gap))

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


    def update_grid_with_tetromino(self, tetromino: Tetromino) -> None:
        """
        Updates the grid to reflect the position of the Tetromino.
        
        Parameters:
            tetromino (Tetromino): The Tetromino object to place on the grid.
        """
        # Clear the grid
        self.grid = [[0] * self.grid_size for _ in range(self.grid_size)]

        for i, row in enumerate(tetromino.get_shape()):
            for j, cell in enumerate(row):
                if cell == 1:
                    x, y = tetromino.x + j, tetromino.y + i
                    if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
                        self.grid[y][x] = 1

    def handle_action(self, key):
        if not self.selected_tetromino:
            return
        
        actions = {
            # Movement Keys
            pygame.K_a: self.selected_tetromino.move_left,
            pygame.K_d: self.selected_tetromino.move_right,
            pygame.K_s: self.selected_tetromino.move_down,
            pygame.K_w: self.selected_tetromino.move_up,
            pygame.K_q: self.selected_tetromino.rotate_counter_clockwise,
            pygame.K_e: self.selected_tetromino.rotate_clockwise,
            pygame.K_SPACE: self.selected_tetromino.set_in_place,
            
            # Hotbar keys
            pygame.K_1: 1,
            pygame.K_KP1: 1,
            pygame.K_2: 2,
            pygame.K_KP2: 2,
            pygame.K_3: 3,
            pygame.K_KP3: 3,
        }
        if key in actions:
            actions[key](self.grid)


    def run(self):
        running = True
        
        hotbar_keys = {
            pygame.K_1: 0,
            pygame.K_KP1: 0,
            pygame.K_2: 1,
            pygame.K_KP2: 1,
            pygame.K_3: 2,
            pygame.K_KP3: 2,
        }
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key in hotbar_keys:
                        index = hotbar_keys[event.key]
                        self.selected_tetromino = Tetromino(self.hotbar[index])
                    else:
                        self.handle_action(event.key)
                        for key, action in key_mapping.items():
                            if event.key == key:
                                action(self.grid)
                                self.update_grid_with_tetromino(self.selected_tetromino)
                    

                    
                    if event.key in hotbar_keys:
                        index = hotbar_keys[event.key]
                        self.selected_tetromino = Tetromino(self.hotbar[index])

            self.draw_background((0, 12, 102))
            self.draw_grid()

            # Draw the hotbar and other UI elements
            self.draw_hotbar(self.hotbar)

            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    window_size = (800, 600)
    grid_size = 8
    cell_size = 50
    
    view = Visualization(window_size, grid_size, cell_size)
    view.run()