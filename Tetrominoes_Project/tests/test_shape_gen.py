import sys
sys.path.append('Z:\Tetrominoes_Project\src')
import unittest
from src.shape_generation import ShapeGenerator


class TestShapeGeneration(unittest.TestCase):
    # Test 1: is_contiguous
    def test_is_contiguous(self):
        shape1 = [[1, 0, 0],
                  [1, 1, 0],
                  [0, 0, 0]]
        self.assertTrue(ShapeGenerator.is_contiguous(shape1))

        shape2 = [[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]]
        self.assertFalse(ShapeGenerator.is_contiguous(shape2))


    # Test 2: rotation_permutations
    def test_rotation_permutations(self):
        shape = [[0, 1, 0],
                 [0, 1, 1],
                 [0, 0, 0]]
        
        rotated = [[0, 0, 0],
                   [0, 1, 0],
                   [1, 1, 0]]
        self.assertEqual(ShapeGenerator.rotation_permutations(shape),rotated)


    # Test 3: shape_normalization
    def test_shape_normalization(self):
        shape = [[0, 0, 1],
                 [1, 1, 0],
                 [0, 0, 0]]
        
        normalized = [[0, 1, 0],
                      [1, 0, 0],
                      [1, 0, 0]]
        self.assertEqual(ShapeGenerator.shape_normalization(shape), normalized)


    # Test 4: unique_shape_check
    def test_unique_shape_check(self):
        unique_shapes = ShapeGenerator.unique_shape_check(10)
        self.assertEqual(len(unique_shapes), 10)
        for shape in unique_shapes:
            self.assertTrue(ShapeGenerator.is_contiguous(shape))

if __name__ == '__main__':
    unittest.main()
