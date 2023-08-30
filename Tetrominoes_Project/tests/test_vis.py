# import pytest
# from ..src.visualization import initialize_window, draw_hotbar, handle_drag_and_drop
# from ..src.grid import Grid
# from ..src.tetromino import Tetromino

# # Mocked Tetromino object for testing
# mock_tetromino = Tetromino([[1]])

# # Mocked Grid object for testing
# mock_grid = Grid((8, 8))

# class TestVisualization():

#     def test_initialize_window():
#         surface = initialize_window((800, 600))
#         assert surface.get_size() == (800, 600)
    

#     def test_hotbar_initialization(self):
#         """
#         Test if the hotbar initializes with up to 3 random tetrominos
#         """
#         surface = initialize_window((800, 600))
#         draw_hotbar(surface, [mock_tetromino, mock_tetromino, mock_tetromino])
#         # Assuming draw_hotbar changes the color of certain pixels to indicate tetrominos
#         assert surface.get_at((x, y)) == expected_color


#     def test_hotbar_refill(self):
#         """
#         Test if the hotbar refills only when all 3 slots are empty
#         """
#         pass


#     def test_drag_and_drop(self):
#         """
#         Test if a drag-and-drop operation updates the grid and the hotbar correctly
#         """
#         surface = initialize_window((800, 600))
#         event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {"pos": (100, 100)})
#         handle_drag_and_drop(event, [mock_tetromino, mock_tetromino], mock_grid)
#         # Assuming handle_drag_and_drop modifies the grid object upon successful drop
#         assert mock_grid.some_attribute == expected_value  # Replace some_attribute and expected_value as needed
            