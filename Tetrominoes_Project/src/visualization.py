import pygame
from typing import Tuple, List

def initialize_window(size: Tuple[int, int]) -> pygame.Surface:
    """
    Initializes the Pygame window and returns the surface.
    
    Parameters:
        size (Tuple[int, int]): The dimensions of the window.
        
    Returns:
        pygame.Surface: The surface to draw on.
    """
    pygame.init()
    surface = pygame.display.set_mode(size)
    pygame.display.set_caption('Tetris Visualization')
    return surface


def draw_background(surface: pygame.Surface, color: Tuple[int, int, int], rect: pygame.Rect):
    """
    Draws a rectangle on the given surface.
    
    Parameters:
        surface (pygame.Surface): The surface to draw on.
        color (Tuple[int, int, int]): The color of the rectangle (R, G, B).
        rect (pygame.Rect): The rectangle dimensions (x, y, width, height).
    """
    pygame.draw.rect(surface, color, rect)


def draw_grid(surface: pygame.Surface, grid: 'Grid') -> None:
    """
    Draws the 8x8 grid on the given Pygame surface.
    
    Parameters:
        surface (pygame.Surface): The surface to draw on.
        grid (Grid): The Grid object representing the grid state.
    """
    # Pygame drawing logic here
    pass

def draw_tetromino(surface: pygame.Surface, tetromino: 'Tetromino', position: Tuple[int, int]) -> None:
    """
    Draws a Tetromino on the given Pygame surface at the specified position.
    
    Parameters:
        surface (pygame.Surface): The surface to draw on.
        tetromino (Tetromino): The Tetromino to draw.
        position (Tuple[int, int]): The position to draw the Tetromino.
    """
    # Pygame drawing logic here
    pass

def draw_hotbar(surface: pygame.Surface, tetrominos: List['Tetromino']) -> None:
    """
    Draws the hotbar at the bottom of the screen.
    
    Parameters:
        surface (pygame.Surface): The surface to draw on.
        tetrominos (List[Tetromino]): List of Tetrominos to display on the hotbar.
    """
    # Drawing the hotbar and tetrominos
    pass

def handle_drag_and_drop(event: pygame.event.Event, tetrominos: List['Tetromino'], grid: 'Grid') -> None:
    """
    Handles the drag-and-drop functionality.
    
    Parameters:
        event (pygame.event.Event): The Pygame event to handle.
        tetrominos (List[Tetromino]): List of Tetrominos available for placing.
        grid (Grid): The Grid object to place Tetrominos on.
    """
    # Drag-and-drop logic
    pass

if __name__ == "__main__":
    window_size = (800, 600)
    surface = initialize_window(window_size)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Example drawing
        draw_background(surface, (255, 0, 0), pygame.Rect(50, 50, 50, 50))

        pygame.display.update()
    
    pygame.quit()