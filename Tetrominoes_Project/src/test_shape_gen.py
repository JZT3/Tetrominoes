import unittest
from shape_generation import ShapeGenerator
import numpy as np

class TestShapeGeneration(unittest.TestCase):
    # Test 1: is_contiguous
    def test_is_contiguous(self):
        shape_gen = ShapeGenerator()

        bitmask1 = 0b000110110
        self.assertTrue(shape_gen.is_connected(bitmask1))

        bitmask2 = 0b100001001
        self.assertFalse(shape_gen.is_connected(bitmask2))


    # Test 2: rotation_permutations
    def test_rotation_permutations(self):
        shape_gen = ShapeGenerator()

        bitmask = 0b001010110
        rotated_bitmask = 0b000101110  # This should be the 90-degree clockwise rotated bitmask of the original
        self.assertEqual(shape_gen.rotate_bitmask(bitmask), rotated_bitmask)


    # # Test 3: unique_shape_check
    def test_unique_shape_check(self):
            shape_gen = ShapeGenerator()
            unique_shapes = shape_gen.unique_shapes  # Using the instance variable
            self.assertGreaterEqual(len(unique_shapes), 1)  # Replace 1 with whatever the minimum expected number is
            for shape in unique_shapes:
                self.assertTrue(shape_gen.is_connected(shape))

                
    def test_shape_normalization(self):
        bitmask = 0b100110000
        normalized_bitmask = 0b000110100  # This should be the canonical form of the original bitmask
        self.assertEqual(ShapeGenerator.get_canonical_form(bitmask), normalized_bitmask)

    def test_isomorphic_shapes(self):
            shape1 = np.array([[1, 1, 0],
                            [1, 1, 0],
                            [0, 0, 0]])
            
            shape2 = np.array([[0, 0, 0],
                            [1, 1, 0],
                            [1, 1, 0]])

            # Assuming you have a method `are_isomorphic` that checks for isomorphic shapes
            self.assertTrue(ShapeGenerator.is_isomorphic(shape1, shape2))
            
            shape3 = np.array([[1, 0, 0],
                            [1, 1, 0],
                            [0, 1, 0]])
            
            shape4 = np.array([[0, 0, 0],
                            [0, 1, 1],
                            [1, 1, 0]])

            self.assertTrue(ShapeGenerator.is_isomorphic(shape3, shape4))

            shape5 = np.array([[1, 0, 0],
                            [1, 1, 0],
                            [0, 1, 0]])

            shape6 = np.array([[0, 0, 0],
                            [1, 1, 0],
                            [0, 1, 1]])

            self.assertFalse(ShapeGenerator.is_isomorphic(shape5, shape6))

    def test_bounding_boxes(self):
        shape_gen = ShapeGenerator()
        for shape, dimensions in shape_gen.bounding_boxes.items():
            shape_2D = np.array(ShapeGenerator.bitmask_to_2D(shape))
            filled_cells = np.argwhere(shape_2D == 1)
            min_row, min_col = np.min(filled_cells, axis=0)
            max_row, max_col = np.max(filled_cells, axis=0)
            bounding_box_dimensions = (max_row - min_row + 1, max_col - min_col + 1)
            self.assertEqual(dimensions, bounding_box_dimensions)

if __name__ == '__main__':
    unittest.main()